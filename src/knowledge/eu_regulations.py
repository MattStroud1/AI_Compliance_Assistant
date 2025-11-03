"""EU AI Act knowledge base"""

from typing import Dict, List, Optional
from enum import Enum


class EURiskLevel(Enum):
    """EU AI Act risk levels"""

    UNACCEPTABLE = "unacceptable"
    HIGH = "high"
    LIMITED = "limited"
    MINIMAL = "minimal"


class EUAIActKnowledgeBase:
    """Knowledge base for EU AI Act requirements"""

    # Prohibited AI practices (Unacceptable Risk)
    PROHIBITED_PRACTICES = [
        "Subliminal manipulation causing harm",
        "Social scoring by governments",
        "Real-time biometric identification in public spaces (with exceptions)",
        "Exploitation of vulnerabilities of specific groups",
    ]

    # High-risk AI systems categories
    HIGH_RISK_CATEGORIES = {
        "biometric_identification": {
            "name": "Biometric Identification and Categorization",
            "examples": ["Remote biometric identification", "Emotion recognition systems"],
            "requirements": [
                "Conformity assessment required",
                "Fundamental rights impact assessment",
                "Registration in EU database",
            ],
        },
        "critical_infrastructure": {
            "name": "Critical Infrastructure",
            "examples": ["Traffic and water supply management systems"],
            "requirements": [
                "Risk management system",
                "Data governance measures",
                "Technical documentation",
            ],
        },
        "education_employment": {
            "name": "Education and Employment",
            "examples": [
                "Recruitment systems",
                "Educational assessment tools",
                "Promotion decision systems",
            ],
            "requirements": [
                "Human oversight mechanisms",
                "Transparency obligations",
                "Accuracy and robustness requirements",
            ],
        },
        "essential_services": {
            "name": "Essential Services",
            "examples": [
                "Credit scoring systems",
                "Emergency service dispatch",
                "Benefit eligibility assessment",
            ],
            "requirements": [
                "Risk management procedures",
                "Record-keeping obligations",
                "Conformity assessment",
            ],
        },
        "law_enforcement": {
            "name": "Law Enforcement",
            "examples": [
                "Crime risk assessment",
                "Lie detection systems",
                "Evidence evaluation tools",
            ],
            "requirements": [
                "Strict fundamental rights safeguards",
                "Judicial oversight",
                "Data quality requirements",
            ],
        },
        "migration_border": {
            "name": "Migration and Border Control",
            "examples": [
                "Visa application assessment",
                "Border control systems",
                "Asylum decision support",
            ],
            "requirements": [
                "Fundamental rights impact assessment",
                "Data protection compliance",
                "Human review requirement",
            ],
        },
        "justice": {
            "name": "Administration of Justice",
            "examples": ["Legal research tools", "Case outcome prediction"],
            "requirements": [
                "Transparency about AI use",
                "Human oversight",
                "Documentation requirements",
            ],
        },
    }

    # Requirements for high-risk systems
    HIGH_RISK_REQUIREMENTS = {
        "risk_management": {
            "title": "Risk Management System",
            "description": "Establish and maintain a risk management system",
            "actions": [
                "Identify known and foreseeable risks",
                "Estimate and evaluate risks",
                "Adopt appropriate risk management measures",
                "Test and validate the system",
                "Document all risk management activities",
            ],
        },
        "data_governance": {
            "title": "Data and Data Governance",
            "description": "Ensure high-quality training, validation, and testing data",
            "actions": [
                "Implement data governance practices",
                "Ensure data is relevant and representative",
                "Check data for bias and errors",
                "Document data sourcing and processing",
                "Maintain appropriate data quality throughout lifecycle",
            ],
        },
        "technical_documentation": {
            "title": "Technical Documentation",
            "description": "Create comprehensive technical documentation",
            "actions": [
                "Document system design and development",
                "Describe intended purpose and limitations",
                "Detail risk management measures",
                "Document data governance procedures",
                "Include validation and testing results",
                "Maintain documentation up to date",
            ],
        },
        "record_keeping": {
            "title": "Record-Keeping",
            "description": "Maintain automatic recording of events (logs)",
            "actions": [
                "Implement automatic logging functionality",
                "Record system operations and decisions",
                "Ensure logs enable traceability",
                "Protect log integrity",
                "Retain logs for appropriate duration",
            ],
        },
        "transparency": {
            "title": "Transparency and User Information",
            "description": "Provide clear information to users",
            "actions": [
                "Design transparent and interpretable systems",
                "Provide clear user instructions",
                "Explain system capabilities and limitations",
                "Inform about human oversight",
                "Disclose AI system use where appropriate",
            ],
        },
        "human_oversight": {
            "title": "Human Oversight",
            "description": "Enable effective human oversight",
            "actions": [
                "Design for human intervention capability",
                "Enable system deactivation when needed",
                "Ensure humans can override decisions",
                "Provide oversight training",
                "Prevent automation bias",
            ],
        },
        "accuracy_robustness": {
            "title": "Accuracy, Robustness and Cybersecurity",
            "description": "Ensure system resilience and security",
            "actions": [
                "Achieve appropriate accuracy levels",
                "Ensure robustness against errors",
                "Implement cybersecurity measures",
                "Test against adversarial inputs",
                "Maintain security throughout lifecycle",
            ],
        },
        "conformity_assessment": {
            "title": "Conformity Assessment",
            "description": "Undergo conformity assessment before market placement",
            "actions": [
                "Choose appropriate conformity assessment procedure",
                "Conduct internal control or third-party assessment",
                "Prepare EU declaration of conformity",
                "Affix CE marking",
                "Register in EU database",
            ],
        },
    }

    # Limited risk systems (transparency obligations)
    LIMITED_RISK_OBLIGATIONS = {
        "chatbots": "Users must be informed they are interacting with an AI system",
        "deepfakes": "Synthetic content must be clearly labeled",
        "emotion_recognition": "Users must be informed when emotion recognition is used",
        "biometric_categorization": "Users must be informed about biometric categorization",
    }

    @classmethod
    def classify_risk_level(
        cls, system_description: str, use_case: str
    ) -> Dict[str, any]:
        """
        Classify AI system risk level based on description and use case

        Args:
            system_description: Description of the AI system
            use_case: Intended use case

        Returns:
            Dictionary with risk level and relevant requirements
        """
        # Simple keyword-based classification
        # In production, this would use more sophisticated analysis

        description_lower = system_description.lower()
        use_case_lower = use_case.lower()

        # Check for prohibited practices
        for practice in cls.PROHIBITED_PRACTICES:
            if any(
                keyword in description_lower
                for keyword in practice.lower().split()[:3]
            ):
                return {
                    "risk_level": EURiskLevel.UNACCEPTABLE,
                    "reason": f"Likely involves prohibited practice: {practice}",
                    "action_required": "System not permitted under EU AI Act",
                }

        # Check for high-risk categories
        for category_id, category in cls.HIGH_RISK_CATEGORIES.items():
            category_keywords = category["name"].lower().split()
            if any(keyword in use_case_lower for keyword in category_keywords):
                return {
                    "risk_level": EURiskLevel.HIGH,
                    "category": category["name"],
                    "requirements": cls.HIGH_RISK_REQUIREMENTS,
                    "action_required": "Full compliance requirements apply",
                }

        # Check for limited risk (transparency obligations)
        limited_risk_keywords = ["chatbot", "deepfake", "emotion", "biometric"]
        if any(keyword in description_lower for keyword in limited_risk_keywords):
            return {
                "risk_level": EURiskLevel.LIMITED,
                "obligations": cls.LIMITED_RISK_OBLIGATIONS,
                "action_required": "Transparency obligations apply",
            }

        # Default to minimal risk
        return {
            "risk_level": EURiskLevel.MINIMAL,
            "action_required": "Voluntary codes of conduct encouraged",
        }

    @classmethod
    def get_requirements_for_risk_level(cls, risk_level: EURiskLevel) -> List[Dict]:
        """Get compliance requirements for a specific risk level"""

        if risk_level == EURiskLevel.UNACCEPTABLE:
            return [
                {
                    "requirement": "System Prohibition",
                    "description": "This AI system is prohibited under the EU AI Act",
                    "action": "Do not develop, deploy, or use this system",
                }
            ]

        elif risk_level == EURiskLevel.HIGH:
            return list(cls.HIGH_RISK_REQUIREMENTS.values())

        elif risk_level == EURiskLevel.LIMITED:
            return [
                {
                    "requirement": "Transparency Obligation",
                    "description": "Users must be informed about AI system use",
                    "action": "Implement clear disclosure mechanisms",
                }
            ]

        else:  # MINIMAL
            return [
                {
                    "requirement": "Voluntary Measures",
                    "description": "Consider adopting voluntary codes of conduct",
                    "action": "Follow best practices for trustworthy AI",
                }
            ]

    @classmethod
    def get_timeline_and_deadlines(cls) -> Dict[str, str]:
        """Get key EU AI Act implementation timeline"""

        return {
            "2024_Q3": "EU AI Act enters into force",
            "2025_Q1": "Prohibited practices ban takes effect",
            "2026_Q3": "General purpose AI model rules apply",
            "2027_Q3": "High-risk system requirements fully applicable",
            "ongoing": "Member state authorities establish enforcement",
        }
