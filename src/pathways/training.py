"""Training on AI pathway - for individuals learning about AI compliance"""

from typing import List
from src.models import PathwayType, PathwayConfig, RegulatoryFramework
from src.pathways.base import BasePathway


class TrainingOnAIPathway(BasePathway):
    """Pathway for individuals seeking to learn about AI compliance"""

    def get_config(self) -> PathwayConfig:
        """Get pathway configuration"""
        return PathwayConfig(
            pathway_type=PathwayType.TRAINING,
            name="AI Compliance Training",
            description="For individuals seeking to understand AI regulations and compliance requirements",
            icon="🎓",
            default_steps=[
                "Understanding AI Regulations Landscape",
                "Learn EU AI Act Fundamentals",
                "Learn Saudi AI Regulations",
                "Risk Classification and Assessment",
                "Data Governance and Privacy",
                "Transparency and Explainability",
                "Ethical AI Principles",
                "Practical Compliance Application",
            ],
            regulatory_focus=[
                RegulatoryFramework.EU_AI_ACT,
                RegulatoryFramework.SAUDI_AI,
            ],
        )

    def get_default_steps(self) -> List[str]:
        """Get default step titles"""
        return self.get_config().default_steps


class TrainingOnAIStepTemplates:
    """Pre-defined templates for training pathway steps"""

    TEMPLATES = {
        "regulations_landscape": {
            "title": "Understanding AI Regulations Landscape",
            "description": "Get an overview of the global and regional AI regulatory environment",
            "checklist": [
                "Learn about major AI regulatory frameworks worldwide",
                "Understand the EU AI Act's global influence",
                "Explore Saudi Arabia's AI strategy and regulations",
                "Study the relationship between AI and existing laws (GDPR, PDPL)",
                "Learn about international AI governance initiatives",
                "Understand industry-specific regulations",
            ],
            "required_documents": [],
            "resources": [
                {
                    "title": "EU AI Act Official Text",
                    "url": "https://artificialintelligenceact.eu/",
                    "type": "regulation",
                },
                {
                    "title": "Saudi Data & AI Authority",
                    "url": "https://sdaia.gov.sa/",
                    "type": "authority",
                },
            ],
        },
        "eu_ai_act_fundamentals": {
            "title": "Learn EU AI Act Fundamentals",
            "description": "Master the core concepts and requirements of the EU AI Act",
            "checklist": [
                "Understand the four risk levels (Unacceptable, High, Limited, Minimal)",
                "Learn about prohibited AI practices",
                "Study high-risk AI system requirements",
                "Understand transparency obligations",
                "Learn about conformity assessment procedures",
                "Explore enforcement and penalties",
                "Study implementation timeline and deadlines",
            ],
            "required_documents": [],
            "resources": [
                {
                    "title": "EU AI Act Risk Classification Guide",
                    "type": "guide",
                },
            ],
        },
        "saudi_ai_regulations": {
            "title": "Learn Saudi AI Regulations",
            "description": "Understand Saudi Arabia's AI regulatory framework and principles",
            "checklist": [
                "Study Saudi national AI principles",
                "Learn about Saudi Personal Data Protection Law (PDPL)",
                "Understand sector-specific requirements",
                "Explore Vision 2030 alignment",
                "Learn about SDAIA's role and authority",
                "Study cybersecurity requirements (NCA)",
                "Understand cultural and ethical considerations",
            ],
            "required_documents": [],
            "resources": [
                {
                    "title": "Saudi PDPL Overview",
                    "type": "regulation",
                },
            ],
        },
        "risk_classification": {
            "title": "Risk Classification and Assessment",
            "description": "Learn how to classify and assess AI system risks",
            "checklist": [
                "Practice classifying AI systems by risk level",
                "Understand risk assessment methodologies",
                "Learn to identify high-risk use cases",
                "Study risk mitigation strategies",
                "Practice conducting impact assessments",
                "Learn about ongoing risk monitoring",
            ],
            "required_documents": [],
        },
        "data_governance_privacy": {
            "title": "Data Governance and Privacy",
            "description": "Master data governance and privacy requirements for AI",
            "checklist": [
                "Learn data quality requirements for AI",
                "Understand bias detection and mitigation",
                "Study data documentation requirements",
                "Learn privacy-by-design principles",
                "Understand consent and data subject rights",
                "Study cross-border data transfer rules",
                "Practice creating data governance frameworks",
            ],
            "required_documents": [],
        },
        "transparency_explainability": {
            "title": "Transparency and Explainability",
            "description": "Learn about transparency and explainability requirements",
            "checklist": [
                "Understand transparency obligations by risk level",
                "Learn explainability techniques and methods",
                "Study user information requirements",
                "Learn about documenting AI decisions",
                "Understand disclosure requirements",
                "Practice creating transparency notices",
            ],
            "required_documents": [],
        },
        "ethical_ai": {
            "title": "Ethical AI Principles",
            "description": "Explore ethical considerations in AI development and deployment",
            "checklist": [
                "Study fairness and non-discrimination principles",
                "Learn about human oversight and autonomy",
                "Understand accountability in AI systems",
                "Explore sustainability and environmental impact",
                "Study social and cultural considerations",
                "Learn about stakeholder engagement",
                "Practice ethical impact assessments",
            ],
            "required_documents": [],
        },
        "practical_application": {
            "title": "Practical Compliance Application",
            "description": "Apply your knowledge to real-world compliance scenarios",
            "checklist": [
                "Work through case studies and examples",
                "Practice creating compliance documentation",
                "Conduct a mock compliance assessment",
                "Develop a compliance roadmap for a sample project",
                "Practice communicating compliance requirements to stakeholders",
                "Create compliance checklists for different scenarios",
                "Plan your ongoing learning and development",
            ],
            "required_documents": [],
        },
    }
