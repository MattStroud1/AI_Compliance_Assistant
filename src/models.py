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
    # ROPA-specific fields for saving answers
    current_state_answer: Optional[str] = None  # What the organization currently has
    gap_analysis_answer: Optional[str] = None  # Gaps identified between current and ideal state
    project_id: Optional[str] = None  # Added for compatibility
    phase: Optional[str] = None  # Added for compatibility


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


# ============================================================================
# NEOM TRUSTWORTHY AI MODELS
# ============================================================================

class PhaseType(str, Enum):
    """Four phases of NEOM Trustworthy AI development"""
    PLANNING_DESIGN = "planning_design"
    DATA_PREPARATION = "data_preparation"
    BUILD_VALIDATE = "build_validate"
    DEPLOYMENT_MONITORING = "deployment_monitoring"


class PitstopStatus(str, Enum):
    """Status of a pitstop checkpoint"""
    PENDING = "pending"
    SCHEDULED = "scheduled"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    ISSUES_RAISED = "issues_raised"


class RACIRole(str, Enum):
    """RACI role types"""
    RESPONSIBLE = "responsible"  # Does the work
    ACCOUNTABLE = "accountable"  # Ultimately answerable
    CONSULTED = "consulted"      # Provides input
    INFORMED = "informed"        # Kept updated


class EvidenceType(str, Enum):
    """Types of evidence that can be collected"""
    DOCUMENT = "document"
    CHECKLIST = "checklist"
    ASSESSMENT = "assessment"
    METRIC = "metric"
    SIGN_OFF = "sign_off"


class RACIEntry(BaseModel):
    """A single entry in the RACI matrix"""
    task_name: str
    responsible: List[str] = Field(default_factory=list)  # Email addresses
    accountable: List[str] = Field(default_factory=list)
    consulted: List[str] = Field(default_factory=list)
    informed: List[str] = Field(default_factory=list)
    notes: Optional[str] = None


class RACIMatrix(BaseModel):
    """Complete RACI matrix for a project"""
    project_id: str
    entries: List[RACIEntry] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    version: int = 1
    approved_by: Optional[str] = None
    approved_at: Optional[datetime] = None


class Evidence(BaseModel):
    """A piece of evidence collected during compliance journey"""
    id: str
    project_id: str
    phase: PhaseType
    step_id: str
    evidence_type: EvidenceType
    title: str
    description: Optional[str] = None

    # For documents
    file_path: Optional[str] = None
    file_name: Optional[str] = None

    # For checklists/assessments
    questions: Dict[str, Any] = Field(default_factory=dict)
    answers: Dict[str, Any] = Field(default_factory=dict)

    # For metrics
    metric_value: Optional[float] = None
    threshold: Optional[float] = None

    # For sign-offs
    signed_by: Optional[str] = None
    signed_at: Optional[datetime] = None

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class PitstopCheckpoint(BaseModel):
    """A pitstop meeting checkpoint between phases"""
    id: str
    project_id: str
    phase_completed: PhaseType
    status: PitstopStatus = PitstopStatus.PENDING

    scheduled_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None

    # Participants
    pdpo_reviewer: Optional[str] = None  # Email
    participants: List[str] = Field(default_factory=list)  # Emails

    # Review items
    evidence_reviewed: List[str] = Field(default_factory=list)  # Evidence IDs
    issues_raised: List[str] = Field(default_factory=list)
    action_items: List[str] = Field(default_factory=list)

    # Decision
    approved: bool = False
    approval_notes: Optional[str] = None
    approved_by: Optional[str] = None
    approved_at: Optional[datetime] = None

    # Notifications
    notification_sent: bool = False
    reminder_sent: bool = False


class NEOMPhase(BaseModel):
    """A phase in the NEOM Trustworthy AI process"""
    id: str
    project_id: str
    phase_type: PhaseType
    name: str
    description: str
    order: int

    steps: List[ComplianceStep] = Field(default_factory=list)
    evidence_collected: List[str] = Field(default_factory=list)  # Evidence IDs

    status: StepStatus = StepStatus.NOT_STARTED
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    pitstop_id: Optional[str] = None  # Links to pitstop checkpoint


class NEOMProject(BaseModel):
    """A NEOM Trustworthy AI project"""
    project_id: str
    project_name: str
    description: Optional[str] = None

    # Project metadata
    ai_system_name: str
    ai_system_purpose: str
    risk_level: Optional[RiskLevel] = None

    # Governance
    raci_matrix: Optional[RACIMatrix] = None
    project_lead: Optional[str] = None  # Email
    pdpo_contact: Optional[str] = None  # Email

    # Phases
    phases: List[NEOMPhase] = Field(default_factory=list)
    current_phase_index: int = 0

    # Evidence & documents
    evidence: List[Evidence] = Field(default_factory=list)
    documents: List[Document] = Field(default_factory=list)

    # Pitstops
    pitstops: List[PitstopCheckpoint] = Field(default_factory=list)

    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Status
    overall_status: str = "initiated"  # initiated, in_progress, under_review, approved, deployed


class TaskReference(BaseModel):
    """Reference to a specific task in the Trustworthy AI Playbook"""
    task_id: str  # e.g., "2.1", "3.5"
    section: str  # e.g., "Data & Privacy", "Security"
    description: str
    phase: PhaseType
    mandatory: bool = True
    evidence_required: List[EvidenceType] = Field(default_factory=list)
