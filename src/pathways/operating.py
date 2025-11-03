"""Operating AI pathway - for teams deploying and managing AI systems"""

from typing import List
from src.models import PathwayType, PathwayConfig, RegulatoryFramework
from src.pathways.base import BasePathway


class OperatingAIPathway(BasePathway):
    """Pathway for teams operating AI systems in production"""

    def get_config(self) -> PathwayConfig:
        """Get pathway configuration"""
        return PathwayConfig(
            pathway_type=PathwayType.OPERATING,
            name="Operating AI Systems",
            description="For teams deploying, running, and maintaining AI systems in production environments",
            icon="⚙️",
            default_steps=[
                "Establish Operational Governance",
                "Implement Monitoring and Logging",
                "Ensure Human Oversight in Operations",
                "Monitor Performance and Accuracy",
                "Manage Incidents and Issues",
                "Maintain Documentation and Records",
                "Conduct Regular Compliance Audits",
                "Plan for Updates and Changes",
            ],
            regulatory_focus=[
                RegulatoryFramework.EU_AI_ACT,
                RegulatoryFramework.SAUDI_AI,
            ],
        )

    def get_default_steps(self) -> List[str]:
        """Get default step titles"""
        return self.get_config().default_steps


class OperatingAIStepTemplates:
    """Pre-defined templates for operating AI pathway steps"""

    TEMPLATES = {
        "operational_governance": {
            "title": "Establish Operational Governance",
            "description": "Set up governance structures and processes for AI operations",
            "checklist": [
                "Define roles and responsibilities for AI operations",
                "Establish decision-making authority and escalation paths",
                "Create operational policies and procedures",
                "Set up compliance oversight mechanisms",
                "Define KPIs and success metrics",
                "Establish stakeholder communication plan",
                "Document governance framework",
            ],
            "required_documents": [
                "Operational Governance Framework",
                "Roles and Responsibilities Matrix",
            ],
        },
        "monitoring_logging": {
            "title": "Implement Monitoring and Logging",
            "description": "Deploy comprehensive monitoring and logging systems",
            "checklist": [
                "Implement real-time system monitoring",
                "Set up automated logging of decisions and operations",
                "Create dashboards for operational visibility",
                "Configure alerting for anomalies and issues",
                "Ensure log retention meets regulatory requirements",
                "Protect log integrity and security",
                "Enable traceability of AI decisions",
            ],
            "required_documents": [
                "Monitoring and Logging Plan",
                "Log Retention Policy",
            ],
        },
        "human_oversight_ops": {
            "title": "Ensure Human Oversight in Operations",
            "description": "Maintain effective human oversight during AI system operation",
            "checklist": [
                "Train operators on oversight responsibilities",
                "Implement human-in-the-loop workflows where required",
                "Enable easy override and intervention mechanisms",
                "Monitor for automation bias among operators",
                "Conduct regular oversight effectiveness reviews",
                "Document oversight activities and interventions",
                "Update oversight procedures based on learnings",
            ],
            "required_documents": [
                "Human Oversight Procedures",
                "Operator Training Records",
            ],
        },
        "performance_monitoring": {
            "title": "Monitor Performance and Accuracy",
            "description": "Continuously track AI system performance and accuracy",
            "checklist": [
                "Track accuracy metrics against baselines",
                "Monitor for model drift and degradation",
                "Test for bias in production decisions",
                "Analyze error rates and patterns",
                "Compare performance across different user groups",
                "Investigate unexpected behaviors",
                "Trigger retraining or adjustments when needed",
            ],
            "required_documents": [
                "Performance Monitoring Reports",
                "Drift Detection Logs",
            ],
        },
        "incident_management": {
            "title": "Manage Incidents and Issues",
            "description": "Handle operational incidents and compliance issues effectively",
            "checklist": [
                "Implement incident detection and reporting system",
                "Define incident classification and severity levels",
                "Establish incident response procedures",
                "Conduct root cause analysis for incidents",
                "Document all incidents and resolutions",
                "Report serious incidents to authorities if required",
                "Implement corrective and preventive actions",
            ],
            "required_documents": [
                "Incident Management Procedures",
                "Incident Log and Reports",
            ],
        },
        "documentation_records": {
            "title": "Maintain Documentation and Records",
            "description": "Keep comprehensive and up-to-date operational documentation",
            "checklist": [
                "Maintain operational procedures documentation",
                "Keep records of system changes and updates",
                "Document configuration and settings",
                "Maintain training records for operators",
                "Keep audit trails of significant decisions",
                "Update technical documentation as system evolves",
                "Ensure documentation accessibility for audits",
            ],
            "required_documents": [
                "Operational Documentation",
                "Change Control Records",
            ],
        },
        "compliance_audits": {
            "title": "Conduct Regular Compliance Audits",
            "description": "Perform periodic compliance assessments and audits",
            "checklist": [
                "Schedule regular internal compliance reviews",
                "Conduct self-assessments against requirements",
                "Review operational practices against policies",
                "Assess ongoing conformity with regulations",
                "Identify compliance gaps and issues",
                "Implement corrective actions",
                "Prepare for external audits and inspections",
            ],
            "required_documents": [
                "Audit Schedule and Plans",
                "Audit Reports and Findings",
            ],
        },
        "updates_changes": {
            "title": "Plan for Updates and Changes",
            "description": "Manage system updates, changes, and improvements",
            "checklist": [
                "Establish change management procedures",
                "Assess compliance impact of updates",
                "Test updates in non-production environments",
                "Plan for model retraining and updates",
                "Communicate changes to stakeholders",
                "Update documentation for changes",
                "Monitor post-update performance",
            ],
            "required_documents": [
                "Change Management Procedures",
                "Update Impact Assessments",
            ],
        },
    }
