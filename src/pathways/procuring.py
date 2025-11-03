"""Procuring AI pathway - for organizations purchasing AI solutions"""

from typing import List
from src.models import PathwayType, PathwayConfig, RegulatoryFramework
from src.pathways.base import BasePathway


class ProcuringAIPathway(BasePathway):
    """Pathway for organizations procuring AI systems"""

    def get_config(self) -> PathwayConfig:
        """Get pathway configuration"""
        return PathwayConfig(
            pathway_type=PathwayType.PROCURING,
            name="Procuring AI Solutions",
            description="For organizations evaluating and purchasing AI systems from vendors",
            icon="🛒",
            default_steps=[
                "Define Procurement Requirements",
                "Assess Vendor Compliance Claims",
                "Review Risk Classification and Documentation",
                "Evaluate Data Governance Practices",
                "Verify Transparency and Explainability",
                "Assess Security and Privacy Measures",
                "Negotiate Compliance Responsibilities",
                "Plan for Deployment and Monitoring",
            ],
            regulatory_focus=[
                RegulatoryFramework.EU_AI_ACT,
                RegulatoryFramework.SAUDI_AI,
            ],
        )

    def get_default_steps(self) -> List[str]:
        """Get default step titles"""
        return self.get_config().default_steps


class ProcuringAIStepTemplates:
    """Pre-defined templates for procuring AI pathway steps"""

    TEMPLATES = {
        "define_requirements": {
            "title": "Define Procurement Requirements",
            "description": "Establish clear requirements for AI system compliance and capabilities",
            "checklist": [
                "Define business objectives and use cases",
                "Identify regulatory requirements (EU AI Act, Saudi PDPL)",
                "Specify technical and performance requirements",
                "Determine data governance needs",
                "Establish security and privacy requirements",
                "Define integration and compatibility needs",
                "Set budget and timeline constraints",
            ],
            "required_documents": [
                "Requirements Specification",
                "Request for Proposal (RFP)",
            ],
        },
        "vendor_compliance": {
            "title": "Assess Vendor Compliance Claims",
            "description": "Evaluate vendor's compliance documentation and certifications",
            "checklist": [
                "Request compliance documentation from vendors",
                "Verify EU AI Act conformity (CE marking for high-risk systems)",
                "Check for ISO/IEC certifications (27001, 42001)",
                "Review vendor's data protection compliance",
                "Assess vendor's track record and reputation",
                "Verify third-party audits and certifications",
                "Review vendor's incident history",
            ],
            "required_documents": [
                "Vendor Compliance Documentation",
                "Certification Verification",
            ],
        },
        "risk_documentation": {
            "title": "Review Risk Classification and Documentation",
            "description": "Verify the AI system's risk classification and supporting documentation",
            "checklist": [
                "Confirm risk level classification (EU AI Act)",
                "Review risk assessment documentation",
                "Evaluate mitigation strategies for identified risks",
                "Check technical documentation completeness",
                "Verify intended use and limitations documentation",
                "Assess applicability to your use case",
                "Review change management procedures",
            ],
            "required_documents": [
                "Risk Classification Report",
                "Technical Documentation Review",
            ],
        },
        "data_governance": {
            "title": "Evaluate Data Governance Practices",
            "description": "Assess how the vendor manages data throughout the AI lifecycle",
            "checklist": [
                "Review data collection and processing practices",
                "Verify data quality assurance processes",
                "Check bias testing and mitigation measures",
                "Assess data security and encryption",
                "Verify PDPL compliance for Saudi operations",
                "Review data retention and deletion policies",
                "Evaluate cross-border data transfer safeguards",
            ],
            "required_documents": [
                "Data Governance Assessment",
                "Data Processing Agreement",
            ],
        },
        "transparency": {
            "title": "Verify Transparency and Explainability",
            "description": "Ensure the AI system provides adequate transparency and explainability",
            "checklist": [
                "Review system explainability capabilities",
                "Assess user transparency notices",
                "Evaluate decision-making transparency",
                "Check for audit trail and logging features",
                "Verify ability to explain outcomes to stakeholders",
                "Review documentation accessibility",
                "Assess ongoing transparency commitments",
            ],
            "required_documents": [
                "Transparency Assessment",
                "Explainability Documentation",
            ],
        },
        "security_privacy": {
            "title": "Assess Security and Privacy Measures",
            "description": "Evaluate cybersecurity and data privacy protections",
            "checklist": [
                "Review cybersecurity framework and controls",
                "Assess vulnerability management processes",
                "Verify encryption and access controls",
                "Check incident response capabilities",
                "Review privacy-by-design implementation",
                "Assess data breach notification procedures",
                "Verify compliance with NCA requirements (Saudi)",
            ],
            "required_documents": [
                "Security Assessment Report",
                "Privacy Impact Assessment",
            ],
        },
        "negotiate_responsibilities": {
            "title": "Negotiate Compliance Responsibilities",
            "description": "Clearly define compliance responsibilities between your organization and vendor",
            "checklist": [
                "Define deployer vs. provider responsibilities",
                "Negotiate liability and indemnification terms",
                "Establish update and maintenance obligations",
                "Define data ownership and rights",
                "Set performance and SLA requirements",
                "Clarify compliance monitoring responsibilities",
                "Document exit and transition procedures",
            ],
            "required_documents": [
                "Contract with Compliance Terms",
                "Responsibility Matrix (RACI)",
            ],
        },
        "deployment_monitoring": {
            "title": "Plan for Deployment and Monitoring",
            "description": "Prepare for system deployment and ongoing compliance monitoring",
            "checklist": [
                "Develop deployment and integration plan",
                "Establish performance monitoring procedures",
                "Set up compliance monitoring processes",
                "Plan for user training and change management",
                "Define incident escalation procedures",
                "Schedule regular compliance reviews",
                "Plan for updates and patches",
            ],
            "required_documents": [
                "Deployment Plan",
                "Monitoring and Review Schedule",
            ],
        },
    }
