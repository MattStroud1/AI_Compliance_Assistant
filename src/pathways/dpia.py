"""DPIA pathway - for conducting Data Protection Impact Assessments"""

import uuid
from typing import List
from datetime import datetime

from src.models import (
    NEOMPhase,
    ComplianceStep,
    StepStatus,
    PhaseType
)


class DPIAPathway:
    """
    DPIA pathway for conducting Data Protection Impact Assessments
    Based on UK ICO guidance for GDPR compliance
    """

    def __init__(self):
        self.pathway_name = "DPIA (Data Protection Impact Assessment)"
        self.description = "8-step journey for conducting comprehensive DPIAs under UK GDPR"

    def create_phases(self, project_id: str) -> List[NEOMPhase]:
        """Create DPIA phases: Screening & Scoping, Consultation & Assessment, Risk Analysis, Completion & Maintenance"""
        return [
            self._create_phase_1_screening_scoping(project_id),
            self._create_phase_2_consultation_assessment(project_id),
            self._create_phase_3_risk_analysis(project_id),
            self._create_phase_4_completion_maintenance(project_id),
        ]

    def _create_phase_1_screening_scoping(self, project_id: str) -> NEOMPhase:
        """Phase 1: Screening & Scoping (Steps 1-2)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 1: Identify the Need for a DPIA",
                description="Determine whether your processing operations require a DPIA under UK GDPR",
                order=1,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
A DPIA is mandatory for certain types of processing that are likely to result in a high risk to individuals' rights and freedoms. Failure to conduct a DPIA when required can result in fines up to £8.7 million or 2% of global annual turnover.

**What to do:**
Screen your processing activities against the mandatory DPIA criteria to determine if a DPIA is required.

**How to proceed:**
Review your processing against these criteria:
""",
                checklist_items=[
                    "Systematic and extensive profiling with significant effects on individuals",
                    "Large scale processing of special category data (health, genetic, biometric, etc.)",
                    "Systematic monitoring of publicly accessible areas on a large scale",
                    "Use of innovative technology (AI, machine learning, novel applications)",
                    "Automated decision-making affecting access to services or benefits",
                    "Large-scale profiling of individuals",
                    "Processing of biometric or genetic data",
                    "Data matching from multiple sources",
                    "Invisible processing (data not obtained directly from individuals)",
                    "Tracking individuals' location or behaviour",
                    "Targeting children or vulnerable individuals",
                    "Processing that could jeopardize physical health or safety if breached",
                    "Document your decision and reasoning (even if DPIA not required)",
                ],
                project_id=project_id,
                phase="Screening & Scoping"
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 2: Describe the Processing",
                description="Provide a comprehensive description of the processing including nature, scope, context and purposes",
                order=2,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
A clear description of your processing activities is the foundation of your DPIA. This helps identify potential risks and demonstrates compliance with transparency principles.

**What to do:**
Document all aspects of how personal data will be collected, used, stored, and shared.

**How to proceed:**
Describe your processing across four key dimensions:
""",
                checklist_items=[
                    "NATURE: How you collect, store, use, and share the data",
                    "NATURE: Who has access to the data (internal staff, processors, third parties)",
                    "NATURE: Retention periods and deletion procedures",
                    "NATURE: Security measures in place",
                    "NATURE: Use of new or novel technologies",
                    "SCOPE: Types and categories of personal data involved",
                    "SCOPE: Volume and variety of data",
                    "SCOPE: Sensitivity of the data (special category data?)",
                    "SCOPE: Number of individuals affected and frequency of processing",
                    "SCOPE: Duration of processing and geographical area",
                    "CONTEXT: Source of the data (direct from individuals or third parties)",
                    "CONTEXT: Nature of relationship with individuals",
                    "CONTEXT: Level of control individuals have over their data",
                    "CONTEXT: Whether processing aligns with individuals' reasonable expectations",
                    "CONTEXT: Whether individuals include vulnerable groups (children, elderly, patients)",
                    "PURPOSE: Why you are processing the data (legitimate interests)",
                    "PURPOSE: Intended outcome for individuals",
                    "PURPOSE: Expected benefits for your organization and society",
                ],
                project_id=project_id,
                phase="Screening & Scoping"
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,
            name="Phase 1: Screening & Scoping",
            description="Identify DPIA requirements and describe processing activities",
            order=1,
            steps=steps
        )

    def _create_phase_2_consultation_assessment(self, project_id: str) -> NEOMPhase:
        """Phase 2: Consultation & Assessment (Steps 3-4)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 3: Consider Consultation",
                description="Seek and document the views of individuals and other stakeholders",
                order=3,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
Consultation helps you understand how individuals might be affected by your processing and demonstrates transparency. It can reveal concerns or risks you hadn't considered.

**What to do:**
Consult with data subjects, your DPO, processors, and other relevant stakeholders.

**How to proceed:**
Plan and execute consultation activities:
""",
                checklist_items=[
                    "Identify who you need to consult (individuals, representatives, DPO, processors)",
                    "For existing contacts: Design process to seek views of specific individuals",
                    "For future data subjects: Consider public consultation or targeted research",
                    "Consult with your Data Protection Officer (DPO) if you have one",
                    "Request information and assistance from processors",
                    "Engage information security staff",
                    "Consider legal advice or independent experts if needed",
                    "Document all consultation responses and views received",
                    "If you decide not to consult, document your reasons",
                    "If your decision differs from consultation views, record your reasoning",
                ],
                project_id=project_id,
                phase="Consultation & Assessment"
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 4: Assess Necessity and Proportionality",
                description="Evaluate whether the processing is necessary and proportionate to achieve your objectives",
                order=4,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
UK GDPR requires that processing be necessary and proportionate. This assessment helps demonstrate compliance with data protection principles and identifies opportunities to minimize data collection.

**What to do:**
Assess whether your processing helps achieve your purpose and whether there are alternative approaches.

**How to proceed:**
Evaluate necessity and proportionality across key compliance areas:
""",
                checklist_items=[
                    "Confirm your processing helps achieve your stated purpose",
                    "Consider if there's another reasonable way to achieve the same result",
                    "Identify your lawful basis for processing",
                    "Explain how you will prevent function creep (using data for new purposes)",
                    "Describe measures to ensure data quality and accuracy",
                    "Demonstrate data minimisation (only collect what you need)",
                    "Explain how you'll provide privacy information to individuals",
                    "Detail how you'll support individuals exercising their rights",
                    "Confirm measures to ensure processor compliance",
                    "Document safeguards for international transfers (if applicable)",
                    "Specify who will have access and any access restrictions needed",
                    "Describe data storage locations and security measures",
                    "Define retention periods and secure deletion procedures",
                    "Confirm relevant staff have received data protection training",
                ],
                project_id=project_id,
                phase="Consultation & Assessment"
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Phase 2: Consultation & Assessment",
            description="Engage stakeholders and assess necessity and proportionality",
            order=2,
            steps=steps
        )

    def _create_phase_3_risk_analysis(self, project_id: str) -> NEOMPhase:
        """Phase 3: Risk Analysis (Steps 5-6)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 5: Identify and Assess Risks",
                description="Identify privacy risks and assess their likelihood and severity",
                order=5,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
Risk assessment is the core of your DPIA. It helps you understand potential harm to individuals and prioritize mitigation efforts. UK GDPR requires assessment of both likelihood and severity.

**What to do:**
Identify potential harms and assess risks using a structured approach considering likelihood and severity.

**How to proceed:**
Evaluate risks to individuals' rights and freedoms:
""",
                checklist_items=[
                    "Inability to exercise rights (including privacy rights)",
                    "Inability to access services or opportunities",
                    "Loss of control over personal data",
                    "Discrimination or unfair treatment",
                    "Identity theft or fraud",
                    "Financial loss",
                    "Reputational damage",
                    "Physical harm to individuals",
                    "Emotional or psychological harm",
                    "Loss of confidentiality (especially professional secrecy)",
                    "Unauthorized reversal of pseudonymization",
                    "Significant economic or social disadvantage",
                    "Loss of public trust (societal impact)",
                    "SECURITY RISKS: Unauthorized access to data",
                    "SECURITY RISKS: Modification or corruption of data",
                    "SECURITY RISKS: Loss or deletion of data",
                    "LIKELIHOOD: Assess probability of each risk occurring (remote/possible/probable)",
                    "SEVERITY: Assess potential impact if risk materializes (minimal/significant/severe)",
                    "OVERALL RISK LEVEL: Combine likelihood and severity (low/medium/high)",
                ],
                project_id=project_id,
                phase="Risk Analysis"
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 6: Identify Mitigating Measures",
                description="Develop measures to reduce or eliminate identified risks",
                order=6,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
Mitigation measures are how you reduce risks to acceptable levels. Effective measures demonstrate your commitment to data protection by design and can prevent data breaches and compliance failures.

**What to do:**
For each identified risk, develop practical measures to reduce likelihood or severity.

**How to proceed:**
Consider the 4Ts of risk management (Treat, Transfer, Tolerate, Terminate):
""",
                checklist_items=[
                    "TREAT: Decide not to collect certain types of data",
                    "TREAT: Reduce the scope or scale of processing",
                    "TREAT: Reduce retention periods",
                    "TREAT: Implement additional technological security measures",
                    "TREAT: Anonymize or pseudonymize data where possible",
                    "TREAT: Implement encryption (in transit and at rest)",
                    "TREAT: Strengthen access controls and authentication",
                    "TREAT: Provide comprehensive staff training",
                    "TREAT: Write internal guidance and processes",
                    "TREAT: Implement privacy-enhancing technologies",
                    "TRANSFER: Use different technology or approach",
                    "TRANSFER: Put clear data-sharing agreements in place",
                    "TRANSFER: Ensure processor contracts include appropriate safeguards",
                    "TOLERATE: Accept residual risks within acceptable thresholds",
                    "TOLERATE: Document justification for accepted risks",
                    "TERMINATE: Stop specific processing activities",
                    "TERMINATE: Change process to eliminate high risks",
                    "Make changes to privacy notices for transparency",
                    "Offer individuals opt-out options where appropriate",
                    "Implement systems to facilitate rights exercise",
                    "For each measure: Record whether it reduces, eliminates, or accepts the risk",
                    "For each measure: Consider costs and benefits",
                    "Calculate residual risk level after implementing measures",
                ],
                project_id=project_id,
                phase="Risk Analysis"
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Phase 3: Risk Analysis",
            description="Identify risks and develop mitigation strategies",
            order=3,
            steps=steps
        )

    def _create_phase_4_completion_maintenance(self, project_id: str) -> NEOMPhase:
        """Phase 4: Completion & Maintenance (Steps 7-8)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 7: Sign Off and Record Outcomes",
                description="Document decisions, obtain sign-off, and determine if ICO consultation is needed",
                order=7,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
Sign-off creates accountability and ensures senior management takes ownership of residual risks. If high risks remain, you must consult the ICO before proceeding.

**What to do:**
Document all outcomes, obtain necessary approvals, and determine whether ICO consultation is required.

**How to proceed:**
Complete the DPIA process and document all decisions:
""",
                checklist_items=[
                    "Record additional measures you plan to implement",
                    "For each risk: Document whether eliminated, reduced, or accepted",
                    "Calculate overall level of residual risk after mitigation",
                    "Determine if ICO consultation is required (if high risk remains)",
                    "Seek and document DPO advice on compliance and whether processing can proceed",
                    "If not following DPO advice, record your reasons",
                    "Record reasons for going against views of individuals or consultees (if applicable)",
                    "Obtain sign-off from accountable person for residual risks",
                    "Log residual risks in your organizational Risk Register",
                    "Integrate DPIA outcomes into project plan",
                    "Identify action points and assign responsibility",
                    "Consider publishing DPIA (or summary) for transparency",
                    "If publishing, redact commercially sensitive or security-related details",
                    "If high risk remains that cannot be mitigated: Consult ICO before proceeding",
                ],
                project_id=project_id,
                phase="Completion & Maintenance"
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Step 8: Monitor and Review",
                description="Keep your DPIA under review and update as circumstances change",
                order=8,
                status=StepStatus.NOT_STARTED,
                guidance="""
**Why this matters:**
A DPIA is a living document, not a one-off exercise. Processing activities evolve, new risks emerge, and mitigations need adjustment. Regular review ensures ongoing compliance.

**What to do:**
Establish a process for ongoing monitoring and periodic review of your DPIA.

**How to proceed:**
Create a sustainable monitoring and review process:
""",
                checklist_items=[
                    "Establish monitoring plan with defined frequency (quarterly/annually)",
                    "Define Key Performance Indicators (KPIs) for effectiveness",
                    "KPI: Data breach rates",
                    "KPI: Incident response times",
                    "KPI: Staff training completion rates",
                    "KPI: Subject access request response times",
                    "Schedule regular DPIA reviews (at minimum annually)",
                    "Review when making significant changes to processing",
                    "Review when changing amount of data collected",
                    "Review if external context changes (new security flaws, new technologies)",
                    "Review if new public concerns arise about your processing type",
                    "Review if processing vulnerable groups (new safeguards may be needed)",
                    "Conduct quarterly risk assessments for high-risk activities",
                    "Test incident response plans with regular drills",
                    "Evaluate training effectiveness through completion rates and feedback",
                    "Update DPIA documentation to reflect any changes",
                    "Maintain detailed records of all monitoring and review activities",
                    "Document dates, KPIs, findings, and recommendations",
                    "Ensure DPO monitors ongoing DPIA performance",
                    "Integrate DPIA review into existing project management processes",
                ],
                project_id=project_id,
                phase="Completion & Maintenance"
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Phase 4: Completion & Maintenance",
            description="Finalize DPIA and establish ongoing monitoring",
            order=4,
            steps=steps
        )
