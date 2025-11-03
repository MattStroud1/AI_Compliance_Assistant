"""Saudi Arabian AI regulations knowledge base"""

from typing import Dict, List
from enum import Enum


class SaudiAISector(Enum):
    """Key sectors for AI regulation in Saudi Arabia"""

    HEALTHCARE = "healthcare"
    FINANCE = "finance"
    GOVERNMENT = "government"
    EDUCATION = "education"
    TRANSPORTATION = "transportation"
    GENERAL = "general"


class SaudiAIKnowledgeBase:
    """Knowledge base for Saudi Arabian AI regulations and principles"""

    # National AI Principles (based on Saudi Arabia's AI framework)
    NATIONAL_PRINCIPLES = {
        "transparency": {
            "title": "Transparency and Explainability",
            "description": "AI systems should be transparent and their decisions explainable",
            "requirements": [
                "Document AI system objectives and capabilities",
                "Ensure decisions can be explained to users",
                "Provide clear information about AI use",
                "Maintain transparency in data processing",
            ],
        },
        "fairness": {
            "title": "Fairness and Non-Discrimination",
            "description": "AI systems must be fair and avoid discrimination",
            "requirements": [
                "Ensure equal treatment across user groups",
                "Test for bias in algorithms and data",
                "Implement safeguards against discrimination",
                "Monitor for disparate impacts",
            ],
        },
        "privacy": {
            "title": "Privacy and Data Protection",
            "description": "Protect individual privacy and personal data",
            "requirements": [
                "Comply with Saudi Personal Data Protection Law",
                "Implement data minimization principles",
                "Secure data storage and processing",
                "Obtain appropriate consent for data use",
                "Enable data subject rights",
            ],
        },
        "security": {
            "title": "Safety and Security",
            "description": "Ensure AI systems are safe and secure",
            "requirements": [
                "Implement cybersecurity best practices",
                "Conduct security risk assessments",
                "Protect against adversarial attacks",
                "Ensure system reliability and safety",
                "Plan for incident response",
            ],
        },
        "accountability": {
            "title": "Accountability and Governance",
            "description": "Establish clear accountability for AI systems",
            "requirements": [
                "Define roles and responsibilities",
                "Implement governance frameworks",
                "Maintain audit trails",
                "Enable oversight and review",
                "Address liability considerations",
            ],
        },
        "human_oversight": {
            "title": "Human-Centric Design",
            "description": "Keep humans in control of AI systems",
            "requirements": [
                "Design for meaningful human oversight",
                "Enable human intervention when needed",
                "Respect human autonomy",
                "Consider social and cultural context",
            ],
        },
    }

    # Saudi Personal Data Protection Law (PDPL) requirements
    PDPL_REQUIREMENTS = {
        "lawful_processing": {
            "title": "Lawful Data Processing",
            "description": "Process personal data lawfully and fairly",
            "requirements": [
                "Establish legal basis for processing",
                "Process data fairly and transparently",
                "Limit processing to specified purposes",
                "Ensure data accuracy",
            ],
        },
        "consent": {
            "title": "Consent and Rights",
            "description": "Obtain consent and respect data subject rights",
            "requirements": [
                "Obtain clear consent where required",
                "Inform individuals about data processing",
                "Enable right to access personal data",
                "Enable right to correction and deletion",
                "Respect right to data portability",
            ],
        },
        "data_security": {
            "title": "Data Security Measures",
            "description": "Implement appropriate security safeguards",
            "requirements": [
                "Protect data from unauthorized access",
                "Implement encryption where appropriate",
                "Monitor for security breaches",
                "Report breaches to authorities",
            ],
        },
        "cross_border": {
            "title": "Cross-Border Data Transfers",
            "description": "Comply with rules for international data transfers",
            "requirements": [
                "Assess data transfer adequacy",
                "Implement appropriate safeguards",
                "Document transfer mechanisms",
                "Ensure continuous compliance",
            ],
        },
    }

    # Sector-specific requirements
    SECTOR_REQUIREMENTS = {
        SaudiAISector.HEALTHCARE: {
            "name": "Healthcare AI Systems",
            "additional_requirements": [
                "Comply with Ministry of Health regulations",
                "Ensure patient safety and privacy",
                "Validate clinical accuracy and reliability",
                "Maintain medical device compliance if applicable",
                "Protect health information (similar to HIPAA)",
            ],
        },
        SaudiAISector.FINANCE: {
            "name": "Financial AI Systems",
            "additional_requirements": [
                "Comply with SAMA (Saudi Arabian Monetary Authority) regulations",
                "Ensure financial data security",
                "Implement fraud detection safeguards",
                "Maintain audit trails for transactions",
                "Address algorithmic trading requirements",
            ],
        },
        SaudiAISector.GOVERNMENT: {
            "name": "Government AI Systems",
            "additional_requirements": [
                "Align with Vision 2030 objectives",
                "Ensure public service accessibility",
                "Protect citizen data",
                "Maintain transparency in government decisions",
                "Enable citizen recourse mechanisms",
            ],
        },
        SaudiAISector.EDUCATION: {
            "name": "Education AI Systems",
            "additional_requirements": [
                "Comply with Ministry of Education policies",
                "Protect student data and privacy",
                "Ensure educational equity and fairness",
                "Validate pedagogical effectiveness",
                "Align with national curriculum standards",
            ],
        },
        SaudiAISector.TRANSPORTATION: {
            "name": "Transportation AI Systems",
            "additional_requirements": [
                "Comply with transportation authority regulations",
                "Ensure public safety",
                "Meet technical safety standards",
                "Implement incident reporting",
                "Address liability frameworks",
            ],
        },
        SaudiAISector.GENERAL: {
            "name": "General AI Systems",
            "additional_requirements": [
                "Follow national AI principles",
                "Comply with PDPL requirements",
                "Adhere to ethical AI guidelines",
            ],
        },
    }

    # Vision 2030 alignment
    VISION_2030_CONSIDERATIONS = [
        "Support digital transformation objectives",
        "Enhance government service delivery",
        "Promote innovation and entrepreneurship",
        "Develop local AI talent and capabilities",
        "Align with national economic diversification goals",
        "Consider social and cultural values",
    ]

    @classmethod
    def get_applicable_requirements(
        cls, sector: SaudiAISector, involves_personal_data: bool = True
    ) -> Dict[str, List]:
        """
        Get applicable requirements based on sector and data usage

        Args:
            sector: AI system sector
            involves_personal_data: Whether system processes personal data

        Returns:
            Dictionary of applicable requirements
        """
        requirements = {
            "national_principles": list(cls.NATIONAL_PRINCIPLES.values()),
            "sector_specific": cls.SECTOR_REQUIREMENTS.get(
                sector, cls.SECTOR_REQUIREMENTS[SaudiAISector.GENERAL]
            ),
        }

        if involves_personal_data:
            requirements["pdpl"] = list(cls.PDPL_REQUIREMENTS.values())

        requirements["vision_2030"] = cls.VISION_2030_CONSIDERATIONS

        return requirements

    @classmethod
    def classify_sector(cls, system_description: str, use_case: str) -> SaudiAISector:
        """
        Classify AI system sector based on description

        Args:
            system_description: System description
            use_case: Intended use case

        Returns:
            Applicable sector
        """
        text = (system_description + " " + use_case).lower()

        sector_keywords = {
            SaudiAISector.HEALTHCARE: [
                "health",
                "medical",
                "patient",
                "diagnosis",
                "treatment",
                "clinical",
            ],
            SaudiAISector.FINANCE: [
                "financial",
                "banking",
                "payment",
                "credit",
                "trading",
                "insurance",
            ],
            SaudiAISector.GOVERNMENT: [
                "government",
                "public service",
                "citizen",
                "municipal",
                "administrative",
            ],
            SaudiAISector.EDUCATION: [
                "education",
                "learning",
                "student",
                "teaching",
                "training",
                "academic",
            ],
            SaudiAISector.TRANSPORTATION: [
                "transport",
                "vehicle",
                "traffic",
                "autonomous",
                "mobility",
                "logistics",
            ],
        }

        for sector, keywords in sector_keywords.items():
            if any(keyword in text for keyword in keywords):
                return sector

        return SaudiAISector.GENERAL

    @classmethod
    def get_regulatory_bodies(cls) -> Dict[str, str]:
        """Get relevant Saudi regulatory bodies"""

        return {
            "SDAIA": "Saudi Data and AI Authority - Primary AI regulator",
            "SAMA": "Saudi Arabian Monetary Authority - Financial sector",
            "MOH": "Ministry of Health - Healthcare sector",
            "MOE": "Ministry of Education - Education sector",
            "CITC": "Communications and Information Technology Commission - ICT sector",
            "NCA": "National Cybersecurity Authority - Cybersecurity",
        }

    @classmethod
    def get_compliance_checklist(cls) -> List[Dict[str, str]]:
        """Get general compliance checklist for Saudi AI regulations"""

        return [
            {
                "item": "Data Protection Compliance",
                "description": "Ensure compliance with Saudi PDPL",
                "action": "Review and implement PDPL requirements",
            },
            {
                "item": "National Principles Alignment",
                "description": "Align with Saudi AI principles",
                "action": "Map system to each national principle",
            },
            {
                "item": "Sector Regulations",
                "description": "Identify sector-specific requirements",
                "action": "Consult relevant regulatory authority",
            },
            {
                "item": "Cybersecurity",
                "description": "Implement Essential Cybersecurity Controls (ECC)",
                "action": "Follow NCA cybersecurity framework",
            },
            {
                "item": "Cultural Considerations",
                "description": "Respect local cultural and social values",
                "action": "Review content and conduct cultural assessment",
            },
            {
                "item": "Documentation",
                "description": "Maintain comprehensive documentation",
                "action": "Document system design, data, and governance",
            },
            {
                "item": "Governance Framework",
                "description": "Establish AI governance structure",
                "action": "Define roles, responsibilities, and oversight",
            },
        ]
