"""Building AI pathway - for teams developing AI systems"""

from typing import List
from src.models import PathwayType, PathwayConfig, RegulatoryFramework
from src.pathways.base import BasePathway


class BuildingAIPathway(BasePathway):
    """Pathway for teams building AI systems"""

    def get_config(self) -> PathwayConfig:
        """Get pathway configuration"""
        return PathwayConfig(
            pathway_type=PathwayType.BUILDING,
            name="Building AI Systems",
            description="For developers and teams creating AI systems from scratch or enhancing existing systems",
            icon="🔨",
            default_steps=[
                "Define AI System Scope and Purpose",
                "Classify Risk Level",
                "Design Data Governance Framework",
                "Implement Risk Management System",
                "Build Transparency and Documentation",
                "Ensure Human Oversight Mechanisms",
                "Test for Accuracy, Robustness, and Security",
                "Prepare for Conformity Assessment",
            ],
            regulatory_focus=[
                RegulatoryFramework.EU_AI_ACT,
                RegulatoryFramework.SAUDI_AI,
            ],
        )

    def get_default_steps(self) -> List[str]:
        """Get default step titles"""
        return self.get_config().default_steps


class BuildingAIStepTemplates:
    """Pre-defined templates for building AI pathway steps"""

    TEMPLATES = {
        "define_scope": {
            "title": "Define AI System Scope and Purpose",
            "description": "Clearly define what your AI system will do, who will use it, and in what contexts",
            "checklist": [
                "Document the intended purpose of the AI system",
                "Identify target users and stakeholders",
                "Define the operational context and environment",
                "Specify technical capabilities and limitations",
                "Determine expected lifespan and update cycle",
            ],
            "required_documents": [
                "System Design Document",
                "Use Case Specifications",
            ],
        },
        "risk_classification": {
            "title": "Classify Risk Level",
            "description": "Determine your AI system's risk classification under EU AI Act and assess compliance requirements",
            "checklist": [
                "Review EU AI Act risk categories",
                "Assess if system falls under prohibited practices",
                "Check if system is in high-risk category",
                "Determine if limited risk (transparency) obligations apply",
                "Document risk classification rationale",
                "Identify applicable Saudi AI requirements",
            ],
            "required_documents": [
                "Risk Classification Assessment",
                "Regulatory Applicability Analysis",
            ],
        },
        "data_governance": {
            "title": "Design Data Governance Framework",
            "description": "Establish processes for managing training, validation, and operational data",
            "checklist": [
                "Define data collection and sourcing procedures",
                "Implement data quality assurance processes",
                "Establish bias detection and mitigation measures",
                "Create data documentation and lineage tracking",
                "Ensure PDPL compliance for Saudi operations",
                "Implement data minimization principles",
                "Set up access controls and security measures",
            ],
            "required_documents": [
                "Data Governance Policy",
                "Data Processing Impact Assessment",
            ],
        },
        "risk_management": {
            "title": "Implement Risk Management System",
            "description": "Develop a comprehensive risk management framework for your AI system",
            "checklist": [
                "Identify known and foreseeable risks",
                "Assess and prioritize risks",
                "Design risk mitigation measures",
                "Implement monitoring and detection mechanisms",
                "Create incident response procedures",
                "Document all risk management activities",
                "Plan for regular risk reassessment",
            ],
            "required_documents": [
                "Risk Management Plan",
                "Risk Register",
                "Mitigation Strategies Document",
            ],
        },
        "transparency": {
            "title": "Build Transparency and Documentation",
            "description": "Create comprehensive technical documentation and user-facing transparency measures",
            "checklist": [
                "Develop technical documentation package",
                "Create user instructions and guidelines",
                "Implement explainability features where needed",
                "Design transparency notices for users",
                "Document training data and methodology",
                "Maintain version control and change logs",
                "Prepare conformity documentation",
            ],
            "required_documents": [
                "Technical Documentation",
                "User Manual",
                "Transparency Notices",
            ],
        },
        "human_oversight": {
            "title": "Ensure Human Oversight Mechanisms",
            "description": "Design and implement meaningful human oversight capabilities",
            "checklist": [
                "Design human-in-the-loop mechanisms",
                "Enable manual override capabilities",
                "Implement stop/pause functionality",
                "Create monitoring dashboards for operators",
                "Develop training materials for human overseers",
                "Define escalation procedures",
                "Test oversight mechanisms effectiveness",
            ],
            "required_documents": [
                "Human Oversight Procedures",
                "Operator Training Materials",
            ],
        },
        "testing_validation": {
            "title": "Test for Accuracy, Robustness, and Security",
            "description": "Conduct comprehensive testing and validation",
            "checklist": [
                "Test system accuracy against benchmarks",
                "Conduct robustness testing (edge cases, adversarial inputs)",
                "Perform security and cybersecurity assessment",
                "Test for bias and fairness across user groups",
                "Validate performance in operational conditions",
                "Document all testing results",
                "Implement continuous monitoring plan",
            ],
            "required_documents": [
                "Testing and Validation Report",
                "Security Assessment",
                "Performance Benchmarks",
            ],
        },
        "conformity_assessment": {
            "title": "Prepare for Conformity Assessment",
            "description": "Get ready for formal conformity assessment (if required for high-risk systems)",
            "checklist": [
                "Determine required conformity assessment procedure",
                "Compile all technical documentation",
                "Prepare EU Declaration of Conformity",
                "Arrange third-party assessment if needed",
                "Plan for CE marking (EU)",
                "Register in EU database if required",
                "Maintain post-market monitoring system",
            ],
            "required_documents": [
                "Conformity Assessment Package",
                "EU Declaration of Conformity",
                "Post-Market Monitoring Plan",
            ],
        },
    }
