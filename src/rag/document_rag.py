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

    def generate_answer(self, question: str, context_chunks: List[Tuple[DocumentChunk, float]]) -> str:
        """
        Generate an answer to a question based on retrieved context

        Args:
            question: Question to answer
            context_chunks: Retrieved document chunks with similarity scores

        Returns:
            Generated answer
        """
        if not context_chunks:
            return ""

        # Build context from retrieved chunks
        context_parts = []
        for chunk, score in context_chunks:
            if score > 0.5:  # Only use chunks with reasonable similarity
                context_parts.append(f"[From {chunk.document_name}]:\n{chunk.content}")

        context = "\n\n---\n\n".join(context_parts)

        if not context:
            return ""

        # Generate answer using GPT
        prompt = f"""Based on the following project documentation, please answer this question:

Question: {question}

Project Documentation:
{context}

Instructions:
- Provide a clear, concise answer based ONLY on the information in the documentation
- If the documentation doesn't contain enough information, note what's missing
- Format the answer appropriately (bullet points, paragraphs, etc.)
- Be specific and cite relevant details from the documents

Answer:"""

        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an AI compliance assistant helping to extract information from project documentation to fill out compliance forms."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )

        return response.choices[0].message.content.strip()

    def answer_question(self, question: str, top_k: Optional[int] = None) -> Dict[str, Any]:
        """
        Answer a question using RAG

        Args:
            question: Question to answer
            top_k: Number of chunks to retrieve

        Returns:
            Dict with 'answer', 'sources', and 'confidence' keys
        """
        # Retrieve relevant chunks
        chunks = self.retrieve(question, top_k)

        if not chunks:
            return {
                "answer": "",
                "sources": [],
                "confidence": 0.0
            }

        # Generate answer
        answer = self.generate_answer(question, chunks)

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

        return {
            "answer": answer,
            "sources": sources,
            "confidence": float(avg_similarity)
        }

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
