"""
AI Compliance Assistant - Web Interface

A comprehensive tool for AI compliance with EU and Saudi Arabian regulations.
"""

import streamlit as st
import sys
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import uuid

# Load environment variables
load_dotenv()

# Add src to path
current_dir = Path(__file__).parent.resolve()
sys.path.insert(0, str(current_dir))

from src.models import (
    PathwayType,
    PathwaySession,
    UserGoal,
    RegulatoryFramework,
    UserFeedback,
    StepStatus,
)
from src.llm.openai_client import ComplianceGuidanceGenerator
from src.document_processor.processor import DocumentProcessor
from src.feedback.adapter import PathwayAdapter
from src.pathways.building import BuildingAIPathway
from src.pathways.procuring import ProcuringAIPathway
from src.pathways.operating import OperatingAIPathway
from src.pathways.training import TrainingOnAIPathway


# Page configuration
st.set_page_config(
    page_title="AI Compliance Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .pathway-card {
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #ddd;
        margin-bottom: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .pathway-card:hover {
        border-color: #1f77b4;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    .pathway-card.selected {
        border-color: #1f77b4;
        background-color: #e7f3ff;
    }
    .step-card {
        padding: 1rem;
        border-left: 4px solid #4caf50;
        background-color: #f9f9f9;
        margin-bottom: 1rem;
        border-radius: 5px;
    }
    .step-card.completed {
        border-left-color: #4caf50;
        opacity: 0.7;
    }
    .step-card.in-progress {
        border-left-color: #ff9800;
    }
    .step-card.not-started {
        border-left-color: #9e9e9e;
    }
    .compliance-tip {
        background-color: #fff3cd;
        padding: 1rem;
        border-left: 4px solid: #ffc107;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Initialize session state
def init_session_state():
    """Initialize Streamlit session state"""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "welcome"

    if "session" not in st.session_state:
        st.session_state.session = None

    if "llm_client" not in st.session_state:
        try:
            st.session_state.llm_client = ComplianceGuidanceGenerator()
        except ValueError as e:
            st.session_state.llm_client = None
            st.session_state.llm_error = str(e)

    if "doc_processor" not in st.session_state:
        st.session_state.doc_processor = DocumentProcessor()

    if "pathway_adapter" not in st.session_state:
        st.session_state.pathway_adapter = PathwayAdapter(st.session_state.llm_client)


init_session_state()


# Sidebar
with st.sidebar:
    st.title("🤖 AI Compliance Assistant")

    # Check API key status
    if st.session_state.llm_client is None:
        st.error("⚠️ OpenAI API key not configured")
        st.info(
            "Set `OPENAI_API_KEY` in your `.env` file to enable AI-powered guidance"
        )
    else:
        st.success("✅ AI Guidance Enabled")

    st.markdown("---")

    # Navigation
    st.subheader("Navigation")

    if st.session_state.session:
        current_pathway = st.session_state.session.pathway_type.value.replace(
            "_", " "
        ).title()
        st.info(f"**Current Pathway:** {current_pathway}")

        # Progress indicator
        total_steps = len(st.session_state.session.steps)
        completed_steps = sum(
            1 for s in st.session_state.session.steps if s.status == StepStatus.COMPLETED
        )
        progress = completed_steps / total_steps if total_steps > 0 else 0

        st.progress(progress)
        st.caption(f"Progress: {completed_steps}/{total_steps} steps completed")

        st.markdown("---")

        if st.button("🏠 Start Over", use_container_width=True):
            st.session_state.session = None
            st.session_state.current_page = "welcome"
            st.rerun()

    # About section
    st.markdown("---")
    with st.expander("ℹ️ About"):
        st.markdown(
            """
        **AI Compliance Assistant** helps you navigate EU AI Act and Saudi Arabian AI regulations.

        **Pathways:**
        - 🔨 Building AI
        - 🛒 Procuring AI
        - ⚙️ Operating AI
        - 🎓 Training on AI
        """
        )


# Main content
def show_welcome_page():
    """Display welcome page with pathway selection"""
    st.markdown('<h1 class="main-header">AI Compliance Assistant</h1>', unsafe_allow_html=True)

    st.markdown(
        """
    ### Welcome! 👋

    This tool helps you navigate **EU AI Act** and **Saudi Arabian AI regulations**
    through four specialized pathways tailored to your role and objectives.

    **Choose your pathway below to get started:**
    """
    )

    # Pathway cards
    pathways = {
        PathwayType.BUILDING: {
            "pathway": BuildingAIPathway(),
            "icon": "🔨",
            "title": "Building AI",
            "description": "For developers and teams creating AI systems",
        },
        PathwayType.PROCURING: {
            "pathway": ProcuringAIPathway(),
            "icon": "🛒",
            "title": "Procuring AI",
            "description": "For organizations purchasing AI solutions",
        },
        PathwayType.OPERATING: {
            "pathway": OperatingAIPathway(),
            "icon": "⚙️",
            "title": "Operating AI",
            "description": "For teams deploying and managing AI systems",
        },
        PathwayType.TRAINING: {
            "pathway": TrainingOnAIPathway(),
            "icon": "🎓",
            "title": "Training on AI",
            "description": "For individuals learning about AI compliance",
        },
    }

    cols = st.columns(2)

    for idx, (pathway_type, info) in enumerate(pathways.items()):
        with cols[idx % 2]:
            if st.button(
                f"{info['icon']} **{info['title']}**\n\n{info['description']}",
                key=f"pathway_{pathway_type.value}",
                use_container_width=True,
            ):
                st.session_state.selected_pathway = pathway_type
                st.session_state.current_page = "setup_goal"
                st.rerun()

    # Additional info
    st.markdown("---")
    st.info(
        """
    💡 **Not sure which pathway to choose?**

    - **Building**: You're developing an AI system from scratch
    - **Procuring**: You're evaluating and buying AI solutions from vendors
    - **Operating**: You're deploying or managing AI systems in production
    - **Training**: You want to learn about AI compliance requirements
    """
    )


def show_goal_setup_page():
    """Display goal setup page"""
    st.title("Define Your Compliance Goal")

    pathway_type = st.session_state.selected_pathway
    pathway_icons = {
        PathwayType.BUILDING: "🔨",
        PathwayType.PROCURING: "🛒",
        PathwayType.OPERATING: "⚙️",
        PathwayType.TRAINING: "🎓",
    }

    st.info(
        f"**Selected Pathway:** {pathway_icons[pathway_type]} {pathway_type.value.replace('_', ' ').title()}"
    )

    # Goal input
    st.subheader("What do you want to achieve?")

    goal_description = st.text_area(
        "Describe your compliance goal:",
        placeholder="e.g., Ensure my facial recognition system complies with EU AI Act high-risk requirements",
        height=100,
        help="Be as specific as possible about what you want to accomplish",
    )

    # Regulatory framework selection
    st.subheader("Which regulations apply to you?")

    regulatory_framework = st.radio(
        "Select applicable regulations:",
        [
            ("Both EU and Saudi Arabian", RegulatoryFramework.BOTH),
            ("EU AI Act only", RegulatoryFramework.EU_AI_ACT),
            ("Saudi Arabian regulations only", RegulatoryFramework.SAUDI_AI),
        ],
        format_func=lambda x: x[0],
        help="Select which regulatory frameworks you need to comply with",
    )

    # Timeline (optional)
    timeline = st.text_input(
        "Timeline (optional):",
        placeholder="e.g., Need to be compliant by Q3 2025",
        help="When do you need to achieve compliance?",
    )

    # Additional context
    additional_context = st.text_area(
        "Additional context (optional):",
        placeholder="e.g., We're a healthcare startup in Saudi Arabia planning to operate in EU",
        height=80,
        help="Provide any additional context that might help customize your pathway",
    )

    # Document upload
    st.subheader("📎 Upload Supporting Documents (Optional)")

    st.markdown(
        """
    Upload project documents, specifications, or other relevant files to get more contextualized guidance.

    **Supported formats:** PDF, DOCX, TXT, MD (Max 10MB per file)
    """
    )

    uploaded_files = st.file_uploader(
        "Choose files",
        accept_multiple_files=True,
        type=["pdf", "docx", "txt", "md"],
        help="Upload documents that describe your AI system or project",
    )

    # Submit button
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.current_page = "welcome"
            st.rerun()

    with col3:
        if st.button(
            "Generate Pathway →",
            type="primary",
            use_container_width=True,
            disabled=not goal_description or st.session_state.llm_client is None,
        ):
            if st.session_state.llm_client is None:
                st.error("OpenAI API key is required to generate pathways")
            else:
                # Create user goal
                user_goal = UserGoal(
                    description=goal_description,
                    pathway=pathway_type,
                    regulatory_framework=regulatory_framework[1],
                    timeline=timeline if timeline else None,
                    additional_context=additional_context if additional_context else None,
                )

                # Process uploaded documents
                documents = []
                document_context = ""

                if uploaded_files:
                    with st.spinner("Processing uploaded documents..."):
                        for uploaded_file in uploaded_files:
                            try:
                                # Save file temporarily
                                temp_path = f"/tmp/{uploaded_file.name}"
                                with open(temp_path, "wb") as f:
                                    f.write(uploaded_file.getbuffer())

                                # Process document
                                doc = st.session_state.doc_processor.process_upload(
                                    temp_path, uploaded_file.name
                                )

                                # Summarize for context
                                if doc.content:
                                    summary = st.session_state.llm_client.summarize_documents(
                                        doc.content
                                    )
                                    doc.summary = summary
                                    document_context += f"\n{uploaded_file.name}: {summary}"

                                documents.append(doc)

                            except Exception as e:
                                st.error(f"Error processing {uploaded_file.name}: {str(e)}")

                # Generate pathway steps
                with st.spinner("Generating your customized compliance pathway..."):
                    # Get appropriate pathway class
                    pathway_classes = {
                        PathwayType.BUILDING: BuildingAIPathway,
                        PathwayType.PROCURING: ProcuringAIPathway,
                        PathwayType.OPERATING: OperatingAIPathway,
                        PathwayType.TRAINING: TrainingOnAIPathway,
                    }

                    pathway = pathway_classes[pathway_type](st.session_state.llm_client)
                    steps = pathway.generate_steps(
                        user_goal,
                        document_context if document_context else None,
                    )

                    # Create session
                    st.session_state.session = PathwaySession(
                        session_id=str(uuid.uuid4()),
                        user_goal=user_goal,
                        pathway_type=pathway_type,
                        steps=steps,
                        documents=documents,
                    )

                    st.session_state.current_page = "pathway"
                    st.rerun()


def show_pathway_page():
    """Display pathway with steps"""
    session = st.session_state.session

    st.title(f"{session.pathway_type.value.replace('_', ' ').title()} Pathway")

    # Display user goal
    with st.expander("📋 Your Compliance Goal", expanded=False):
        st.markdown(f"**Goal:** {session.user_goal.description}")
        st.markdown(
            f"**Regulations:** {session.user_goal.regulatory_framework.value.replace('_', ' ').upper()}"
        )
        if session.user_goal.timeline:
            st.markdown(f"**Timeline:** {session.user_goal.timeline}")
        if session.documents:
            st.markdown(f"**Uploaded Documents:** {len(session.documents)} file(s)")

    # Step navigation
    st.markdown("---")

    # Display steps
    for idx, step in enumerate(session.steps):
        is_current = idx == session.current_step_index

        # Step card
        status_class = step.status.value.replace("_", "-")
        status_emoji = {
            StepStatus.NOT_STARTED: "⚪",
            StepStatus.IN_PROGRESS: "🟡",
            StepStatus.COMPLETED: "✅",
            StepStatus.SKIPPED: "⏭️",
        }

        with st.container():
            col1, col2 = st.columns([10, 1])

            with col1:
                st.markdown(
                    f"### {status_emoji[step.status]} Step {step.order}: {step.title}"
                )

            st.markdown(f"**Description:** {step.description}")

            if is_current or step.status == StepStatus.IN_PROGRESS:
                # Show detailed guidance
                if step.guidance:
                    with st.expander("📖 Detailed Guidance", expanded=is_current):
                        st.markdown(step.guidance)

                # Show checklist
                if step.checklist_items:
                    st.markdown("**Checklist:**")
                    for item in step.checklist_items:
                        st.checkbox(
                            item,
                            key=f"check_{step.id}_{item[:20]}",
                            disabled=step.status == StepStatus.COMPLETED,
                        )

                # Show resources
                if step.resources:
                    with st.expander("🔗 Resources"):
                        for resource in step.resources:
                            st.markdown(f"- [{resource['title']}]({resource.get('url', '#')})")

                # Action buttons
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    if step.status != StepStatus.IN_PROGRESS:
                        if st.button(
                            "Start Step",
                            key=f"start_{step.id}",
                            use_container_width=True,
                        ):
                            step.status = StepStatus.IN_PROGRESS
                            session.current_step_index = idx
                            st.rerun()

                with col2:
                    if step.status == StepStatus.IN_PROGRESS:
                        if st.button(
                            "Mark Complete",
                            key=f"complete_{step.id}",
                            type="primary",
                            use_container_width=True,
                        ):
                            step.status = StepStatus.COMPLETED
                            step.completed_at = datetime.now()

                            # Move to next step if available
                            if idx < len(session.steps) - 1:
                                session.current_step_index = idx + 1
                                session.steps[idx + 1].status = StepStatus.IN_PROGRESS

                            st.rerun()

                with col3:
                    if st.button(
                        "Skip",
                        key=f"skip_{step.id}",
                        use_container_width=True,
                        disabled=step.status == StepStatus.COMPLETED,
                    ):
                        step.status = StepStatus.SKIPPED
                        if idx < len(session.steps) - 1:
                            session.current_step_index = idx + 1
                        st.rerun()

                with col4:
                    if st.button(
                        "💬 Feedback",
                        key=f"feedback_{step.id}",
                        use_container_width=True,
                    ):
                        st.session_state.feedback_step_id = step.id
                        st.session_state.show_feedback_form = True

                # Feedback form
                if (
                    st.session_state.get("show_feedback_form")
                    and st.session_state.get("feedback_step_id") == step.id
                ):
                    with st.form(f"feedback_form_{step.id}"):
                        st.subheader("Provide Feedback")

                        rating = st.slider(
                            "How helpful was this step?", 1, 5, 3, key=f"rating_{step.id}"
                        )

                        comment = st.text_area(
                            "Comments (optional):",
                            key=f"comment_{step.id}",
                            placeholder="Share your thoughts...",
                        )

                        needs_help = st.checkbox(
                            "I need more help with this step", key=f"help_{step.id}"
                        )

                        suggested_changes = st.text_area(
                            "Suggested improvements (optional):",
                            key=f"suggestions_{step.id}",
                        )

                        submit_feedback = st.form_submit_button("Submit Feedback")

                        if submit_feedback:
                            feedback = UserFeedback(
                                step_id=step.id,
                                rating=rating,
                                comment=comment if comment else None,
                                needs_more_help=needs_help,
                                suggested_changes=suggested_changes if suggested_changes else None,
                            )

                            session.feedback_history.append(feedback)

                            # Adapt step based on feedback if needed
                            if feedback.rating <= 3 or feedback.needs_more_help:
                                adapted_step = st.session_state.pathway_adapter.adapt_step(
                                    step, feedback, session
                                )
                                # Update step in session
                                for s in session.steps:
                                    if s.id == step.id:
                                        s.guidance = adapted_step.guidance
                                        s.user_notes = adapted_step.user_notes

                                st.success(
                                    "Thank you! We've updated the guidance based on your feedback."
                                )
                            else:
                                st.success("Thank you for your feedback!")

                            st.session_state.show_feedback_form = False
                            st.rerun()

            st.markdown("---")

    # Completion check
    all_completed = all(
        s.status in [StepStatus.COMPLETED, StepStatus.SKIPPED] for s in session.steps
    )

    if all_completed:
        st.balloons()
        st.success("🎉 Congratulations! You've completed all steps in this pathway!")

        st.markdown(
            """
        ### Next Steps:
        - Review your completed steps and documentation
        - Consider scheduling a compliance audit
        - Stay updated on regulatory changes
        - Export your compliance report (coming soon)
        """
        )


# Main app logic
def main():
    """Main application logic"""
    if st.session_state.current_page == "welcome":
        show_welcome_page()
    elif st.session_state.current_page == "setup_goal":
        show_goal_setup_page()
    elif st.session_state.current_page == "pathway":
        show_pathway_page()


if __name__ == "__main__":
    main()
