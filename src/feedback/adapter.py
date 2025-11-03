"""Adaptive pathway system based on user feedback"""

from typing import List, Dict, Optional
from src.models import UserFeedback, ComplianceStep, PathwaySession
from src.llm.openai_client import ComplianceGuidanceGenerator


class PathwayAdapter:
    """Adapt compliance pathways based on user feedback"""

    def __init__(self, llm_client: Optional[ComplianceGuidanceGenerator] = None):
        """
        Initialize pathway adapter

        Args:
            llm_client: LLM client for generating adaptations
        """
        self.llm_client = llm_client or ComplianceGuidanceGenerator()

    def analyze_feedback(
        self, feedback: UserFeedback, step: ComplianceStep
    ) -> Dict[str, any]:
        """
        Analyze user feedback to determine adaptation needs

        Args:
            feedback: User feedback on a step
            step: The step being evaluated

        Returns:
            Analysis with adaptation recommendations
        """
        analysis = {
            "needs_adaptation": False,
            "adaptation_type": None,
            "recommendations": [],
        }

        # Low rating indicates dissatisfaction
        if feedback.rating <= 2:
            analysis["needs_adaptation"] = True
            analysis["adaptation_type"] = "major_revision"
            analysis["recommendations"].append(
                "Step requires significant revision based on low user rating"
            )

        # User explicitly needs more help
        elif feedback.needs_more_help:
            analysis["needs_adaptation"] = True
            analysis["adaptation_type"] = "add_detail"
            analysis["recommendations"].append(
                "Add more detailed guidance and examples"
            )

        # User suggested specific changes
        if feedback.suggested_changes:
            analysis["needs_adaptation"] = True
            analysis["adaptation_type"] = "user_directed"
            analysis["recommendations"].append(
                f"Incorporate user suggestion: {feedback.suggested_changes}"
            )

        # Moderate rating suggests minor improvements
        elif 3 <= feedback.rating <= 4:
            analysis["adaptation_type"] = "minor_improvement"
            analysis["recommendations"].append(
                "Consider minor enhancements to improve user experience"
            )

        return analysis

    def adapt_step(
        self,
        step: ComplianceStep,
        feedback: UserFeedback,
        session_context: Optional[PathwaySession] = None,
    ) -> ComplianceStep:
        """
        Adapt a specific step based on feedback

        Args:
            step: Step to adapt
            feedback: User feedback
            session_context: Full session context for better adaptation

        Returns:
            Adapted step
        """
        analysis = self.analyze_feedback(feedback, step)

        if not analysis["needs_adaptation"]:
            return step

        # Use LLM to generate adapted content
        adaptation_prompt = self._build_adaptation_prompt(
            step, feedback, analysis, session_context
        )

        adapted_guidance = self.llm_client.generate_step_guidance(
            step_title=step.title,
            step_description=step.description,
            user_context=adaptation_prompt,
        )

        # Update step with adapted guidance
        step.guidance = adapted_guidance

        # Add user notes about the adaptation
        if not step.user_notes:
            step.user_notes = ""
        step.user_notes += f"\n[Adapted based on feedback: {feedback.comment or 'User requested changes'}]"

        return step

    def adapt_pathway(
        self, session: PathwaySession, recent_feedback: List[UserFeedback]
    ) -> PathwaySession:
        """
        Adapt entire pathway based on accumulated feedback

        Args:
            session: Current pathway session
            recent_feedback: Recent user feedback items

        Returns:
            Adapted session
        """
        # Analyze patterns in feedback
        feedback_pattern = self._analyze_feedback_patterns(recent_feedback)

        # If user consistently needs more help, add intermediate steps
        if feedback_pattern["needs_more_detail"]:
            session = self._add_intermediate_steps(session)

        # If user consistently skips certain types of steps, adjust focus
        if feedback_pattern["skip_pattern"]:
            session = self._adjust_focus(session, feedback_pattern["skip_pattern"])

        # If user is progressing well but wants customization
        if feedback_pattern["high_engagement"]:
            session = self._enhance_relevant_areas(session, recent_feedback)

        return session

    def suggest_additional_resources(
        self, step: ComplianceStep, feedback: UserFeedback
    ) -> List[Dict[str, str]]:
        """
        Suggest additional resources based on feedback

        Args:
            step: Current step
            feedback: User feedback

        Returns:
            List of suggested resources
        """
        resources = []

        if feedback.needs_more_help:
            # Add beginner-friendly resources
            resources.extend(
                [
                    {
                        "title": "Detailed Guide to " + step.title,
                        "type": "guide",
                        "description": "Step-by-step walkthrough with examples",
                    },
                    {
                        "title": "Common Challenges and Solutions",
                        "type": "troubleshooting",
                        "description": "Frequent issues and how to resolve them",
                    },
                ]
            )

        if feedback.rating <= 2:
            # Add expert consultation option
            resources.append(
                {
                    "title": "Expert Consultation",
                    "type": "consultation",
                    "description": "Consider consulting with a compliance specialist",
                }
            )

        return resources

    def _build_adaptation_prompt(
        self,
        step: ComplianceStep,
        feedback: UserFeedback,
        analysis: Dict,
        session_context: Optional[PathwaySession],
    ) -> str:
        """Build prompt for LLM adaptation"""

        context_parts = [
            f"User rated this step {feedback.rating}/5",
        ]

        if feedback.comment:
            context_parts.append(f"User comment: {feedback.comment}")

        if feedback.suggested_changes:
            context_parts.append(f"Suggested changes: {feedback.suggested_changes}")

        if feedback.needs_more_help:
            context_parts.append(
                "User needs more detailed help and examples for this step"
            )

        if session_context:
            context_parts.append(
                f"User is on the {session_context.pathway_type.value} pathway"
            )
            if session_context.documents:
                context_parts.append(
                    f"User has uploaded {len(session_context.documents)} document(s)"
                )

        return " | ".join(context_parts)

    def _analyze_feedback_patterns(
        self, feedback_list: List[UserFeedback]
    ) -> Dict[str, any]:
        """Analyze patterns across multiple feedback items"""

        if not feedback_list:
            return {
                "needs_more_detail": False,
                "skip_pattern": None,
                "high_engagement": False,
            }

        avg_rating = sum(f.rating for f in feedback_list) / len(feedback_list)
        help_requests = sum(1 for f in feedback_list if f.needs_more_help)

        return {
            "needs_more_detail": help_requests > len(feedback_list) * 0.5,
            "skip_pattern": None,  # Could analyze which types of steps are skipped
            "high_engagement": avg_rating >= 4
            and any(f.comment or f.suggested_changes for f in feedback_list),
            "average_rating": avg_rating,
        }

    def _add_intermediate_steps(self, session: PathwaySession) -> PathwaySession:
        """Add intermediate steps for users who need more detail"""

        # Find complex steps that could benefit from breaking down
        current_step = session.steps[session.current_step_index]

        # If step has many checklist items, consider breaking it down
        if len(current_step.checklist_items) > 5:
            # This would generate new intermediate steps
            # Implementation would use LLM to break down the step
            pass

        return session

    def _adjust_focus(self, session: PathwaySession, skip_pattern: str) -> PathwaySession:
        """Adjust pathway focus based on skip patterns"""
        # Implementation would reorder or emphasize certain steps
        return session

    def _enhance_relevant_areas(
        self, session: PathwaySession, feedback_list: List[UserFeedback]
    ) -> PathwaySession:
        """Enhance areas where user shows high interest"""
        # Implementation would add depth to areas of interest
        return session
