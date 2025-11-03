"""NEOM Trustworthy AI - Building pathway with 4 lifecycle phases"""

from typing import List, Dict
from src.models import (
    PathwayType, PathwayConfig, RegulatoryFramework,
    PhaseType, NEOMPhase, ComplianceStep, StepStatus,
    TaskReference, EvidenceType
)
from src.pathways.base import BasePathway
import uuid


class NEOMBuildingAIPathway(BasePathway):
    """NEOM-compliant pathway for building AI systems with full lifecycle management"""

    def get_config(self) -> PathwayConfig:
        """Get pathway configuration"""
        return PathwayConfig(
            pathway_type=PathwayType.BUILDING,
            name="Building AI (NEOM Trustworthy AI)",
            description="Complete NEOM-compliant AI development lifecycle with evidence collection, RACI management, and pitstop checkpoints",
            icon="🏗️",
            default_steps=[],  # Steps are organized by phase
            regulatory_focus=[RegulatoryFramework.BOTH],
        )

    def get_default_steps(self) -> List[str]:
        """Get default step titles (not used for NEOM pathway)"""
        return []

    def create_phases(self, project_id: str) -> List[NEOMPhase]:
        """
        Create all 4 phases with their specific steps

        Returns:
            List of NEOMPhase objects
        """
        return [
            self._create_phase_1_planning_design(project_id),
            self._create_phase_2_data_preparation(project_id),
            self._create_phase_3_build_validate(project_id),
            self._create_phase_4_deployment_monitoring(project_id),
        ]

    # ========================================================================
    # PHASE 1: PLANNING & DESIGN
    # ========================================================================

    def _create_phase_1_planning_design(self, project_id: str) -> NEOMPhase:
        """Create Phase 1: Planning & Design"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Establish Governance & RACI",
                description="Define roles, responsibilities, and governance structure for the AI project",
                order=1,
                checklist_items=[
                    "Create RACI matrix with clear roles (Responsible, Accountable, Consulted, Informed)",
                    "Define Data Owner, Data Steward, and Data Custodian roles",
                    "Identify project lead and PDPO contact",
                    "Establish decision-making authority and escalation paths",
                    "Get buy-in from all named stakeholders",
                    "Document data governance framework",
                ],
                required_documents=[
                    "RACI Matrix",
                    "Data Governance Framework",
                ],
                resources=[
                    {
                        "title": "RACI Template",
                        "type": "template",
                        "description": "Available in Trustworthy AI Toolbox"
                    }
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Define AI System Scope & Purpose",
                description="Document what your AI system will do, who will use it, and in what contexts",
                order=2,
                checklist_items=[
                    "Document the AI system's name and intended purpose",
                    "Identify target users and stakeholders",
                    "Define operational context and environment",
                    "Specify technical capabilities and limitations",
                    "Determine expected lifespan and update cycle",
                    "Identify if system will affect children or vulnerable groups",
                    "Determine deployment languages and geographies",
                ],
                required_documents=[
                    "System Design Document",
                    "Use Case Specifications",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Determine Legal Basis & Sensitive Data",
                description="Identify data requirements, sensitive data, and establish legal basis for processing",
                order=3,
                checklist_items=[
                    "List all personal data required (minimize scope)",
                    "Identify sensitive data (ethnic origin, health data, biometric, financial, etc.)",
                    "Check if data includes children's data (under 13 for PDPL, under 16 for GDPR)",
                    "Determine legal basis: Legitimate Interest, Contract, or Consent",
                    "Complete Legitimate Interest Assessment (LIA) if applicable",
                    "Design consent capture mechanisms if needed",
                    "Document logic for legal basis selection",
                ],
                required_documents=[
                    "Data Inventory",
                    "Legal Basis Assessment",
                    "Legitimate Interest Assessment (if applicable)",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Privacy Impact Assessment (PIA)",
                description="Assess privacy risks and document mitigation measures",
                order=4,
                checklist_items=[
                    "Assess if processing is 'high-risk' using ICO criteria",
                    "Document description of intended data processing",
                    "Assess risks to privacy, rights, and freedoms of individuals",
                    "Document privacy-by-design measures (transparency, minimization, PETs)",
                    "Define safeguards and security measures",
                    "Justify processing considering data subjects' rights",
                    "Get PDPO review and sign-off",
                ],
                required_documents=[
                    "Privacy Impact Assessment",
                    "PDPO Sign-off",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Security Risk Analysis",
                description="Identify AI-specific security threats and plan countermeasures",
                order=5,
                checklist_items=[
                    "Assess risk of training data leaks",
                    "Assess risk of model theft",
                    "Assess risk of supply chain poisoning",
                    "Assess risk of training data poisoning",
                    "Assess risk of evasion/adversarial attacks",
                    "Assess risk of model inversion attacks",
                    "Assess risk of membership inference attacks",
                    "Document countermeasures for each identified risk",
                    "Get CISO review and approval",
                ],
                required_documents=[
                    "Security Risk Assessment",
                    "Security Countermeasures Plan",
                    "CISO Sign-off",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Risk & Fairness Analysis",
                description="Identify risks to human rights, fairness, and plan mitigation measures",
                order=6,
                checklist_items=[
                    "Analyze impact on human rights and cultural values",
                    "Assess social and environmental impacts",
                    "Identify foreseeable errors and misuse scenarios",
                    "Assess risk of biased feedback loops",
                    "Define fairness metrics and thresholds (80% rule or sector-specific)",
                    "Plan mitigation measures (design, process, training, oversight)",
                    "Document residual risks and justification",
                ],
                required_documents=[
                    "Risk & Fairness Assessment",
                    "Fairness Metrics Definition",
                    "Mitigation Plan",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Explainability Planning",
                description="Plan how the AI system's decisions will be explained to users",
                order=7,
                checklist_items=[
                    "Select explainability approach (LIME, SHAP, visualization, etc.)",
                    "Define what needs to be explained (internal logic + specific decisions)",
                    "Design user communication channels (manuals, UI text, pop-ups)",
                    "Plan logging and audit trail retention (typically 7 years)",
                    "Design process for users to request explanations",
                    "Plan validation of explainability effectiveness",
                ],
                required_documents=[
                    "Explainability Strategy",
                    "User Communication Design",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Technology Development Record - Planning",
                description="Document high-level design and validation methodology",
                order=8,
                checklist_items=[
                    "Describe proposed AI system design (attach design documents)",
                    "Define required levels of accuracy, reliability, and security",
                    "Justify why design will achieve objectives",
                    "Define validation methodology for accuracy/reliability/security",
                    "Design logging and record-keeping processes",
                    "Document what events generate logs and retention periods",
                    "Get required sign-offs per RACI",
                ],
                required_documents=[
                    "Technology Development Record - Part 1",
                    "Validation Methodology",
                    "Logging Design",
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,
            name="Phase 1: Planning & Design",
            description="Establish governance, assess risks, and plan compliance approach",
            order=1,
            steps=steps
        )

    # ========================================================================
    # PHASE 2: DATA PREPARATION
    # ========================================================================

    def _create_phase_2_data_preparation(self, project_id: str) -> NEOMPhase:
        """Create Phase 2: Data Preparation"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Data Cards & Residency",
                description="Document all datasets with data cards and ensure data residency compliance",
                order=1,
                checklist_items=[
                    "Create data card for each dataset",
                    "Document: origin, structure, labels, completeness, creation date",
                    "Document data accuracy determination",
                    "Document why data is relevant to the AI purpose",
                    "Check for data processors transferring data outside KSA",
                    "Consult CISO if cross-border transfer detected",
                    "Version and archive data cards",
                ],
                required_documents=[
                    "Data Cards (all datasets)",
                    "Data Residency Assessment",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Identify & Mitigate Biases",
                description="Explore datasets for biases and proxies for sensitive attributes",
                order=2,
                checklist_items=[
                    "Identify proxies for sensitive data attributes",
                    "Remove sensitive data and proxies where possible",
                    "Document justification if sensitive data/proxies must be retained",
                    "Check for measurement bias, sampling bias, survivorship bias",
                    "Check for recency bias, data processing bias, algorithmic bias",
                    "Check for cultural bias, exclusion bias, confirmation bias",
                    "Document all identified biases and mitigation steps",
                ],
                required_documents=[
                    "Bias Analysis Report",
                    "Bias Mitigation Documentation",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Apply Privacy Enhancing Technologies (PETs)",
                description="Evaluate and implement PETs to protect privacy while enabling insights",
                order=3,
                checklist_items=[
                    "Evaluate synthetic data generation",
                    "Evaluate differential privacy techniques",
                    "Evaluate homomorphic encryption",
                    "Evaluate secure multi-party computation",
                    "Evaluate private set intersection",
                    "Evaluate federated learning",
                    "Document which PETs are suitable for your project",
                    "Document implementation or justification for not using PETs",
                ],
                required_documents=[
                    "PETs Analysis",
                    "PETs Implementation Plan (if applicable)",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Data Quality Validation",
                description="Ensure data is fit for purpose and representative",
                order=4,
                checklist_items=[
                    "Verify data credibility and source quality",
                    "Assess data accuracy, consistency, completeness, timeliness",
                    "Ensure data represents real-world diversity",
                    "Confirm sample size is adequate (use statistical power analysis)",
                    "Clean data and handle missing values",
                    "Document all data processing decisions",
                    "Update PIA with new facts from data preparation",
                ],
                required_documents=[
                    "Data Quality Report",
                    "Updated PIA",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Technology Development Record - Data",
                description="Document data range, outliers, and backup procedures",
                order=5,
                checklist_items=[
                    "Define range of input data the model will encounter",
                    "Identify foreseeable outlier data",
                    "Ensure training/validation datasets cover expected range and outliers",
                    "Design and implement data backup procedures",
                    "Document backup schedule and governance",
                    "Get required sign-offs per RACI",
                ],
                required_documents=[
                    "Technology Development Record - Part 2",
                    "Data Backup Procedures",
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Phase 2: Data Preparation",
            description="Prepare, clean, and validate data with privacy and fairness safeguards",
            order=2,
            steps=steps
        )

    # ========================================================================
    # PHASE 3: BUILD & VALIDATE
    # ========================================================================

    def _create_phase_3_build_validate(self, project_id: str) -> NEOMPhase:
        """Create Phase 3: Build & Validate"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Model Training & Documentation",
                description="Build AI model and document every step for reproducibility",
                order=1,
                checklist_items=[
                    "Divide data into training and validation datasets",
                    "Ensure datasets are representative of each other",
                    "Create and archive data cards for each dataset",
                    "Document: datasets used, partitioning method, hardware/software",
                    "Document: hyperparameters for each iteration",
                    "Record sufficient detail for expert reproduction",
                ],
                required_documents=[
                    "Model Training Log",
                    "Dataset Data Cards",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Feature Selection (Bias Check)",
                description="Select features while checking for bias introduction",
                order=2,
                checklist_items=[
                    "Review features for proxies to sensitive attributes",
                    "Ensure no important variables excluded (could cause skew)",
                    "Check for spurious correlations",
                    "Validate feature selection doesn't favor majority groups",
                    "Document feature selection logic and bias checks",
                ],
                required_documents=[
                    "Feature Selection Report",
                    "Bias Check Results",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Champion Model Selection",
                description="Select final model while ensuring fairness across all groups",
                order=3,
                checklist_items=[
                    "Evaluate models on diverse scenarios and populations",
                    "Check performance on minority groups (not just aggregate)",
                    "Ensure model doesn't overfit to training data",
                    "Test generalization to varied real-world contexts",
                    "Document champion model selection rationale",
                    "Verify no new biases introduced",
                ],
                required_documents=[
                    "Champion Model Selection Report",
                    "Generalization Testing Results",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Fairness Metrics Validation",
                description="Test model against defined fairness metrics and thresholds",
                order=4,
                checklist_items=[
                    "Run model on validation data",
                    "Calculate all defined fairness metrics",
                    "Verify all metrics are within thresholds",
                    "Document any threshold violations",
                    "If violations found, retrain or adjust model",
                    "Assess contextual outcomes for vulnerable groups",
                ],
                required_documents=[
                    "Fairness Metrics Results",
                    "Threshold Compliance Report",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Security Validation",
                description="Test security countermeasures and validate system resilience",
                order=5,
                checklist_items=[
                    "Test adversarial training effectiveness",
                    "Test input validation mechanisms",
                    "Test model inversion resistance",
                    "Test membership inference resistance",
                    "Document validation approach and criteria",
                    "Document test inputs and outcomes",
                    "Assess if results acceptable for deployment context",
                ],
                required_documents=[
                    "Security Validation Report",
                    "Penetration Test Results",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Explainability Implementation",
                description="Implement and validate explainability features",
                order=6,
                checklist_items=[
                    "Implement selected explainability techniques",
                    "Create user-facing explanation interfaces",
                    "Design process for users to request explanations",
                    "Validate explanations with test users",
                    "Ensure explanations are comprehensible to target audience",
                    "Document explainability implementation",
                ],
                required_documents=[
                    "Explainability Implementation Report",
                    "User Testing Results",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Integrated System Testing",
                description="Test complete AI system in intended deployment context",
                order=7,
                checklist_items=[
                    "Test if model functions as intended in context",
                    "Test usage guardrails and restrictions",
                    "Test user communication channels",
                    "Test robustness to input errors (if high-risk system)",
                    "Validate human oversight mechanisms work",
                    "Document system limitations",
                    "Define restricted or unsupported use cases",
                ],
                required_documents=[
                    "Integrated Testing Report",
                    "Known Limitations Document",
                    "Restricted Use Cases",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Technology Development Record - Build & Validate",
                description="Complete build & validate section of Technology Development Record",
                order=8,
                checklist_items=[
                    "Document validation methodology execution",
                    "Store and index key decisions and data",
                    "Document training datasets, prompts, and outcomes",
                    "Demonstrate accuracy, reliability, and security",
                    "Document known limitations",
                    "Get required sign-offs per RACI",
                ],
                required_documents=[
                    "Technology Development Record - Part 3",
                    "Validation Results Package",
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Phase 3: Build & Validate",
            description="Train, validate, and test the AI system for compliance and performance",
            order=3,
            steps=steps
        )

    # ========================================================================
    # PHASE 4: DEPLOYMENT & MONITORING
    # ========================================================================

    def _create_phase_4_deployment_monitoring(self, project_id: str) -> NEOMPhase:
        """Create Phase 4: Deployment & Monitoring"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Deployment Preparation",
                description="Prepare data flows, privacy notices, and deployment documentation",
                order=1,
                checklist_items=[
                    "Create data flow map for the service",
                    "Prepare Record of Data Processing (ROPA)",
                    "Create Privacy Notice for users",
                    "Prepare user instructions and manuals",
                    "Create integration guide for deployers",
                    "Document external system interactions",
                ],
                required_documents=[
                    "Data Flow Map",
                    "ROPA",
                    "Privacy Notice",
                    "User Manual",
                    "Integration Guide",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Post-Market Monitoring Setup",
                description="Establish continuous monitoring for fairness, security, and resource usage",
                order=2,
                checklist_items=[
                    "Set up fairness metrics monitoring",
                    "Set up security metrics monitoring",
                    "Set up resource usage monitoring (environmental impact)",
                    "Define monitoring frequency and thresholds",
                    "Create monitoring dashboards",
                    "Establish alert procedures for threshold violations",
                    "Define periodic assessment schedule",
                ],
                required_documents=[
                    "Post-Market Monitoring Plan",
                    "Monitoring Dashboard Access",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="User Interface Validation",
                description="Validate user interfaces for explanations and disclosures",
                order=3,
                checklist_items=[
                    "Test explainability interfaces with real users",
                    "Validate transparency disclosures (deepfakes, emotion recognition, etc.)",
                    "Test complaints process accessibility",
                    "Validate residual risk communication",
                    "Ensure all required disclosures are present and clear",
                    "Document validation results",
                ],
                required_documents=[
                    "UI Validation Report",
                    "User Testing Results",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Continuous Monitoring Execution",
                description="Execute ongoing monitoring and periodic assessments",
                order=4,
                checklist_items=[
                    "Monitor fairness metrics against thresholds",
                    "Monitor security for AI-specific attacks",
                    "Monitor and report resource usage (CO2 emissions)",
                    "Conduct periodic AI Impact Assessments",
                    "Conduct periodic Privacy Impact Assessments",
                    "Conduct periodic Security Assessments",
                    "Document all monitoring results and sign-offs",
                ],
                required_documents=[
                    "Monitoring Logs",
                    "Periodic Assessment Reports",
                    "PDPO Sign-offs",
                ]
            ),

            ComplianceStep(
                id=str(uuid.uuid4()),
                title="Technology Development Record - Operations",
                description="Maintain operational section of Technology Development Record",
                order=5,
                checklist_items=[
                    "Keep record current with operational context",
                    "Document any changes to the system",
                    "Update responsible parties and contact information",
                    "Document system version and deployment date",
                    "Maintain list of standards followed",
                    "Update integration diagrams if system changes",
                ],
                required_documents=[
                    "Technology Development Record - Part 4",
                    "Change Log",
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Phase 4: Deployment & Monitoring",
            description="Deploy system and maintain continuous compliance monitoring",
            order=4,
            steps=steps
        )


# Task references mapped to playbook sections (for reference/traceability)
PLAYBOOK_TASK_REFERENCES = {
    "2.1": TaskReference(
        task_id="2.1",
        section="Data & Privacy, Security, Risk & Fairness, Explainability",
        description="Establish RACI with appropriate roles and sign-offs",
        phase=PhaseType.PLANNING_DESIGN,
        mandatory=True,
        evidence_required=[EvidenceType.DOCUMENT, EvidenceType.SIGN_OFF]
    ),
    "3.1": TaskReference(
        task_id="3.1",
        section="Data & Privacy",
        description="Identify if data includes sensitive data or children's data",
        phase=PhaseType.PLANNING_DESIGN,
        mandatory=True,
        evidence_required=[EvidenceType.ASSESSMENT]
    ),
    # ... (many more task references would be mapped here)
}
