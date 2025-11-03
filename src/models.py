"""Data models for AI Compliance Assistant"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class PathwayType(str, Enum):
    """Four main pathways for AI compliance"""
    BUILDING = "building"
    PROCURING = "procuring"
    OPERATING = "operating"
    TRAINING = "training"


class RegulatoryFramework(str, Enum):
    """Supported regulatory frameworks"""
    EU_AI_ACT = "eu_ai_act"
    SAUDI_AI = "saudi_ai"
    BOTH = "both"


class RiskLevel(str, Enum):
    """EU AI Act risk classification"""
    UNACCEPTABLE = "unacceptable"
    HIGH = "high"
    LIMITED = "limited"
    MINIMAL = "minimal"


class StepStatus(str, Enum):
    """Status of a compliance step"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"


class Document(BaseModel):
    """Uploaded document"""
    id: str
    filename: str
    file_type: str
    upload_date: datetime = Field(default_factory=datetime.now)
    content: Optional[str] = None
    summary: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class UserGoal(BaseModel):
    """User's compliance goal"""
    description: str
    pathway: PathwayType
    regulatory_framework: RegulatoryFramework = RegulatoryFramework.BOTH
    timeline: Optional[str] = None
    additional_context: Optional[str] = None


class ComplianceStep(BaseModel):
    """A step in the compliance pathway"""
    id: str
    title: str
    description: str
    order: int
    status: StepStatus = StepStatus.NOT_STARTED
    guidance: Optional[str] = None
    required_documents: List[str] = Field(default_factory=list)
    checklist_items: List[str] = Field(default_factory=list)
    resources: List[Dict[str, str]] = Field(default_factory=list)
    user_notes: Optional[str] = None
    completed_at: Optional[datetime] = None


class UserFeedback(BaseModel):
    """User feedback on a step"""
    step_id: str
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    needs_more_help: bool = False
    suggested_changes: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)


class PathwaySession(BaseModel):
    """A user's compliance session"""
    session_id: str
    user_goal: UserGoal
    pathway_type: PathwayType
    steps: List[ComplianceStep] = Field(default_factory=list)
    documents: List[Document] = Field(default_factory=list)
    feedback_history: List[UserFeedback] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    current_step_index: int = 0


class PathwayConfig(BaseModel):
    """Configuration for a pathway"""
    pathway_type: PathwayType
    name: str
    description: str
    icon: str
    default_steps: List[str]
    regulatory_focus: List[RegulatoryFramework]
