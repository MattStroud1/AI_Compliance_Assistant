"""
RAG (Retrieval-Augmented Generation) System for AI Compliance Assistant

This module handles document chunking, embedding, and retrieval to intelligently
populate compliance questions from uploaded project documents.
"""

import os
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
import numpy as np
from dataclasses import dataclass
import json

from openai import OpenAI

# Excel reading functionality
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False


@dataclass
class DocumentChunk:
    """A chunk of text from a document"""
    chunk_id: str
    document_id: str
    document_name: str
    content: str
    chunk_index: int
    metadata: Dict[str, Any]
    embedding: Optional[np.ndarray] = None


class DocumentRAG:
    """
    RAG system for extracting and retrieving information from project documents
    """

    def __init__(self, openai_api_key: Optional[str] = None):
        """
        Initialize RAG system

        Args:
            openai_api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
        """
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required for RAG system")

        self.client = OpenAI(api_key=self.api_key)
        self.chunks: List[DocumentChunk] = []
        self.embeddings: Optional[np.ndarray] = None

        # RAG configuration
        self.chunk_size = 800  # tokens per chunk
        self.chunk_overlap = 200  # token overlap between chunks
        self.embedding_model = "text-embedding-3-small"
        self.top_k = 5  # number of chunks to retrieve

    def chunk_text(self, text: str, document_id: str, document_name: str) -> List[DocumentChunk]:
        """
        Split text into overlapping chunks

        Args:
            text: Document text
            document_id: Unique document identifier
            document_name: Human-readable document name

        Returns:
            List of document chunks
        """
        # Simple word-based chunking (roughly 800 tokens ≈ 600 words)
        words = text.split()
        chunk_size_words = int(self.chunk_size * 0.75)  # Conservative estimate
        overlap_words = int(self.chunk_overlap * 0.75)

        chunks = []
        for i in range(0, len(words), chunk_size_words - overlap_words):
            chunk_words = words[i:i + chunk_size_words]
            chunk_text = " ".join(chunk_words)

            if chunk_text.strip():
                chunk = DocumentChunk(
                    chunk_id=f"{document_id}_chunk_{len(chunks)}",
                    document_id=document_id,
                    document_name=document_name,
                    content=chunk_text,
                    chunk_index=len(chunks),
                    metadata={
                        "word_count": len(chunk_words),
                        "char_count": len(chunk_text)
                    }
                )
                chunks.append(chunk)

        return chunks

    def generate_embeddings(self, chunks: List[DocumentChunk]) -> np.ndarray:
        """
        Generate embeddings for document chunks

        Args:
            chunks: List of document chunks

        Returns:
            Numpy array of embeddings (shape: [num_chunks, embedding_dim])
        """
        texts = [chunk.content for chunk in chunks]

        # Batch embedding generation (OpenAI supports up to 2048 inputs)
        batch_size = 100
        all_embeddings = []

        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i + batch_size]
            response = self.client.embeddings.create(
                input=batch_texts,
                model=self.embedding_model
            )
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)

        embeddings_array = np.array(all_embeddings)

        # Store embeddings in chunks
        for chunk, embedding in zip(chunks, all_embeddings):
            chunk.embedding = np.array(embedding)

        return embeddings_array

    def add_documents(self, documents: List[Dict[str, str]]):
        """
        Add documents to the RAG system

        Args:
            documents: List of dicts with 'id', 'name', and 'content' keys
        """
        new_chunks = []

        for doc in documents:
            doc_chunks = self.chunk_text(
                doc['content'],
                doc['id'],
                doc['name']
            )
            new_chunks.extend(doc_chunks)

        if new_chunks:
            # Generate embeddings for new chunks
            self.generate_embeddings(new_chunks)
            self.chunks.extend(new_chunks)

            # Rebuild embeddings matrix
            self.embeddings = np.array([chunk.embedding for chunk in self.chunks])

    def retrieve(self, query: str, top_k: Optional[int] = None) -> List[Tuple[DocumentChunk, float]]:
        """
        Retrieve most relevant document chunks for a query

        Args:
            query: Search query
            top_k: Number of chunks to retrieve (defaults to self.top_k)

        Returns:
            List of (chunk, similarity_score) tuples, sorted by relevance
        """
        if not self.chunks or self.embeddings is None:
            return []

        top_k = top_k or self.top_k

        # Generate query embedding
        response = self.client.embeddings.create(
            input=[query],
            model=self.embedding_model
        )
        query_embedding = np.array(response.data[0].embedding)

        # Calculate cosine similarity
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )

        # Get top-k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        results = [
            (self.chunks[idx], float(similarities[idx]))
            for idx in top_indices
        ]

        return results

    def generate_answer(self, question: str, context_chunks: List[Tuple[DocumentChunk, float]], guidance: str = "") -> str:
        """
        Generate an answer to a question based on retrieved context

        Args:
            question: Question to answer
            context_chunks: Retrieved document chunks with similarity scores
            guidance: Guidance on what should be covered (for structuring)

        Returns:
            Generated answer extracted from documents, structured to match guidance
        """
        if not context_chunks:
            return "No relevant information found in uploaded documents."

        # Build context from retrieved chunks (lowered threshold to 0.3)
        context_parts = []
        max_score = 0.0
        for chunk, score in context_chunks:
            max_score = max(max_score, score)
            if score > 0.3:  # Lowered from 0.5 to capture more context
                context_parts.append(f"[From {chunk.document_name}]:\n{chunk.content}")

        context = "\n\n---\n\n".join(context_parts)

        if not context:
            return f"No sufficiently relevant information found in documents (highest relevance: {max_score:.0%}). The uploaded documents may not contain details about this specific requirement."

        # Generate answer using GPT - structured to match guidance
        guidance_structure = f"\n\nStructure your answer to address these points if information is available:\n{guidance}" if guidance else ""

        prompt = f"""You are extracting specific information from project documentation to answer a compliance question.

Question: {question}

Project Documentation:
{context}{guidance_structure}

Instructions:
- Extract and summarize ONLY the relevant factual information found in the documentation
- Structure your answer using numbered sections that match the guidance points (if provided)
- For each section, extract what IS available from the documents
- If specific data, names, dates, processes, or details are mentioned, include them
- Do NOT provide generic guidance or suggestions
- Do NOT say what "should" be done - only say what IS described in the documents
- If a section has no information in the documents, write: "[No information found in documents]"
- Be specific with facts, numbers, names, and concrete details from the documents

Format your answer with numbered sections like:
1. [Section topic]: [Extracted information or "No information found in documents"]
2. [Section topic]: [Extracted information or "No information found in documents"]

Extracted Information:"""

        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are extracting factual information from project documents. Structure your response to match the guidance sections. Only report what is explicitly stated in the documents."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,  # Lower temperature for more factual extraction
            max_tokens=800
        )

        return response.choices[0].message.content.strip()

    def generate_guidance(self, question: str) -> str:
        """
        Generate guidance on what an ideal answer should cover

        Args:
            question: The compliance question

        Returns:
            Guidance text describing what should be included in the answer
        """
        prompt = f"""For this AI compliance question, provide brief guidance on what an ideal answer should cover.

Question: {question}

Provide a concise description (2-4 bullet points) of what information should ideally be included in the answer to properly address this compliance requirement.

Focus on WHAT to include, not HOW to do it.

Guidance:"""

        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a compliance expert providing guidance on what information compliance answers should contain."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    def analyze_gaps(self, extracted_answer: str, guidance: str, question: str) -> str:
        """
        Analyze gaps between extracted answer and ideal answer

        Args:
            extracted_answer: What was found in documents
            guidance: What should ideally be covered
            question: The original question

        Returns:
            Gap analysis describing what's missing and needs to be added
        """
        prompt = f"""Compare what was extracted from documents versus what should ideally be covered, and identify gaps.

Question: {question}

What Should Be Covered (Ideal):
{guidance}

What Was Found in Documents (Actual):
{extracted_answer}

Instructions:
- Identify which parts of the ideal answer are missing or incomplete in the extracted answer
- Be specific about what information is lacking
- Suggest what the user needs to add to complete the answer
- If the extracted answer is complete, say "The extracted information appears complete."
- Use bullet points for clarity

Gap Analysis:"""

        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are analyzing gaps in compliance documentation. Be specific and actionable."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    def answer_question(self, question: str, top_k: Optional[int] = None) -> Dict[str, Any]:
        """
        Answer a question using RAG

        Args:
            question: Question to answer
            top_k: Number of chunks to retrieve

        Returns:
            Dict with 'answer', 'guidance', 'gap_analysis', 'sources', and 'confidence' keys
        """
        # Retrieve relevant chunks
        chunks = self.retrieve(question, top_k)

        # Generate guidance (what should be covered)
        guidance = self.generate_guidance(question)

        if not chunks:
            return {
                "answer": "No relevant information found in uploaded documents.",
                "guidance": guidance,
                "gap_analysis": "All information is missing from documents. Please add all required details manually.",
                "sources": [],
                "confidence": 0.0
            }

        # Generate answer (what was found in docs) - structured to match guidance
        answer = self.generate_answer(question, chunks, guidance)

        # Calculate confidence (average similarity of top chunks)
        avg_similarity = np.mean([score for _, score in chunks[:3]])

        # Extract sources
        sources = [
            {
                "document": chunk.document_name,
                "excerpt": chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content,
                "similarity": float(score)
            }
            for chunk, score in chunks[:3]
        ]

        # Analyze gaps between what was found vs what should be covered
        gap_analysis = self.analyze_gaps(answer, guidance, question)

        return {
            "answer": answer,
            "guidance": guidance,
            "gap_analysis": gap_analysis,
            "sources": sources,
            "confidence": float(avg_similarity)
        }

    def add_excel_knowledge_base(self, filepath: str, kb_type: str = "generic") -> int:
        """
        Load an Excel file and add each row as a document chunk to the RAG system.

        Args:
            filepath: Path to Excel file
            kb_type: Type of knowledge base ("risk_register" or "controls" or "generic")

        Returns:
            Number of rows added to the RAG system
        """
        if not PANDAS_AVAILABLE:
            print("pandas not available - cannot load Excel files")
            return 0

        try:
            # Load Excel file
            df = pd.read_excel(filepath)

            # Convert each row to a text document
            documents = []
            for idx, row in df.iterrows():
                # Convert row to a readable text format
                row_text_parts = []
                for col_name, value in row.items():
                    if pd.notna(value):  # Skip NaN values
                        row_text_parts.append(f"{col_name}: {value}")

                row_text = "\n".join(row_text_parts)

                # Create a document for this row
                doc = {
                    'id': f"{kb_type}_{idx}",
                    'name': f"{kb_type.replace('_', ' ').title()} - Row {idx + 1}",
                    'content': row_text
                }
                documents.append(doc)

            # Add documents to RAG system
            self.add_documents(documents)

            print(f"✅ Added {len(documents)} rows from {kb_type} to RAG system")
            return len(documents)

        except FileNotFoundError:
            print(f"❌ File not found: {filepath}")
            return 0
        except Exception as e:
            print(f"❌ Error loading Excel file: {e}")
            return 0

    def retrieve_knowledge_base_entries(
        self,
        query: str,
        kb_type: Optional[str] = None,
        top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant knowledge base entries for a query.

        Args:
            query: Search query describing what you're looking for
            kb_type: Optional filter by KB type ("risk_register" or "controls")
            top_k: Number of entries to retrieve

        Returns:
            List of dicts with 'content', 'similarity', and 'source' keys
        """
        # Retrieve chunks
        chunks = self.retrieve(query, top_k=top_k * 2)  # Get more to allow filtering

        # Filter by kb_type if specified
        if kb_type:
            chunks = [(chunk, score) for chunk, score in chunks if kb_type in chunk.chunk_id]

        # Take top_k after filtering
        chunks = chunks[:top_k]

        # Format results
        results = []
        for chunk, score in chunks:
            results.append({
                'content': chunk.content,
                'similarity': float(score),
                'source': chunk.document_name,
                'chunk_id': chunk.chunk_id
            })

        return results

    def save(self, filepath: str):
        """Save RAG state to disk"""
        data = {
            "chunks": [
                {
                    "chunk_id": c.chunk_id,
                    "document_id": c.document_id,
                    "document_name": c.document_name,
                    "content": c.content,
                    "chunk_index": c.chunk_index,
                    "metadata": c.metadata,
                    "embedding": c.embedding.tolist() if c.embedding is not None else None
                }
                for c in self.chunks
            ]
        }

        with open(filepath, 'w') as f:
            json.dump(data, f)

    def load(self, filepath: str):
        """Load RAG state from disk"""
        with open(filepath, 'r') as f:
            data = json.load(f)

        self.chunks = [
            DocumentChunk(
                chunk_id=c["chunk_id"],
                document_id=c["document_id"],
                document_name=c["document_name"],
                content=c["content"],
                chunk_index=c["chunk_index"],
                metadata=c["metadata"],
                embedding=np.array(c["embedding"]) if c["embedding"] else None
            )
            for c in data["chunks"]
        ]

        if self.chunks and self.chunks[0].embedding is not None:
            self.embeddings = np.array([c.embedding for c in self.chunks])
