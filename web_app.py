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
    NEOMProject,
    PhaseType,
    RACIMatrix,
    RACIEntry,
    RACIRole,
    Evidence,
    EvidenceType,
    PitstopCheckpoint,
    PitstopStatus,
)
from src.llm.openai_client import ComplianceGuidanceGenerator
from src.document_processor.processor import DocumentProcessor
from src.feedback.adapter import PathwayAdapter
from src.pathways.building import BuildingAIPathway
from src.pathways.procuring import ProcuringAIPathway
from src.pathways.operating import OperatingAIPathway
from src.pathways.training import TrainingOnAIPathway
from src.pathways.neom_building_updated import NEOMBuildingAIPathway
from src.storage.project_storage import ProjectStorageManager
from src.notifications.email_service import EmailService
from src.rag.document_rag import DocumentRAG


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

    if "storage_manager" not in st.session_state:
        st.session_state.storage_manager = ProjectStorageManager()

    if "email_service" not in st.session_state:
        st.session_state.email_service = EmailService()

    if "neom_project" not in st.session_state:
        st.session_state.neom_project = None

    if "rag_system" not in st.session_state:
        try:
            st.session_state.rag_system = DocumentRAG()
        except ValueError:
            st.session_state.rag_system = None

    if "rag_documents" not in st.session_state:
        st.session_state.rag_documents = []


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

    # Document upload section
    st.subheader("📚 Project Documents")

    if st.session_state.rag_system:
        st.success(f"✅ {len(st.session_state.rag_documents)} documents loaded")

        with st.expander("Upload Documents", expanded=len(st.session_state.rag_documents) == 0):
            st.markdown("""
            Upload your project documents here. The AI will use these to automatically fill in compliance questions.

            **Supported formats:** PDF, DOCX, TXT, MD
            """)

            uploaded_files = st.file_uploader(
                "Choose files",
                accept_multiple_files=True,
                type=["pdf", "docx", "txt", "md"],
                key="rag_uploader"
            )

            if st.button("Process Documents", key="process_rag_docs"):
                if uploaded_files:
                    with st.spinner("Processing documents..."):
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

                                if doc.content:
                                    # Add to RAG system
                                    st.session_state.rag_system.add_documents([{
                                        "id": doc.id,
                                        "name": doc.filename,
                                        "content": doc.content
                                    }])

                                    st.session_state.rag_documents.append({
                                        "id": doc.id,
                                        "name": doc.filename,
                                        "size": len(doc.content)
                                    })

                            except Exception as e:
                                st.error(f"Error processing {uploaded_file.name}: {str(e)}")

                    st.success(f"✅ Processed {len(uploaded_files)} documents!")
                    st.rerun()

        # Show loaded documents
        if st.session_state.rag_documents:
            with st.expander("Loaded Documents", expanded=False):
                for doc in st.session_state.rag_documents:
                    st.markdown(f"📄 **{doc['name']}** ({doc['size']:,} chars)")
    else:
        st.warning("⚠️ RAG system requires OpenAI API key")

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

    elif st.session_state.neom_project:
        st.info(f"**NEOM Project:** {st.session_state.neom_project.project_name}")

        # Calculate overall progress
        total_steps = sum(len(phase.steps) for phase in st.session_state.neom_project.phases)
        completed_steps = sum(
            1 for phase in st.session_state.neom_project.phases
            for s in phase.steps if s.status == StepStatus.COMPLETED
        )
        progress = completed_steps / total_steps if total_steps > 0 else 0

        st.progress(progress)
        st.caption(f"Progress: {completed_steps}/{total_steps} steps completed")

        st.markdown("---")

        # Answer History for Auditing
        st.subheader("📋 Answer History")
        if st.session_state.neom_project.evidence:
            # Group evidence by phase
            phase_names = {
                PhaseType.PLANNING_DESIGN: "Phase 1: Planning & Design",
                PhaseType.DATA_PREPARATION: "Phase 2: Data Preparation",
                PhaseType.BUILD_VALIDATE: "Phase 3: Build & Validate",
                PhaseType.DEPLOYMENT_MONITORING: "Phase 4: Deployment & Monitoring"
            }

            # Create dropdown options
            evidence_options = []
            for evidence in st.session_state.neom_project.evidence:
                phase_name = phase_names.get(evidence.phase, "Unknown Phase")
                if evidence.questions:
                    question_title = list(evidence.questions.keys())[0]
                    evidence_options.append(f"{phase_name} - {question_title}")
                else:
                    evidence_options.append(f"{phase_name} - {evidence.id[:8]}")

            if evidence_options:
                selected_evidence = st.selectbox(
                    "View saved answers:",
                    options=["Select an answer..."] + evidence_options,
                    key="answer_history_selector"
                )

                if selected_evidence != "Select an answer...":
                    # Find the selected evidence
                    selected_idx = evidence_options.index(selected_evidence)
                    evidence = st.session_state.neom_project.evidence[selected_idx]

                    with st.expander("📄 Answer Details", expanded=True):
                        if evidence.questions and evidence.answers:
                            for question, answer_text in evidence.answers.items():
                                st.markdown(f"**Q:** {question}")
                                st.markdown(f"**A:** {answer_text}")
                                st.markdown("---")

                        if evidence.file_path:
                            st.caption(f"📎 File: {evidence.file_path}")

                        st.caption(f"🕒 Saved: {evidence.created_at.strftime('%Y-%m-%d %H:%M')}")
        else:
            st.caption("No answers saved yet")

        st.markdown("---")

        if st.button("🏠 Start Over", use_container_width=True):
            st.session_state.neom_project = None
            st.session_state.current_page = "welcome"
            st.rerun()

    # About section
    st.markdown("---")
    with st.expander("ℹ️ About"):
        st.markdown(
            """
        **AI Compliance Assistant** helps you navigate EU AI Act and Saudi Arabian AI regulations.

        **Pathways:**
        - 🏗️ Building AI
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
    through specialized pathways tailored to your role and objectives.
    """
    )

    # Load existing project section
    st.markdown("---")
    st.markdown("### 📂 Load Existing Project")

    existing_projects = st.session_state.storage_manager.list_all_projects()

    if existing_projects:
        project_options = {
            f"{proj['project_name']} ({proj['ai_system_name']})": proj['project_id']
            for proj in existing_projects
        }
        project_options = {"-- Select a project --": None, **project_options}

        selected_project_display = st.selectbox(
            "Choose an existing NEOM Building AI project:",
            options=list(project_options.keys()),
            key="existing_project_selector"
        )

        if selected_project_display and selected_project_display != "-- Select a project --":
            project_id = project_options[selected_project_display]

            if st.button("📂 Load Project", type="primary"):
                loaded_project = st.session_state.storage_manager.load_project(project_id)
                if loaded_project:
                    st.session_state.neom_project = loaded_project
                    st.session_state.current_page = "neom_pathway"
                    st.success(f"✅ Loaded project: {loaded_project.project_name}")
                    st.rerun()
                else:
                    st.error("Failed to load project")
    else:
        st.info("No existing projects found. Create a new project below.")

    st.markdown("---")
    st.markdown("### 🆕 Create New Project")
    st.markdown("**Choose your pathway below to get started:**")

    # Pathway cards
    pathways = {
        "neom_building": {
            "icon": "🏗️",
            "title": "Building AI",
            "description": "Comprehensive 4-phase journey for building trustworthy AI systems with evidence collection, RACI management, and pitstop checkpoints",
            "page": "neom_project_init",
        },
        PathwayType.PROCURING: {
            "icon": "🛒",
            "title": "Procuring AI",
            "description": "For organizations purchasing AI solutions",
            "page": "setup_goal",
        },
        PathwayType.OPERATING: {
            "icon": "⚙️",
            "title": "Operating AI",
            "description": "For teams deploying and managing AI systems",
            "page": "setup_goal",
        },
        PathwayType.TRAINING: {
            "icon": "🎓",
            "title": "Training on AI",
            "description": "For individuals learning about AI compliance",
            "page": "setup_goal",
        },
    }

    cols = st.columns(2)

    for idx, (pathway_type, info) in enumerate(pathways.items()):
        with cols[idx % 2]:
            if st.button(
                f"{info['icon']} **{info['title']}**\n\n{info['description']}",
                key=f"pathway_{pathway_type.value if isinstance(pathway_type, PathwayType) else pathway_type}",
                use_container_width=True,
            ):
                st.session_state.selected_pathway = pathway_type
                st.session_state.current_page = info["page"]
                st.rerun()

    # Additional info
    st.markdown("---")
    st.info(
        """
    💡 **Not sure which pathway to choose?**

    - **Building AI**: Comprehensive 4-phase journey with evidence collection, RACI management, and formal pitstop checkpoints for developing AI systems
    - **Procuring AI**: Evaluating and purchasing AI solutions from vendors
    - **Operating AI**: Deploying and managing AI systems in production
    - **Training on AI**: Learning about AI compliance requirements
    """
    )


def show_goal_setup_page():
    """Display goal setup page"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_goal_setup"):
        st.session_state.current_page = "welcome"
        st.rerun()

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
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_pathway"):
        st.session_state.current_page = "welcome"
        st.rerun()

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


def show_neom_project_init_page():
    """Display NEOM project initialization page"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_init"):
        st.session_state.current_page = "welcome"
        st.rerun()

    st.title("🏗️ NEOM Trustworthy AI - Project Initialization")

    st.markdown("""
    ### Create Your AI Compliance Project

    This comprehensive pathway guides you through the **4 phases** of trustworthy AI development:
    1. 📋 **Planning & Design** - Governance, scope, and risk analysis
    2. 📊 **Data Preparation** - Data quality, bias mitigation, privacy
    3. 🔨 **Build & Validate** - Model training, fairness, security validation
    4. 🚀 **Deployment & Monitoring** - Deployment and continuous monitoring

    Each phase includes **pitstop checkpoint meetings** for PDPO review and approval.
    """)

    st.markdown("---")
    st.subheader("Project Information")

    with st.form("neom_project_form"):
        project_name = st.text_input(
            "Project Name *",
            placeholder="e.g., Customer Service Chatbot Project",
            help="Internal name for tracking this project"
        )

        ai_system_name = st.text_input(
            "AI System Name *",
            placeholder="e.g., SmartBot Customer Assistant",
            help="Official name of the AI system being developed"
        )

        ai_system_purpose = st.text_area(
            "AI System Purpose *",
            placeholder="Describe what this AI system will do and why...",
            height=100,
            help="Clear description of the AI system's intended purpose and use cases"
        )

        st.markdown("### RACI Matrix Setup")
        st.markdown("Define key stakeholders and their roles (you can modify this later)")

        col1, col2 = st.columns(2)

        with col1:
            project_lead_name = st.text_input("Project Lead Name *")
            project_lead_email = st.text_input("Project Lead Email *")

        with col2:
            pdpo_name = st.text_input("PDPO Reviewer Name *")
            pdpo_email = st.text_input("PDPO Reviewer Email *")

        st.markdown("### Notification Settings")
        email_notifications = st.checkbox(
            "Enable email notifications for pitstop meetings",
            value=True,
            help="Send email invitations when pitstop checkpoints are ready for review"
        )

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.form_submit_button("← Back", use_container_width=True):
                st.session_state.current_page = "welcome"
                st.rerun()

        with col2:
            submit = st.form_submit_button("Create Project →", type="primary", use_container_width=True)

        if submit:
            if not all([project_name, ai_system_name, ai_system_purpose,
                       project_lead_name, project_lead_email, pdpo_name, pdpo_email]):
                st.error("Please fill in all required fields marked with *")
            else:
                # Create NEOM project
                project_id = str(uuid.uuid4())

                # Create project folder structure
                st.session_state.storage_manager.create_project_folder(project_id)

                # Initialize RACI matrix
                raci_matrix = RACIMatrix(
                    project_id=project_id,
                    entries=[
                        RACIEntry(
                            task_name="Overall Project Management",
                            responsible=[project_lead_email],
                            accountable=[project_lead_email],
                            consulted=[pdpo_email],
                            informed=[]
                        )
                    ]
                )

                # Create NEOM project
                neom_project = NEOMProject(
                    project_id=project_id,
                    project_name=project_name,
                    ai_system_name=ai_system_name,
                    ai_system_purpose=ai_system_purpose,
                    raci_matrix=raci_matrix,
                    phases=[],
                    evidence=[],
                    pitstops=[]
                )

                # Initialize pathway and phases
                pathway = NEOMBuildingAIPathway()
                phases = pathway.create_phases(project_id)
                neom_project.phases = phases

                # Create initial pitstop (project initiation)
                initial_pitstop = PitstopCheckpoint(
                    id=str(uuid.uuid4()),
                    project_id=project_id,
                    phase_completed=PhaseType.PLANNING_DESIGN,
                    status=PitstopStatus.PENDING,
                    pdpo_reviewer=pdpo_email,
                    participants=[project_lead_email, pdpo_email]
                )
                neom_project.pitstops.append(initial_pitstop)

                # Store in session
                st.session_state.neom_project = neom_project
                st.session_state.email_notifications_enabled = email_notifications

                # Save project to storage
                st.session_state.storage_manager.save_project(neom_project)

                st.success(f"✅ Project '{project_name}' created successfully!")
                st.info(f"📁 Project ID: `{project_id}`")

                st.session_state.current_page = "neom_pathway"
                st.rerun()


def show_neom_pathway_page():
    """Display NEOM pathway with phases and steps"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_pathway"):
        st.session_state.current_page = "welcome"
        st.rerun()

    project = st.session_state.neom_project

    if not project:
        st.error("No NEOM project found. Please create a project first.")
        if st.button("← Back to Home"):
            st.session_state.current_page = "welcome"
            st.rerun()
        return

    # Header
    st.title(f"🏗️ {project.project_name}")
    st.markdown(f"**AI System:** {project.ai_system_name}")
    st.markdown(f"**Purpose:** {project.ai_system_purpose}")

    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Phases & Steps", "👥 RACI Matrix", "📄 Evidence", "🔍 Pitstops"])

    with tab1:
        show_neom_phases_view(project)

    with tab2:
        show_neom_raci_view(project)

    with tab3:
        show_neom_evidence_view(project)

    with tab4:
        show_neom_pitstops_view(project)


def show_neom_phases_view(project: NEOMProject):
    """Show phases and steps view"""
    st.markdown("### Trustworthy AI Development Phases")

    # Phase progress
    phase_icons = {
        PhaseType.PLANNING_DESIGN: "📋",
        PhaseType.DATA_PREPARATION: "📊",
        PhaseType.BUILD_VALIDATE: "🔨",
        PhaseType.DEPLOYMENT_MONITORING: "🚀"
    }

    # Display phases
    for phase in project.phases:
        phase_completed = all(s.status == StepStatus.COMPLETED for s in phase.steps)
        phase_in_progress = any(s.status == StepStatus.IN_PROGRESS for s in phase.steps)

        status_emoji = "✅" if phase_completed else "🟡" if phase_in_progress else "⚪"

        with st.expander(
            f"{status_emoji} {phase_icons.get(phase.phase_type, '📌')} **Phase {phase.order}: {phase.name}**",
            expanded=phase_in_progress or (not phase_completed and phase.order == 1)
        ):
            st.markdown(f"**Description:** {phase.description}")

            # Steps in this phase
            st.markdown(f"**Steps ({len(phase.steps)}):**")

            for step in phase.steps:
                step_status_emoji = {
                    StepStatus.NOT_STARTED: "⚪",
                    StepStatus.IN_PROGRESS: "🟡",
                    StepStatus.COMPLETED: "✅",
                    StepStatus.SKIPPED: "⏭️"
                }[step.status]

                with st.container():
                    col1, col2 = st.columns([8, 2])

                    with col1:
                        st.markdown(f"{step_status_emoji} **{step.title}**")

                    with col2:
                        if step.status == StepStatus.NOT_STARTED:
                            if st.button("Start", key=f"start_step_{step.id}", use_container_width=True):
                                step.status = StepStatus.IN_PROGRESS
                                st.rerun()

                    # Show details if in progress
                    if step.status == StepStatus.IN_PROGRESS:
                        # Display the regulatory requirement/control description
                        if step.description:
                            st.info(f"**Regulatory Requirement:**\n\n{step.description}")

                        st.markdown("**Checklist:**")
                        for item in step.checklist_items:
                            st.checkbox(item, key=f"check_{step.id}_{item[:30]}")

                        # Evidence collection
                        st.markdown("**📎 Collect Evidence:**")
                        evidence_type = st.selectbox(
                            "Evidence Type",
                            [e.value for e in EvidenceType],
                            key=f"evidence_type_{step.id}"
                        )

                        # RAG-powered answer generation
                        if st.session_state.rag_system and st.session_state.rag_documents:
                            st.markdown("**🤖 AI-Assisted Completion:**")

                            # Generate question based on step
                            question = f"{step.title}: {step.description}"

                            if st.button("✨ Generate Answer from Documents", key=f"rag_gen_{step.id}"):
                                with st.spinner("Analyzing your project documents..."):
                                    result = st.session_state.rag_system.answer_question(question)

                                    if result["answer"] or result["guidance"]:
                                        st.session_state[f"draft_answer_{step.id}"] = result["answer"]
                                        st.session_state[f"draft_guidance_{step.id}"] = result["guidance"]
                                        st.session_state[f"draft_gap_analysis_{step.id}"] = result["gap_analysis"]
                                        st.session_state[f"draft_sources_{step.id}"] = result["sources"]
                                        st.session_state[f"draft_confidence_{step.id}"] = result["confidence"]
                                        st.rerun()

                            # Show draft answer if generated
                            if f"draft_answer_{step.id}" in st.session_state:
                                confidence = st.session_state.get(f"draft_confidence_{step.id}", 0)
                                confidence_color = "green" if confidence > 0.7 else "orange" if confidence > 0.5 else "red"

                                st.markdown(f"**AI Analysis** (Confidence: :{confidence_color}[{confidence:.0%}])")

                                # Two-column layout
                                col_answer, col_guidance = st.columns(2)

                                with col_answer:
                                    st.markdown("**📄 Extracted from Your Documents:**")
                                    # Editable answer
                                    edited_answer = st.text_area(
                                        "Information found in your documents:",
                                        value=st.session_state[f"draft_answer_{step.id}"],
                                        height=250,
                                        key=f"edit_answer_{step.id}",
                                        help="This is what the AI found in your uploaded documents. Edit as needed."
                                    )

                                with col_guidance:
                                    st.markdown("**💡 What Should Be Covered:**")
                                    guidance_text = st.session_state.get(f"draft_guidance_{step.id}", "")
                                    st.text_area(
                                        "Ideal answer should include:",
                                        value=guidance_text,
                                        height=250,
                                        key=f"guidance_{step.id}",
                                        disabled=True,
                                        help="Guidance on what a complete answer should cover"
                                    )

                                # Gap Analysis Box
                                st.markdown("**⚠️ Gap Analysis - What's Missing:**")
                                gap_analysis = st.session_state.get(f"draft_gap_analysis_{step.id}", "")
                                st.text_area(
                                    "Weaknesses and information you need to add:",
                                    value=gap_analysis,
                                    height=150,
                                    key=f"gap_analysis_{step.id}",
                                    disabled=True,
                                    help="This shows what information is missing or incomplete compared to the ideal answer"
                                )

                                # Show sources (always visible to help debug)
                                st.markdown("**📚 Document Sources Used:**")
                                sources = st.session_state.get(f"draft_sources_{step.id}", [])
                                if sources:
                                    for i, source in enumerate(sources, 1):
                                        relevance = source['similarity']
                                        color = "🟢" if relevance > 0.7 else "🟡" if relevance > 0.4 else "🔴"
                                        st.markdown(f"{color} **{source['document']}** - Relevance: {relevance:.0%}")

                                    show_excerpts = st.checkbox("Show excerpts", key=f"show_excerpts_{step.id}", value=False)
                                    if show_excerpts:
                                        for i, source in enumerate(sources, 1):
                                            st.caption(f"{i}. {source['excerpt']}")
                                            st.markdown("---")
                                else:
                                    st.caption("No sources retrieved")

                                # Save button and evidence upload
                                st.markdown("---")

                                uploaded_file = st.file_uploader(
                                    "📎 Upload Supporting Document (optional)",
                                    key=f"upload_{step.id}",
                                    type=["pdf", "docx", "txt", "md"],
                                    help="Upload any supporting evidence documents"
                                )

                                if st.button("💾 Save Answer & Evidence", key=f"save_evidence_{step.id}", type="primary", use_container_width=True):
                                    # Create evidence entry with edited answer
                                    evidence_id = str(uuid.uuid4())
                                    evidence = Evidence(
                                        id=evidence_id,
                                        project_id=project.project_id,
                                        phase=phase.phase_type,
                                        step_id=step.id,
                                        evidence_type=EvidenceType(evidence_type),
                                        title=step.title,
                                        description=step.description,
                                        questions={step.title: step.description},
                                        answers={step.title: edited_answer if edited_answer else ""}
                                    )

                                    # Save uploaded file if provided
                                    if uploaded_file:
                                        temp_path = f"/tmp/{uploaded_file.name}"
                                        with open(temp_path, "wb") as f:
                                            f.write(uploaded_file.getbuffer())

                                        file_path = st.session_state.storage_manager.save_evidence(
                                            project.project_id,
                                            evidence
                                        )
                                        evidence.file_path = str(file_path)

                                    project.evidence.append(evidence)

                                    # Auto-save project
                                    st.session_state.storage_manager.save_project(project)

                                    st.success("✅ Answer and evidence saved successfully!")

                                    # Clear draft data after saving
                                    if f"draft_answer_{step.id}" in st.session_state:
                                        del st.session_state[f"draft_answer_{step.id}"]
                                    if f"draft_guidance_{step.id}" in st.session_state:
                                        del st.session_state[f"draft_guidance_{step.id}"]
                                    if f"draft_gap_analysis_{step.id}" in st.session_state:
                                        del st.session_state[f"draft_gap_analysis_{step.id}"]

                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("✅ Mark Complete", key=f"complete_{step.id}", type="primary"):
                                step.status = StepStatus.COMPLETED
                                step.completed_at = datetime.now()
                                st.rerun()

                        with col2:
                            if st.button("Skip", key=f"skip_{step.id}"):
                                step.status = StepStatus.SKIPPED
                                st.rerun()

                    st.markdown("---")

            # Check if phase is complete and show pitstop button
            if phase_completed:
                st.success(f"✅ Phase {phase.order} completed!")

                # Check if pitstop exists for this phase
                pitstop = next((p for p in project.pitstops if p.phase_completed == phase.phase_type), None)

                if not pitstop:
                    if st.button(f"📍 Schedule Pitstop Checkpoint for Phase {phase.order}",
                               key=f"schedule_pitstop_{phase.phase_type.value}"):
                        # Create pitstop
                        pitstop_id = str(uuid.uuid4())
                        new_pitstop = PitstopCheckpoint(
                            id=pitstop_id,
                            project_id=project.project_id,
                            phase_completed=phase.phase_type,
                            status=PitstopStatus.PENDING,
                            pdpo_reviewer=project.raci_matrix.entries[0].accountable if project.raci_matrix else None,
                            participants=[]
                        )
                        project.pitstops.append(new_pitstop)

                        # Send email notification if enabled
                        if st.session_state.get("email_notifications_enabled"):
                            st.session_state.email_service.send_pitstop_notification(project, new_pitstop)

                        st.success("Pitstop scheduled! Check the Pitstops tab.")
                        st.rerun()


def show_neom_raci_view(project: NEOMProject):
    """Show RACI matrix management"""
    st.markdown("### RACI Matrix")

    st.info("""
    **RACI Definitions:**
    - **Responsible (R)**: The individual(s) who perform the task or do the work. There can be multiple people responsible for a task.
    - **Accountable (A)**: The one person who is answerable for the correct and thorough completion of the deliverable or task, and who approves the work. There must be only one "A" per task.
    - **Consulted (C)**: People whose input and expertise are required before a decision is made or a task is completed (two-way communication).
    - **Informed (I)**: People who are kept up-to-date on the progress or outcome of the task (one-way communication).
    """)

    # Define team members section
    st.markdown("---")
    st.markdown("### 👥 Define Team Members for RACI Roles")
    st.markdown("Enter the name and email for each role in the RACI matrix:")

    # Initialize team members dict in session state if not exists
    if 'raci_team_members' not in st.session_state:
        st.session_state.raci_team_members = {}

    # Define the 7 RACI roles
    raci_roles = [
        "AI Product Manager",
        "Data Scientist",
        "Software Engineer",
        "Compliance Officer / Legal Counsel",
        "Data Privacy Officer",
        "Risk Management Officer",
        "Executive Sponsor"
    ]

    with st.form("add_raci_team_members"):
        st.markdown("**Fill in details for each RACI role:**")

        for role in raci_roles:
            st.markdown(f"**{role}**")
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input(
                    f"Name for {role}",
                    value=st.session_state.raci_team_members.get(role, {}).get("name", ""),
                    key=f"name_{role}",
                    placeholder="e.g., John Doe"
                )
            with col2:
                email = st.text_input(
                    f"Email for {role}",
                    value=st.session_state.raci_team_members.get(role, {}).get("email", ""),
                    key=f"email_{role}",
                    placeholder="john.doe@example.com"
                )

            # Store temporarily during form interaction
            if role not in st.session_state.raci_team_members:
                st.session_state.raci_team_members[role] = {}
            if name or email:
                st.session_state.raci_team_members[role] = {"name": name, "email": email}

        if st.form_submit_button("💾 Save Team Members", type="primary"):
            # Update all roles with form data
            saved_count = 0
            for role in raci_roles:
                name = st.session_state.get(f"name_{role}", "")
                email = st.session_state.get(f"email_{role}", "")
                if name or email:
                    st.session_state.raci_team_members[role] = {"name": name, "email": email}
                    saved_count += 1

            if saved_count > 0:
                st.success(f"✅ Saved team member details for {saved_count} role(s)")
                # Save project
                st.session_state.storage_manager.save_project(project)
                st.rerun()
            else:
                st.warning("Please enter at least one team member")

    # Display current team members summary
    if st.session_state.raci_team_members:
        st.markdown("#### Current RACI Team:")
        assigned_roles = {role: info for role, info in st.session_state.raci_team_members.items() if info.get("name") or info.get("email")}
        if assigned_roles:
            for role, info in assigned_roles.items():
                name = info.get("name", "Not assigned")
                email = info.get("email", "No email")
                st.markdown(f"**{role}**: {name} ({email})")

    # RACI Matrix
    st.markdown("---")
    st.markdown("### 📊 Draft RACI Matrix for AI Compliance")

    # Define the draft RACI matrix structure
    raci_matrix_data = [
        {"phase": "Project Initiation Phase", "tasks": [
            {"task": "Define project scope and AI use case", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "I", "Compliance Officer / Legal Counsel": "C", "Data Privacy Officer": "C", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Identify relevant AI regulations (e.g., EU AI Act, data privacy laws)", "roles": {"AI Product Manager": "I", "Data Scientist": "I", "Software Engineer": "I", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "A", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Conduct initial risk assessment and impact analysis", "roles": {"AI Product Manager": "A", "Data Scientist": "C", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "C", "Data Privacy Officer": "R", "Risk Management Officer": "A", "Executive Sponsor": "I"}},
            {"task": "Define ethical principles and guidelines for the project", "roles": {"AI Product Manager": "A", "Data Scientist": "C", "Software Engineer": "C", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "C", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
        ]},
        {"phase": "Data Management Phase", "tasks": [
            {"task": "Data collection and acquisition (ensuring legal basis)", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "I", "Compliance Officer / Legal Counsel": "C", "Data Privacy Officer": "R", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Data anonymization and de-identification", "roles": {"AI Product Manager": "I", "Data Scientist": "R", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "I", "Data Privacy Officer": "A", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Data quality and bias assessment", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "C", "Compliance Officer / Legal Counsel": "I", "Data Privacy Officer": "C", "Risk Management Officer": "R", "Executive Sponsor": "I"}},
            {"task": "Data documentation and lineage tracking", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "C", "Data Privacy Officer": "C", "Risk Management Officer": "R", "Executive Sponsor": "I"}},
        ]},
        {"phase": "Model Development Phase", "tasks": [
            {"task": "Model training and testing", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "I", "Data Privacy Officer": "I", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Model validation (performance, fairness, robustness)", "roles": {"AI Product Manager": "A", "Data Scientist": "C", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "C", "Data Privacy Officer": "C", "Risk Management Officer": "R", "Executive Sponsor": "I"}},
            {"task": "Documentation of model methodology and decisions", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "C", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "I", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Peer review and internal audit of the model", "roles": {"AI Product Manager": "I", "Data Scientist": "C", "Software Engineer": "I", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "C", "Risk Management Officer": "A", "Executive Sponsor": "I"}},
        ]},
        {"phase": "Deployment & Operations Phase", "tasks": [
            {"task": "Model deployment to production environment", "roles": {"AI Product Manager": "A", "Data Scientist": "I", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "I", "Data Privacy Officer": "I", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Continuous monitoring of model performance and compliance", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "C", "Risk Management Officer": "A", "Executive Sponsor": "I"}},
            {"task": "Incident response plan for model failure or bias incidents", "roles": {"AI Product Manager": "A", "Data Scientist": "C", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "C", "Data Privacy Officer": "R", "Risk Management Officer": "A", "Executive Sponsor": "I"}},
            {"task": "Regulatory reporting and external audits", "roles": {"AI Product Manager": "I", "Data Scientist": "I", "Software Engineer": "I", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "A", "Risk Management Officer": "C", "Executive Sponsor": "A"}},
        ]},
        {"phase": "In-Live Monitoring Phase", "tasks": [
            {"task": "Establish real-time performance and drift monitoring", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "C", "Data Privacy Officer": "I", "Risk Management Officer": "A", "Executive Sponsor": "I"}},
            {"task": "Implement human-in-the-loop/oversight protocols", "roles": {"AI Product Manager": "A", "Data Scientist": "I", "Software Engineer": "C", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "C", "Risk Management Officer": "A", "Executive Sponsor": "I"}},
            {"task": "Monitor adherence to model explainability requirements", "roles": {"AI Product Manager": "A", "Data Scientist": "R", "Software Engineer": "I", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "C", "Risk Management Officer": "C", "Executive Sponsor": "I"}},
            {"task": "Trigger alerts for potential compliance breaches/bias incidents", "roles": {"AI Product Manager": "A", "Data Scientist": "C", "Software Engineer": "R", "Compliance Officer / Legal Counsel": "R", "Data Privacy Officer": "C", "Risk Management Officer": "A", "Executive Sponsor": "I"}},
        ]},
    ]

    # Display RACI matrix by phase
    for phase_data in raci_matrix_data:
        with st.expander(f"📋 {phase_data['phase']}", expanded=True):
            # Create header row
            roles = ["AI Product Manager", "Data Scientist", "Software Engineer", "Compliance Officer / Legal Counsel", "Data Privacy Officer", "Risk Management Officer", "Executive Sponsor"]

            # Display as a table
            for task_data in phase_data['tasks']:
                st.markdown(f"**{task_data['task']}**")

                cols = st.columns(len(roles))
                for idx, role in enumerate(roles):
                    with cols[idx]:
                        raci_value = task_data['roles'].get(role, "")
                        color = {"R": "🔵", "A": "🟢", "C": "🟡", "I": "⚪"}.get(raci_value, "")
                        st.markdown(f"<div style='text-align: center'><small>{role}</small><br/><b style='font-size: 1.5em'>{color} {raci_value}</b></div>", unsafe_allow_html=True)

                st.markdown("---")


def show_neom_evidence_view(project: NEOMProject):
    """Show collected evidence"""
    st.markdown("### Collected Evidence")

    if not project.evidence:
        st.info("No evidence collected yet. Evidence will appear here as you complete steps.")
        return

    # Group evidence by phase
    phase_names = {
        PhaseType.PLANNING_DESIGN: "Phase 1: Planning & Design",
        PhaseType.DATA_PREPARATION: "Phase 2: Data Preparation",
        PhaseType.BUILD_VALIDATE: "Phase 3: Build & Validate",
        PhaseType.DEPLOYMENT_MONITORING: "Phase 4: Deployment & Monitoring"
    }

    for phase_type, phase_name in phase_names.items():
        phase_evidence = [e for e in project.evidence if e.phase == phase_type]

        if phase_evidence:
            st.markdown(f"#### {phase_name}")

            for evidence in phase_evidence:
                with st.expander(f"📄 {evidence.evidence_type.value} - {evidence.id[:8]}"):
                    st.markdown(f"**Type:** {evidence.evidence_type.value}")
                    st.markdown(f"**Step ID:** {evidence.step_id}")

                    # Show questions and answers
                    if evidence.questions and evidence.answers:
                        st.markdown("**Questions & Answers:**")
                        for question, desc in evidence.questions.items():
                            st.markdown(f"**Q:** {question}")
                            if question in evidence.answers:
                                st.markdown(f"**A:** {evidence.answers[question]}")
                            st.markdown("---")

                    if evidence.file_path:
                        st.markdown(f"**File:** {evidence.file_path}")

                    if evidence.signed_by:
                        st.markdown(f"**Signed by:** {evidence.signed_by}")

                    st.markdown(f"**Created:** {evidence.created_at}")


def show_neom_pitstops_view(project: NEOMProject):
    """Show pitstop checkpoints"""
    st.markdown("### Pitstop Checkpoints")

    st.info("""
    **Pitstop meetings** are formal checkpoints between phases where the PDPO reviews progress,
    evidence, and approves moving to the next phase.
    """)

    if not project.pitstops:
        st.warning("No pitstops scheduled yet. Complete a phase to schedule a pitstop.")
        return

    for pitstop in project.pitstops:
        status_color = {
            PitstopStatus.PENDING: "🟡",
            PitstopStatus.SCHEDULED: "🔵",
            PitstopStatus.IN_REVIEW: "🟣",
            PitstopStatus.APPROVED: "✅",
            PitstopStatus.ISSUES_RAISED: "❌"
        }

        phase_names = {
            PhaseType.PLANNING_DESIGN: "Phase 1: Planning & Design",
            PhaseType.DATA_PREPARATION: "Phase 2: Data Preparation",
            PhaseType.BUILD_VALIDATE: "Phase 3: Build & Validate",
            PhaseType.DEPLOYMENT_MONITORING: "Phase 4: Deployment & Monitoring"
        }

        with st.expander(
            f"{status_color[pitstop.status]} Pitstop: {phase_names[pitstop.phase_completed]} - {pitstop.status.value}",
            expanded=pitstop.status in [PitstopStatus.PENDING, PitstopStatus.IN_REVIEW]
        ):
            st.markdown(f"**Phase Completed:** {phase_names[pitstop.phase_completed]}")
            st.markdown(f"**Status:** {pitstop.status.value}")
            st.markdown(f"**PDPO Reviewer:** {pitstop.pdpo_reviewer}")

            if pitstop.participants:
                st.markdown(f"**Participants:** {', '.join(pitstop.participants)}")

            if pitstop.scheduled_date:
                st.markdown(f"**Scheduled:** {pitstop.scheduled_date}")

            if pitstop.status == PitstopStatus.PENDING:
                col1, col2 = st.columns(2)

                with col1:
                    if st.button("✅ Approve & Continue", key=f"approve_{pitstop.id}", type="primary"):
                        pitstop.status = PitstopStatus.APPROVED
                        pitstop.approved = True
                        pitstop.approved_at = datetime.now()

                        # Send notification
                        if st.session_state.get("email_notifications_enabled"):
                            st.session_state.email_service.send_approval_notification(project, pitstop)

                        st.success("Phase approved! You can now proceed to the next phase.")
                        st.rerun()

                with col2:
                    if st.button("❌ Raise Issues", key=f"issues_{pitstop.id}"):
                        # Open issues log interface
                        st.session_state[f"show_issues_log_{pitstop.id}"] = True
                        st.rerun()

            # Issues Log Interface
            if st.session_state.get(f"show_issues_log_{pitstop.id}", False) or pitstop.status == PitstopStatus.ISSUES_RAISED:
                st.markdown("---")
                st.markdown("### 📋 Issues Log")

                # Display existing issues
                if pitstop.issues_raised:
                    st.markdown("**Current Issues:**")
                    for idx, issue in enumerate(pitstop.issues_raised):
                        col1, col2 = st.columns([5, 1])
                        with col1:
                            # Make issues editable
                            edited_issue = st.text_area(
                                f"Issue {idx + 1}",
                                value=issue,
                                key=f"edit_issue_{pitstop.id}_{idx}",
                                height=80
                            )
                            if edited_issue != issue:
                                pitstop.issues_raised[idx] = edited_issue
                                st.session_state.storage_manager.save_project(project)
                        with col2:
                            if st.button("🗑️", key=f"delete_issue_{pitstop.id}_{idx}", help="Delete issue"):
                                pitstop.issues_raised.pop(idx)
                                st.session_state.storage_manager.save_project(project)
                                st.rerun()
                    st.markdown("---")

                # Add new issue
                st.markdown("**Add New Issue:**")
                new_issue = st.text_area(
                    "Describe the issue",
                    key=f"new_issue_{pitstop.id}",
                    placeholder="Describe the issue that needs to be addressed...",
                    height=100
                )

                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("➕ Add Issue", key=f"add_issue_{pitstop.id}", type="primary"):
                        if new_issue.strip():
                            pitstop.issues_raised.append(new_issue.strip())
                            pitstop.status = PitstopStatus.ISSUES_RAISED

                            # Send notification
                            if st.session_state.get("email_notifications_enabled"):
                                st.session_state.email_service.send_issues_notification(project, pitstop)

                            st.session_state.storage_manager.save_project(project)
                            st.success("✅ Issue added!")
                            # Clear the new issue field
                            del st.session_state[f"new_issue_{pitstop.id}"]
                            st.rerun()
                        else:
                            st.error("Please enter an issue description")

                with col2:
                    if st.button("💾 Save All Changes", key=f"save_issues_{pitstop.id}"):
                        st.session_state.storage_manager.save_project(project)
                        st.success("✅ All changes saved!")

                with col3:
                    if st.button("✅ Close Issues Log", key=f"close_issues_{pitstop.id}"):
                        st.session_state[f"show_issues_log_{pitstop.id}"] = False
                        st.rerun()

            if pitstop.approval_notes:
                st.markdown("**Notes:**")
                st.text_area("", value=pitstop.approval_notes, key=f"notes_{pitstop.id}", disabled=True)


# Main app logic
def main():
    """Main application logic"""
    if st.session_state.current_page == "welcome":
        show_welcome_page()
    elif st.session_state.current_page == "setup_goal":
        show_goal_setup_page()
    elif st.session_state.current_page == "pathway":
        show_pathway_page()
    elif st.session_state.current_page == "neom_project_init":
        show_neom_project_init_page()
    elif st.session_state.current_page == "neom_pathway":
        show_neom_pathway_page()


if __name__ == "__main__":
    main()
