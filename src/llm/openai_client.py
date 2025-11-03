"""OpenAI API client for generating compliance guidance"""

import os
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class ComplianceGuidanceGenerator:
    """Generate AI compliance guidance using OpenAI"""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize OpenAI client

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model to use (defaults to OPENAI_MODEL env var or gpt-4-turbo-preview)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not found. Set OPENAI_API_KEY environment variable."
            )

        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")
        self.client = OpenAI(api_key=self.api_key)

    def generate_pathway_steps(
        self,
        pathway_type: str,
        user_goal: str,
        regulatory_framework: str,
        document_context: Optional[str] = None,
    ) -> List[Dict[str, str]]:
        """
        Generate structured compliance steps for a pathway

        Args:
            pathway_type: Type of pathway (building, procuring, operating, training)
            user_goal: User's compliance goal
            regulatory_framework: EU, Saudi, or both
            document_context: Optional context from uploaded documents

        Returns:
            List of steps with title, description, and guidance
        """
        system_prompt = self._build_system_prompt(pathway_type, regulatory_framework)
        user_prompt = self._build_user_prompt(user_goal, document_context)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=2000,
        )

        # Parse the response into structured steps
        return self._parse_steps_response(response.choices[0].message.content)

    def generate_step_guidance(
        self,
        step_title: str,
        step_description: str,
        user_context: Optional[str] = None,
        regulatory_framework: str = "both",
    ) -> str:
        """
        Generate detailed guidance for a specific step

        Args:
            step_title: Title of the compliance step
            step_description: Description of the step
            user_context: Optional user-specific context
            regulatory_framework: Relevant regulatory framework

        Returns:
            Detailed guidance text
        """
        prompt = f"""
You are an AI compliance expert. Provide detailed, actionable guidance for the following compliance step:

**Step**: {step_title}
**Description**: {step_description}
**Regulatory Framework**: {regulatory_framework.upper().replace('_', ' ')}

{f"**User Context**: {user_context}" if user_context else ""}

Provide:
1. Clear, step-by-step instructions
2. Specific regulatory requirements
3. Best practices and recommendations
4. Common pitfalls to avoid
5. Relevant templates or checklists

Format your response in a clear, actionable manner.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500,
        )

        return response.choices[0].message.content

    def adapt_pathway_from_feedback(
        self,
        current_steps: List[Dict[str, str]],
        feedback: str,
        user_goal: str,
    ) -> List[Dict[str, str]]:
        """
        Adapt pathway based on user feedback

        Args:
            current_steps: Current list of steps
            feedback: User's feedback
            user_goal: Original user goal

        Returns:
            Adapted list of steps
        """
        prompt = f"""
You are an AI compliance expert. A user is working through a compliance pathway with the following goal:

**Goal**: {user_goal}

**Current Steps**:
{self._format_steps_for_prompt(current_steps)}

**User Feedback**: {feedback}

Based on this feedback, adjust the pathway to better meet the user's needs while ensuring all compliance requirements are still addressed.

Return the updated steps in the same format, making modifications as needed.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000,
        )

        return self._parse_steps_response(response.choices[0].message.content)

    def summarize_documents(self, document_content: str, max_length: int = 500) -> str:
        """
        Summarize uploaded documents for context

        Args:
            document_content: Full document text
            max_length: Maximum summary length in words

        Returns:
            Summary text
        """
        prompt = f"""
Summarize the following document, focusing on aspects relevant to AI compliance:

{document_content[:8000]}  # Limit input to avoid token limits

Provide a {max_length}-word summary highlighting:
- Purpose of the document
- AI systems or processes described
- Compliance considerations mentioned
- Key technical details
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=800,
        )

        return response.choices[0].message.content

    def _build_system_prompt(self, pathway_type: str, regulatory_framework: str) -> str:
        """Build system prompt based on pathway and framework"""

        framework_context = {
            "eu_ai_act": "Focus on EU AI Act requirements including risk classification, transparency, documentation, and conformity assessment.",
            "saudi_ai": "Focus on Saudi Arabian AI principles including data governance, ethical AI, and national regulations.",
            "both": "Address both EU AI Act and Saudi Arabian AI regulations, highlighting differences and common requirements.",
        }

        pathway_context = {
            "building": "You are helping developers and teams building AI systems ensure compliance from design through deployment.",
            "procuring": "You are helping organizations evaluate and procure AI solutions with compliance in mind.",
            "operating": "You are helping teams deploy and operate AI systems in compliance with regulations.",
            "training": "You are helping individuals understand AI compliance requirements and best practices.",
        }

        return f"""
You are an expert AI compliance advisor specializing in {regulatory_framework.upper().replace('_', ' ')}.

{pathway_context.get(pathway_type, '')}

{framework_context.get(regulatory_framework, '')}

Your role is to provide practical, actionable guidance tailored to the user's specific situation.
"""

    def _build_user_prompt(
        self, user_goal: str, document_context: Optional[str] = None
    ) -> str:
        """Build user prompt with goal and context"""

        prompt = f"""
Create a structured compliance pathway for the following goal:

**User Goal**: {user_goal}

{f"**Document Context**: {document_context}" if document_context else ""}

Generate 5-8 sequential steps that will help achieve this goal. For each step, provide:
- Title (clear, action-oriented)
- Description (2-3 sentences explaining what needs to be done)
- Key Actions (3-5 specific actions)

Format as:
STEP 1: [Title]
Description: [Description]
Actions:
- [Action 1]
- [Action 2]
...
"""

        return prompt

    def _parse_steps_response(self, response_text: str) -> List[Dict[str, str]]:
        """Parse LLM response into structured steps"""

        steps = []
        current_step = None

        for line in response_text.split("\n"):
            line = line.strip()

            if line.startswith("STEP"):
                if current_step:
                    steps.append(current_step)

                # Extract step number and title
                parts = line.split(":", 1)
                title = parts[1].strip() if len(parts) > 1 else line

                current_step = {
                    "title": title,
                    "description": "",
                    "actions": [],
                }

            elif line.startswith("Description:") and current_step:
                current_step["description"] = line.replace("Description:", "").strip()

            elif line.startswith("Actions:") and current_step:
                continue  # Actions header

            elif line.startswith("-") and current_step:
                action = line.lstrip("- ").strip()
                if action:
                    current_step["actions"].append(action)

            elif line and current_step and not current_step["description"]:
                # Additional description text
                current_step["description"] += " " + line

        # Add last step
        if current_step:
            steps.append(current_step)

        return steps

    def _format_steps_for_prompt(self, steps: List[Dict[str, str]]) -> str:
        """Format steps for inclusion in a prompt"""

        formatted = []
        for i, step in enumerate(steps, 1):
            formatted.append(f"STEP {i}: {step['title']}")
            formatted.append(f"Description: {step['description']}")
            if "actions" in step:
                formatted.append("Actions:")
                for action in step["actions"]:
                    formatted.append(f"- {action}")
            formatted.append("")

        return "\n".join(formatted)
