"""Document upload and processing"""

import os
import uuid
from typing import Optional, List
from datetime import datetime
from pathlib import Path
import PyPDF2
import docx

from src.models import Document


class DocumentProcessor:
    """Process and extract text from uploaded documents"""

    SUPPORTED_FORMATS = {".pdf", ".docx", ".txt", ".md"}
    MAX_FILE_SIZE_MB = 10

    def __init__(self, upload_dir: str = "uploads"):
        """
        Initialize document processor

        Args:
            upload_dir: Directory to store uploaded files
        """
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(exist_ok=True, parents=True)

    def process_upload(
        self, file_path: str, original_filename: str
    ) -> Optional[Document]:
        """
        Process an uploaded file

        Args:
            file_path: Path to the uploaded file
            original_filename: Original filename

        Returns:
            Document object if successful, None otherwise
        """
        file_ext = Path(original_filename).suffix.lower()

        if file_ext not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported file format: {file_ext}. Supported: {', '.join(self.SUPPORTED_FORMATS)}"
            )

        # Check file size
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > self.MAX_FILE_SIZE_MB:
            raise ValueError(
                f"File too large ({file_size_mb:.2f}MB). Max size: {self.MAX_FILE_SIZE_MB}MB"
            )

        # Extract text based on file type
        content = self._extract_text(file_path, file_ext)

        # Create document object
        doc = Document(
            id=str(uuid.uuid4()),
            filename=original_filename,
            file_type=file_ext,
            content=content,
            metadata={
                "size_bytes": os.path.getsize(file_path),
                "size_mb": round(file_size_mb, 2),
            },
        )

        return doc

    def _extract_text(self, file_path: str, file_ext: str) -> str:
        """
        Extract text from a file based on its extension

        Args:
            file_path: Path to file
            file_ext: File extension

        Returns:
            Extracted text content
        """
        if file_ext == ".pdf":
            return self._extract_from_pdf(file_path)
        elif file_ext == ".docx":
            return self._extract_from_docx(file_path)
        elif file_ext in [".txt", ".md"]:
            return self._extract_from_text(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")

    def _extract_from_pdf(self, file_path: str) -> str:
        """Extract text from PDF"""
        text_content = []

        try:
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)

                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text_content.append(page.extract_text())

            return "\n\n".join(text_content)

        except Exception as e:
            raise ValueError(f"Error extracting PDF text: {str(e)}")

    def _extract_from_docx(self, file_path: str) -> str:
        """Extract text from DOCX"""
        try:
            doc = docx.Document(file_path)
            paragraphs = [paragraph.text for paragraph in doc.paragraphs]
            return "\n\n".join(paragraphs)

        except Exception as e:
            raise ValueError(f"Error extracting DOCX text: {str(e)}")

    def _extract_from_text(self, file_path: str) -> str:
        """Extract text from plain text file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        except UnicodeDecodeError:
            # Try with latin-1 encoding
            with open(file_path, "r", encoding="latin-1") as file:
                return file.read()

        except Exception as e:
            raise ValueError(f"Error reading text file: {str(e)}")

    def extract_key_information(self, content: str) -> dict:
        """
        Extract key information from document content

        Args:
            content: Document text content

        Returns:
            Dictionary with extracted information
        """
        # Simple keyword-based extraction
        # In production, this could use NLP or LLM-based extraction

        info = {
            "mentions_ai": any(
                keyword in content.lower()
                for keyword in ["artificial intelligence", "machine learning", "ai system", "neural network"]
            ),
            "mentions_data": any(
                keyword in content.lower()
                for keyword in ["data processing", "personal data", "dataset", "training data"]
            ),
            "mentions_compliance": any(
                keyword in content.lower()
                for keyword in ["compliance", "regulation", "gdpr", "ai act"]
            ),
            "word_count": len(content.split()),
            "has_tables": "table" in content.lower() or "|" in content,
        }

        return info

    def chunk_content(self, content: str, chunk_size: int = 1000) -> List[str]:
        """
        Split content into chunks for processing

        Args:
            content: Full document content
            chunk_size: Maximum words per chunk

        Returns:
            List of content chunks
        """
        words = content.split()
        chunks = []

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i : i + chunk_size])
            chunks.append(chunk)

        return chunks
