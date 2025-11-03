"""Base pathway class"""

from abc import ABC, abstractmethod
from typing import List, Optional
from src.models import (
    PathwayType,
    PathwayConfig,
    ComplianceStep,
    UserGoal,
    RegulatoryFramework,
    StepStatus,
)
from src.llm.openai_client import ComplianceGuidanceGenerator
from src.knowledge.eu_regulations import EUAIActKnowledgeBase
from src.knowledge.saudi_regulations import SaudiAIKnowledgeBase
import uuid


class BasePathway(ABC):
    """Base class for compliance pathways"""

    def __init__(self, llm_client: Optional[ComplianceGuidanceGenerator] = None):
        """
        Initialize pathway

        Args:
            llm_client: LLM client for generating guidance
        """
        self.llm_client = llm_client or ComplianceGuidanceGenerator()
        self.eu_kb = EUAIActKnowledgeBase()
        self.saudi_kb = SaudiAIKnowledgeBase()

    @abstractmethod
    def get_config(self) -> PathwayConfig:
        """Get pathway configuration"""
        pass

    @abstractmethod
    def get_default_steps(self) -> List[str]:
        """Get default step titles for this pathway"""
        pass

    def generate_steps(
        self,
        user_goal: UserGoal,
        document_context: Optional[str] = None,
    ) -> List[ComplianceStep]:
        """
        Generate compliance steps for this pathway

        Args:
            user_goal: User's compliance goal
            document_context: Optional context from uploaded documents

        Returns:
            List of compliance steps
        """
        # Use LLM to generate customized steps
        raw_steps = self.llm_client.generate_pathway_steps(
            pathway_type=self.get_config().pathway_type.value,
            user_goal=user_goal.description,
            regulatory_framework=user_goal.regulatory_framework.value,
            document_context=document_context,
        )

        # Convert to ComplianceStep objects
        steps = []
        for idx, raw_step in enumerate(raw_steps):
            step = ComplianceStep(
                id=str(uuid.uuid4()),
                title=raw_step["title"],
                description=raw_step["description"],
                order=idx + 1,
                status=StepStatus.NOT_STARTED,
                checklist_items=raw_step.get("actions", []),
                resources=[],
            )

            # Generate detailed guidance for each step
            step.guidance = self.llm_client.generate_step_guidance(
                step_title=step.title,
                step_description=step.description,
                user_context=user_goal.additional_context,
                regulatory_framework=user_goal.regulatory_framework.value,
            )

            steps.append(step)

        # Add regulatory-specific requirements
        steps = self._enhance_with_regulatory_requirements(steps, user_goal)

        return steps

    def _enhance_with_regulatory_requirements(
        self, steps: List[ComplianceStep], user_goal: UserGoal
    ) -> List[ComplianceStep]:
        """Add regulatory-specific requirements to steps"""

        # This is pathway-specific and can be overridden
        # Base implementation adds general resources

        for step in steps:
            if user_goal.regulatory_framework in [
                RegulatoryFramework.EU_AI_ACT,
                RegulatoryFramework.BOTH,
            ]:
                step.resources.append(
                    {
                        "title": "EU AI Act Reference",
                        "url": "https://artificialintelligenceact.eu/",
                        "type": "regulation",
                    }
                )

            if user_goal.regulatory_framework in [
                RegulatoryFramework.SAUDI_AI,
                RegulatoryFramework.BOTH,
            ]:
                step.resources.append(
                    {
                        "title": "Saudi Data & AI Authority (SDAIA)",
                        "url": "https://sdaia.gov.sa/",
                        "type": "authority",
                    }
                )

        return steps
