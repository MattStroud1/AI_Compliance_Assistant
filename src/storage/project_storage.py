"""File storage system for NEOM projects"""

import os
import shutil
from pathlib import Path
from typing import Optional, List
from datetime import datetime
import uuid

from src.models import NEOMProject, Evidence, Document, EvidenceType


class ProjectStorageManager:
    """Manages file storage for NEOM compliance projects"""

    def __init__(self, base_storage_path: str = "project_storage"):
        """
        Initialize storage manager

        Args:
            base_storage_path: Base directory for all project storage
        """
        self.base_path = Path(base_storage_path)
        self.base_path.mkdir(exist_ok=True, parents=True)

    def create_project_folder(self, project_id: str) -> Path:
        """
        Create folder structure for a new project

        Structure:
        project_storage/
        └── {project_id}/
            ├── documents/          # Uploaded documents
            ├── evidence/           # Distilled evidence
            │   ├── planning_design/
            │   ├── data_preparation/
            │   ├── build_validate/
            │   └── deployment_monitoring/
            ├── reports/            # Generated reports
            └── exports/            # Exported compliance packages

        Args:
            project_id: Unique project identifier

        Returns:
            Path to project root folder
        """
        project_path = self.base_path / project_id

        # Create main directories
        (project_path / "documents").mkdir(parents=True, exist_ok=True)
        (project_path / "evidence" / "planning_design").mkdir(parents=True, exist_ok=True)
        (project_path / "evidence" / "data_preparation").mkdir(parents=True, exist_ok=True)
        (project_path / "evidence" / "build_validate").mkdir(parents=True, exist_ok=True)
        (project_path / "evidence" / "deployment_monitoring").mkdir(parents=True, exist_ok=True)
        (project_path / "reports").mkdir(parents=True, exist_ok=True)
        (project_path / "exports").mkdir(parents=True, exist_ok=True)

        return project_path

    def save_document(
        self,
        project_id: str,
        file_path: str,
        original_filename: str,
        metadata: Optional[dict] = None
    ) -> Document:
        """
        Save an uploaded document to project storage

        Args:
            project_id: Project identifier
            file_path: Temporary file path
            original_filename: Original filename
            metadata: Optional metadata

        Returns:
            Document object with storage location
        """
        project_path = self.base_path / project_id / "documents"
        project_path.mkdir(parents=True, exist_ok=True)

        # Generate unique filename
        file_ext = Path(original_filename).suffix
        unique_id = str(uuid.uuid4())[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"{timestamp}_{unique_id}_{original_filename}"

        # Copy file to project storage
        destination = project_path / new_filename
        shutil.copy2(file_path, destination)

        # Create document record
        doc = Document(
            id=unique_id,
            filename=original_filename,
            file_type=file_ext,
            metadata=metadata or {}
        )

        # Store the relative path
        doc.metadata["storage_path"] = str(destination.relative_to(self.base_path))

        return doc

    def save_evidence(
        self,
        project_id: str,
        evidence: Evidence
    ) -> Path:
        """
        Save evidence to project storage

        Args:
            project_id: Project identifier
            evidence: Evidence object to save

        Returns:
            Path to saved evidence file
        """
        # Determine evidence subfolder based on phase
        phase_folder = evidence.phase.value
        evidence_path = self.base_path / project_id / "evidence" / phase_folder

        evidence_path.mkdir(parents=True, exist_ok=True)

        # Create filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{evidence.evidence_type.value}_{evidence.id}_{timestamp}.json"

        # Save evidence as JSON
        file_path = evidence_path / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(evidence.model_dump_json(indent=2))

        return file_path

    def get_document(self, project_id: str, document_id: str) -> Optional[Path]:
        """
        Retrieve a document from storage

        Args:
            project_id: Project identifier
            document_id: Document identifier

        Returns:
            Path to document if found, None otherwise
        """
        docs_path = self.base_path / project_id / "documents"

        for file in docs_path.glob(f"*_{document_id}_*"):
            return file

        return None

    def get_all_evidence(
        self,
        project_id: str,
        phase: Optional[str] = None
    ) -> List[Path]:
        """
        Get all evidence files for a project

        Args:
            project_id: Project identifier
            phase: Optional phase filter

        Returns:
            List of paths to evidence files
        """
        if phase:
            evidence_path = self.base_path / project_id / "evidence" / phase
            return list(evidence_path.glob("*.json"))
        else:
            evidence_base = self.base_path / project_id / "evidence"
            return list(evidence_base.rglob("*.json"))

    def export_project(
        self,
        project_id: str,
        export_name: Optional[str] = None
    ) -> Path:
        """
        Create a complete export of project data

        Args:
            project_id: Project identifier
            export_name: Optional name for export file

        Returns:
            Path to export archive
        """
        if not export_name:
            export_name = f"{project_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        exports_path = self.base_path / project_id / "exports"
        exports_path.mkdir(parents=True, exist_ok=True)

        # Create archive of entire project
        project_path = self.base_path / project_id
        archive_path = exports_path / export_name

        shutil.make_archive(
            str(archive_path),
            'zip',
            str(project_path.parent),
            str(project_path.name)
        )

        return Path(str(archive_path) + '.zip')

    def get_storage_stats(self, project_id: str) -> dict:
        """
        Get storage statistics for a project

        Args:
            project_id: Project identifier

        Returns:
            Dictionary with storage statistics
        """
        project_path = self.base_path / project_id

        if not project_path.exists():
            return {"error": "Project not found"}

        def get_folder_size(path: Path) -> int:
            """Calculate total size of folder"""
            return sum(f.stat().st_size for f in path.rglob('*') if f.is_file())

        stats = {
            "project_id": project_id,
            "total_size_bytes": get_folder_size(project_path),
            "documents_count": len(list((project_path / "documents").glob('*'))),
            "evidence_count": len(list((project_path / "evidence").rglob('*.json'))),
            "reports_count": len(list((project_path / "reports").glob('*'))),
            "exports_count": len(list((project_path / "exports").glob('*.zip'))),
        }

        # Convert bytes to MB
        stats["total_size_mb"] = round(stats["total_size_bytes"] / (1024 * 1024), 2)

        return stats

    def delete_project(self, project_id: str, confirm: bool = False) -> bool:
        """
        Delete all project data (use with caution!)

        Args:
            project_id: Project identifier
            confirm: Must be True to actually delete

        Returns:
            True if deleted, False otherwise
        """
        if not confirm:
            return False

        project_path = self.base_path / project_id

        if project_path.exists():
            shutil.rmtree(project_path)
            return True

        return False
