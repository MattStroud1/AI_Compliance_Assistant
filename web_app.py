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
from src.pathways.neom_procuring_updated import NEOMProcuringAIPathway
from src.pathways.neom_operating_updated import NEOMOperatingAIPathway
from src.pathways.neom_training_updated import NEOMTrainingPathway
from src.pathways.ropa import ROPAPathway
from src.pathways.dpia import DPIAPathway
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

    # Load all existing projects once
    existing_projects = st.session_state.storage_manager.list_all_projects()

    # Load existing project section
    st.markdown("---")
    st.markdown("### 📂 Load Existing Project")

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
        "neom_procuring": {
            "icon": "🛒",
            "title": "Procuring AI",
            "description": "Comprehensive procurement assessment for purchasing AI solutions with 7 compliance frameworks",
            "page": "neom_procuring_init",
        },
        "neom_operating": {
            "icon": "⚙️",
            "title": "Operating AI",
            "description": "Comprehensive post-market monitoring for operational AI systems with 7 compliance frameworks",
            "page": "neom_operating_init",
        },
        "ropa": {
            "icon": "📋",
            "title": "ROPA Creation",
            "description": "Step-by-step guide for creating and maintaining UK GDPR Article 30 Records of Processing Activities",
            "page": "ropa_init",
        },
        "dpia": {
            "icon": "🔒",
            "title": "DPIA Creation",
            "description": "8-step process for conducting Data Protection Impact Assessments under UK GDPR",
            "page": "dpia_init",
        },
        "neom_training": {
            "icon": "🎓",
            "title": "Training on AI",
            "description": "Comprehensive 7-chapter interactive course for learning trustworthy AI principles and compliance",
            "page": "neom_training_init",
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
    - **DPIA (Data Protection Impact Assessment)**: Conduct comprehensive DPIAs under UK GDPR with 8 structured steps across 4 phases
    - **ROPA Creation**: Create and maintain UK GDPR Article 30 Records of Processing Activities with 9 structured steps
    - **Training on AI**: Interactive 7-chapter course covering all aspects of trustworthy AI compliance
    """
    )

    # Project Dashboard Link at bottom
    if existing_projects:
        st.markdown("---")
        if st.button("📊 View All Projects Dashboard", type="primary", use_container_width=True):
            st.session_state.current_page = "project_dashboard"
            st.rerun()


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
    # Check if a Building AI project is already loaded
    if 'neom_project' in st.session_state and st.session_state.neom_project:
        project = st.session_state.neom_project
        # Verify this is actually a Building AI project by checking phase structure
        if project.phases and len(project.phases) == 4:
            # Check if phases look like Building AI phases (they should start with "Planning & Design")
            if "Planning & Design" in project.phases[0].name or (hasattr(project.phases[0], 'phase_type') and project.phases[0].phase_type.value == "planning_design"):
                st.session_state.current_page = "neom_pathway"
                st.rerun()
                return

        # Wrong project type - clear it
        st.session_state.neom_project = None

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

    # Navigation buttons instead of tabs
    if 'neom_view' not in st.session_state:
        st.session_state.neom_view = "phases"

    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📋 Phases & Steps", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "phases" else "secondary",
                    key="nav_phases_building"):
            st.session_state.neom_view = "phases"
            st.rerun()

    with col2:
        if st.button("📄 Evidence", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "evidence" else "secondary",
                    key="nav_evidence_building"):
            st.session_state.neom_view = "evidence"
            st.rerun()

    with col3:
        if st.button("🔍 Pitstops", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "pitstops" else "secondary",
                    key="nav_pitstops_building"):
            st.session_state.neom_view = "pitstops"
            st.rerun()

    st.markdown("---")

    # Show appropriate view
    if st.session_state.neom_view == "phases":
        show_neom_phases_view(project)
    elif st.session_state.neom_view == "raci":
        show_neom_raci_view(project)
    elif st.session_state.neom_view == "evidence":
        show_neom_evidence_view(project)
    elif st.session_state.neom_view == "pitstops":
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
                        for idx, item in enumerate(step.checklist_items):
                            st.checkbox(item, key=f"check_{step.id}_{idx}_{item[:20]}")

                        # Check if this is a RACI-related question
                        if "RACI" in step.title or "raci" in step.title.lower():
                            st.markdown("---")
                            st.info("💡 This question requires you to create or update the RACI matrix")
                            if st.button("📊 Go to RACI Matrix", key=f"goto_raci_{step.id}", type="primary"):
                                # Store where we came from
                                st.session_state.raci_return_step_id = step.id
                                st.session_state.raci_return_step_title = step.title
                                # Navigate to RACI view
                                st.session_state.neom_view = "raci"
                                st.rerun()
                            st.markdown("---")

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

    # Return button if we came from a specific step
    if 'raci_return_step_id' in st.session_state and 'raci_return_step_title' in st.session_state:
        st.markdown("---")
        st.markdown("---")
        if st.button(f"⬅️ Return to: {st.session_state.raci_return_step_title}",
                    type="primary", use_container_width=True, key="return_from_raci"):
            # Clear the return context
            del st.session_state.raci_return_step_id
            del st.session_state.raci_return_step_title
            # Navigate back to phases view
            st.session_state.neom_view = "phases"
            st.rerun()


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


def _identify_pathway_type(project):
    """Identify the pathway type based on phase names"""
    if not project.phases:
        return "unknown"

    # Check first phase name to identify pathway
    first_phase_name = project.phases[0].name if project.phases else ""
    num_phases = len(project.phases)

    # DPIA pathway - 4 phases starting with "Phase 1: Screening & Scoping"
    if "Phase 1: Screening & Scoping" in first_phase_name or "DPIA" in project.project_name.upper():
        return "dpia"

    # ROPA pathway - 4 phases starting with "Phase 1: Planning & Scoping"
    if "Phase 1: Planning & Scoping" in first_phase_name or "ROPA" in project.project_name.upper():
        return "ropa"

    # Procuring pathway - 7 phases starting with "Project Setup & Assessment"
    if first_phase_name == "Project Setup & Assessment" or num_phases == 7:
        if "Procuring" in project.project_name or "Procurement" in project.project_name:
            return "procuring"
        # Check if it's operating by looking at first phase name more carefully
        if first_phase_name == "Project Setup & Documentation":
            return "operating"
        return "procuring"

    # Operating pathway - 7 phases starting with "Project Setup & Documentation"
    if first_phase_name == "Project Setup & Documentation":
        return "operating"

    # AI Build pathway - 4 phases (Planning & Design, Data Preparation, Build & Validate, Deployment & Monitoring)
    if num_phases == 4 and any(p.phase_type == PhaseType.BUILD_VALIDATE for p in project.phases):
        return "building"

    return "building"  # Default to building


def _render_project_matrix(projects, pathway_name, phase_configs, target_page):
    """Render a project matrix for a specific pathway type

    Args:
        projects: List of projects for this pathway
        pathway_name: Display name for the pathway (e.g., "AI Building Projects")
        phase_configs: List of tuples (phase_name, phase_identifier) for column headers
        target_page: Page to navigate to when clicking project (e.g., "neom_pathway")
    """
    if not projects:
        return

    st.markdown(f"### {pathway_name}")
    st.markdown(f"**{len(projects)} project(s)**")
    st.markdown("---")

    # Create table header
    num_phases = len(phase_configs)
    col_widths = [3] + [2] * num_phases
    header_cols = st.columns(col_widths)

    with header_cols[0]:
        st.markdown("**Project Name**")

    for idx, (phase_name, _) in enumerate(phase_configs):
        with header_cols[idx + 1]:
            st.markdown(f"**{phase_name}**")

    st.markdown("---")

    # Process each project
    for project in projects:
        cols = st.columns(col_widths)

        with cols[0]:
            # Make project name clickable
            if st.button(f"📁 {project.project_name}",
                        key=f"proj_{pathway_name}_{project.project_id}",
                        use_container_width=True):
                st.session_state.neom_project = project
                st.session_state.current_page = target_page
                st.rerun()
            st.caption(f"{project.ai_system_name}")

        # Calculate status for each phase
        for idx, (phase_name, phase_identifier) in enumerate(phase_configs):
            # Find the phase in the project by name
            phase = next((p for p in project.phases if phase_identifier in p.name), None)

            if not phase or not phase.steps:
                # No phase or steps - red
                status_circle = "🔴"
                status_text = "Not Started"
            else:
                # Calculate completion
                total_steps = len(phase.steps)
                completed_steps = sum(1 for step in phase.steps if step.status == StepStatus.COMPLETED)
                in_progress_steps = sum(1 for step in phase.steps if step.status == StepStatus.IN_PROGRESS)

                if completed_steps == total_steps and total_steps > 0:
                    # All completed - green
                    status_circle = "🟢"
                    status_text = f"Completed ({completed_steps}/{total_steps})"
                elif completed_steps > 0 or in_progress_steps > 0:
                    # Some progress - orange
                    status_circle = "🟠"
                    status_text = f"In Progress ({completed_steps}/{total_steps})"
                else:
                    # Not started - red
                    status_circle = "🔴"
                    status_text = f"Not Started (0/{total_steps})"

            with cols[idx + 1]:
                st.markdown(f"<div style='text-align: center; font-size: 2em'>{status_circle}</div>",
                          unsafe_allow_html=True)
                st.caption(status_text)

        st.markdown("---")


def show_project_dashboard():
    """Display project dashboard with status matrix for all pathway types"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_dashboard"):
        st.session_state.current_page = "welcome"
        st.rerun()

    st.title("📊 All Projects Dashboard")
    st.markdown("Overview of all NEOM Trustworthy AI projects and their progress")

    # Load all projects
    project_list = st.session_state.storage_manager.list_all_projects()

    if not project_list:
        st.info("No projects found. Create a new project to get started!")
        return

    st.markdown(f"**Total Projects:** {len(project_list)}")
    st.markdown("🔴 Not Started | 🟠 In Progress | 🟢 Completed")
    st.markdown("---")

    # Group projects by pathway type
    projects_by_pathway = {
        "building": [],
        "procuring": [],
        "operating": [],
        "ropa": [],
        "dpia": []
    }

    for proj_info in project_list:
        project = st.session_state.storage_manager.load_project(proj_info['project_id'])
        if project:
            pathway_type = _identify_pathway_type(project)
            projects_by_pathway[pathway_type].append(project)

    # Render AI Building Projects matrix
    if projects_by_pathway["building"]:
        building_phases = [
            ("Planning & Design", "Planning"),
            ("Data Preparation", "Data Preparation"),
            ("Build & Validate", "Build"),
            ("Deployment & Monitoring", "Deployment")
        ]
        _render_project_matrix(
            projects_by_pathway["building"],
            "🏗️ AI Building Projects",
            building_phases,
            "neom_pathway"
        )
        st.markdown("<br>", unsafe_allow_html=True)

    # Render AI Procurement Projects matrix
    if projects_by_pathway["procuring"]:
        procuring_phases = [
            ("Setup", "Setup"),
            ("Privacy", "Privacy"),
            ("Security", "Security"),
            ("Fairness", "Fairness"),
            ("Explainability", "Explainability"),
            ("Technology", "Technology"),
            ("Monitoring", "Monitoring")
        ]
        _render_project_matrix(
            projects_by_pathway["procuring"],
            "🛒 AI Procurement Projects",
            procuring_phases,
            "neom_procuring_pathway"
        )
        st.markdown("<br>", unsafe_allow_html=True)

    # Render AI Operations Projects matrix
    if projects_by_pathway["operating"]:
        operating_phases = [
            ("Setup", "Setup"),
            ("Privacy", "Privacy"),
            ("Security", "Security"),
            ("Fairness", "Fairness"),
            ("Explainability", "Explainability"),
            ("Technology", "Technology"),
            ("Monitoring", "Monitoring")
        ]
        _render_project_matrix(
            projects_by_pathway["operating"],
            "⚙️ AI Operations Projects",
            operating_phases,
            "neom_operating_pathway"
        )
        st.markdown("<br>", unsafe_allow_html=True)

    # Render ROPA Projects matrix
    if projects_by_pathway["ropa"]:
        ropa_phases = [
            ("Planning", "Planning"),
            ("Data Collection", "Data Collection"),
            ("Documentation", "Documentation"),
            ("Maintenance", "Maintenance")
        ]
        _render_project_matrix(
            projects_by_pathway["ropa"],
            "📋 ROPA Projects",
            ropa_phases,
            "ropa_pathway"
        )
        st.markdown("<br>", unsafe_allow_html=True)

    # Render DPIA Projects matrix
    if projects_by_pathway["dpia"]:
        dpia_phases = [
            ("Screening", "Screening"),
            ("Consultation", "Consultation"),
            ("Risk Analysis", "Risk Analysis"),
            ("Completion", "Completion")
        ]
        _render_project_matrix(
            projects_by_pathway["dpia"],
            "🔒 DPIA Projects",
            dpia_phases,
            "dpia_pathway"
        )
        st.markdown("<br>", unsafe_allow_html=True)

    # Summary statistics
    st.markdown("---")
    st.markdown("### Summary")

    # Calculate overall statistics
    total_projects = sum(len(projects) for projects in projects_by_pathway.values())
    total_phases = 0
    completed_phases = 0
    in_progress_phases = 0
    not_started_phases = 0

    for pathway_projects in projects_by_pathway.values():
        for project in pathway_projects:
            for phase in project.phases:
                total_phases += 1
                if phase.steps:
                    total_steps = len(phase.steps)
                    completed_steps = sum(1 for step in phase.steps if step.status == StepStatus.COMPLETED)
                    in_progress_steps = sum(1 for step in phase.steps if step.status == StepStatus.IN_PROGRESS)

                    if completed_steps == total_steps and total_steps > 0:
                        completed_phases += 1
                    elif completed_steps > 0 or in_progress_steps > 0:
                        in_progress_phases += 1
                    else:
                        not_started_phases += 1
                else:
                    not_started_phases += 1

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Projects", total_projects)
    with col2:
        st.metric("Total Phases", total_phases)
    with col3:
        st.metric("🟢 Completed", completed_phases)
    with col4:
        st.metric("🟠 In Progress", in_progress_phases)
    with col5:
        st.metric("🔴 Not Started", not_started_phases)


def show_neom_procuring_init_page():
    """Display NEOM Procuring AI project initialization page"""
    # Check if a Procuring AI project is already loaded
    if 'neom_project' in st.session_state and st.session_state.neom_project:
        project = st.session_state.neom_project
        # Verify this is actually a Procuring AI project by checking phase structure
        if project.phases and len(project.phases) == 7:
            # Check if phases look like Procuring AI phases (first phase = "Project Setup & Assessment")
            if "Project Setup & Assessment" in project.phases[0].name:
                st.session_state.current_page = "neom_procuring_pathway"
                st.rerun()
                return

        # Wrong project type - clear it
        st.session_state.neom_project = None

    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_procuring_init"):
        st.session_state.current_page = "welcome"
        st.rerun()

    st.title("🛒 NEOM Procuring AI - Project Initialization")

    st.markdown("""
    ### Create Your AI Procurement Assessment

    This comprehensive pathway guides you through **7 compliance frameworks** for AI procurement:
    1. 📋 **Project Setup & Assessment** - Initial requirements and vendor evaluation
    2. 🔒 **Privacy & Data Governance** - Data protection and privacy controls
    3. 🛡️ **Security Framework** - Cybersecurity and infrastructure assessment
    4. ⚖️ **Fairness & Risk Mitigation** - Bias testing and fairness measures
    5. 💡 **Explainability Framework** - Transparency and explainability requirements
    6. 🔧 **Technology Development & Robustness** - Technical validation and testing
    7. 📊 **Post-Market Monitoring** - Ongoing monitoring and compliance

    Each framework includes detailed assessment questions for vendor evaluation.
    """)

    st.markdown("---")
    st.subheader("Project Information")

    with st.form("neom_procuring_form"):
        project_name = st.text_input(
            "Project Name *",
            placeholder="e.g., AI Chatbot Procurement Assessment",
            help="Internal name for tracking this procurement project"
        )

        ai_system_name = st.text_input(
            "AI System Name *",
            placeholder="e.g., Vendor SmartBot Solution",
            help="Name of the AI system being evaluated for procurement"
        )

        ai_system_purpose = st.text_area(
            "AI System Purpose *",
            placeholder="Describe the intended use and business requirements...",
            height=100,
            help="Clear description of what the AI system will be used for"
        )

        st.markdown("### RACI Matrix Setup")
        st.markdown("Define key stakeholders for procurement assessment")

        col1, col2 = st.columns(2)

        with col1:
            project_lead_name = st.text_input("Procurement Lead Name *")
            project_lead_email = st.text_input("Procurement Lead Email *")

        with col2:
            pdpo_name = st.text_input("PDPO Reviewer Name *")
            pdpo_email = st.text_input("PDPO Reviewer Email *")

        st.markdown("### Notification Settings")
        email_notifications = st.checkbox(
            "Enable email notifications for review checkpoints",
            value=True,
            help="Send notifications when assessment milestones are reached"
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
                # Create NEOM procurement project
                project_id = str(uuid.uuid4())

                # Create project folder structure
                st.session_state.storage_manager.create_project_folder(project_id)

                # Initialize RACI matrix
                raci_matrix = RACIMatrix(
                    project_id=project_id,
                    entries=[
                        RACIEntry(
                            task_name="Overall Procurement Assessment",
                            responsible=[project_lead_email],
                            accountable=[project_lead_email],
                            consulted=[pdpo_email],
                            informed=[]
                        )
                    ]
                )

                # Create NEOM procurement project
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

                # Initialize procurement pathway and phases
                pathway = NEOMProcuringAIPathway()
                phases = pathway.create_phases(project_id)
                neom_project.phases = phases

                # Store in session
                st.session_state.neom_project = neom_project
                st.session_state.email_notifications_enabled = email_notifications

                # Save project to storage
                st.session_state.storage_manager.save_project(neom_project)

                st.success(f"✅ Procurement project '{project_name}' created successfully!")
                st.info(f"📁 Project ID: `{project_id}`")

                st.session_state.current_page = "neom_procuring_pathway"
                st.rerun()


def show_neom_procuring_pathway_page():
    """Display NEOM Procuring AI pathway with compliance frameworks"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_procuring_pathway"):
        st.session_state.current_page = "welcome"
        st.rerun()

    project = st.session_state.neom_project

    if not project:
        st.error("No procurement project found. Please create a project first.")
        if st.button("← Back to Home"):
            st.session_state.current_page = "welcome"
            st.rerun()
        return

    # Header
    st.title(f"🛒 {project.project_name}")
    st.markdown(f"**AI System:** {project.ai_system_name}")
    st.markdown(f"**Purpose:** {project.ai_system_purpose}")

    # Navigation buttons instead of tabs
    if 'neom_view' not in st.session_state:
        st.session_state.neom_view = "phases"

    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📋 Compliance Frameworks", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "phases" else "secondary",
                    key="nav_phases_procuring"):
            st.session_state.neom_view = "phases"
            st.rerun()

    with col2:
        if st.button("📄 Evidence", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "evidence" else "secondary",
                    key="nav_evidence_procuring"):
            st.session_state.neom_view = "evidence"
            st.rerun()

    with col3:
        if st.button("🔍 Checkpoints", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "pitstops" else "secondary",
                    key="nav_pitstops_procuring"):
            st.session_state.neom_view = "pitstops"
            st.rerun()

    st.markdown("---")

    # Show appropriate view
    if st.session_state.neom_view == "phases":
        show_neom_phases_view(project)
    elif st.session_state.neom_view == "raci":
        show_neom_raci_view(project)
    elif st.session_state.neom_view == "evidence":
        show_neom_evidence_view(project)
    elif st.session_state.neom_view == "pitstops":
        show_neom_pitstops_view(project)


def show_neom_operating_init_page():
    """Display NEOM Operating AI project initialization page"""
    # Check if an Operating AI project is already loaded
    if 'neom_project' in st.session_state and st.session_state.neom_project:
        project = st.session_state.neom_project
        # Verify this is actually an Operating AI project by checking phase structure
        if project.phases and len(project.phases) == 7:
            # Check if phases look like Operating AI phases (first phase = "Project Setup & Documentation")
            if "Project Setup & Documentation" in project.phases[0].name:
                st.session_state.current_page = "neom_operating_pathway"
                st.rerun()
                return

        # Wrong project type - clear it
        st.session_state.neom_project = None

    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_operating_init"):
        st.session_state.current_page = "welcome"
        st.rerun()

    st.title("⚙️ NEOM Operating AI - Project Initialization")

    st.markdown("""
    ### Create Your AI Operations Monitoring Project

    This comprehensive pathway guides you through **7 compliance frameworks** for AI operations:
    1. 📋 **Project Setup & Documentation** - Review and update project documentation
    2. 🔒 **Privacy & Data Governance** - Monitor privacy controls and data governance
    3. 🛡️ **Security Framework** - Track security threats and mitigation measures
    4. ⚖️ **Fairness & Risk Mitigation** - Monitor fairness metrics and emerging risks
    5. 💡 **Explainability Framework** - Ensure transparency and explainability
    6. 🔧 **Technology Development & Robustness** - Monitor technical robustness and changes
    7. 📊 **Post-Market Monitoring** - Ensure ongoing compliance assessments

    Each framework includes detailed monitoring questions for operational AI systems.
    """)

    st.markdown("---")
    st.subheader("Project Information")

    with st.form("neom_operating_form"):
        project_name = st.text_input(
            "Project Name *",
            placeholder="e.g., Customer Service AI Operations Monitor",
            help="Internal name for tracking this operational AI monitoring project"
        )

        ai_system_name = st.text_input(
            "AI System Name *",
            placeholder="e.g., SmartBot Customer Assistant",
            help="Name of the operational AI system being monitored"
        )

        ai_system_purpose = st.text_area(
            "AI System Purpose *",
            placeholder="Describe the AI system's operational purpose...",
            height=100,
            help="Clear description of what the AI system does in operation"
        )

        st.markdown("### RACI Matrix Setup")
        st.markdown("Define key stakeholders for operational monitoring")

        col1, col2 = st.columns(2)

        with col1:
            project_lead_name = st.text_input("Operations Lead Name *")
            project_lead_email = st.text_input("Operations Lead Email *")

        with col2:
            pdpo_name = st.text_input("PDPO Reviewer Name *")
            pdpo_email = st.text_input("PDPO Reviewer Email *")

        st.markdown("### Notification Settings")
        email_notifications = st.checkbox(
            "Enable email notifications for monitoring milestones",
            value=True,
            help="Send notifications when monitoring checkpoints are due"
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
                # Create NEOM operating project
                project_id = str(uuid.uuid4())

                # Create project folder structure
                st.session_state.storage_manager.create_project_folder(project_id)

                # Initialize RACI matrix
                raci_matrix = RACIMatrix(
                    project_id=project_id,
                    entries=[
                        RACIEntry(
                            task_name="Overall Operations Monitoring",
                            responsible=[project_lead_email],
                            accountable=[project_lead_email],
                            consulted=[pdpo_email],
                            informed=[]
                        )
                    ]
                )

                # Create NEOM operating project
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

                # Initialize operating pathway and phases
                pathway = NEOMOperatingAIPathway()
                phases = pathway.create_phases(project_id)
                neom_project.phases = phases

                # Store in session
                st.session_state.neom_project = neom_project
                st.session_state.email_notifications_enabled = email_notifications

                # Save project to storage
                st.session_state.storage_manager.save_project(neom_project)

                st.success(f"✅ Operations monitoring project '{project_name}' created successfully!")
                st.info(f"📁 Project ID: `{project_id}`")

                st.session_state.current_page = "neom_operating_pathway"
                st.rerun()


def show_neom_operating_pathway_page():
    """Display NEOM Operating AI pathway with compliance frameworks"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_operating_pathway"):
        st.session_state.current_page = "welcome"
        st.rerun()

    project = st.session_state.neom_project

    if not project:
        st.error("No operating project found. Please create a project first.")
        if st.button("← Back to Home"):
            st.session_state.current_page = "welcome"
            st.rerun()
        return

    # Header
    st.title(f"⚙️ {project.project_name}")
    st.markdown(f"**AI System:** {project.ai_system_name}")
    st.markdown(f"**Purpose:** {project.ai_system_purpose}")

    # Navigation buttons instead of tabs
    if 'neom_view' not in st.session_state:
        st.session_state.neom_view = "phases"

    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📋 Monitoring Frameworks", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "phases" else "secondary",
                    key="nav_phases_operating"):
            st.session_state.neom_view = "phases"
            st.rerun()

    with col2:
        if st.button("📄 Evidence", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "evidence" else "secondary",
                    key="nav_evidence_operating"):
            st.session_state.neom_view = "evidence"
            st.rerun()

    with col3:
        if st.button("🔍 Checkpoints", use_container_width=True,
                    type="primary" if st.session_state.neom_view == "pitstops" else "secondary",
                    key="nav_pitstops_operating"):
            st.session_state.neom_view = "pitstops"
            st.rerun()

    st.markdown("---")

    # Show appropriate view
    if st.session_state.neom_view == "phases":
        show_neom_phases_view(project)
    elif st.session_state.neom_view == "raci":
        show_neom_raci_view(project)
    elif st.session_state.neom_view == "evidence":
        show_neom_evidence_view(project)
    elif st.session_state.neom_view == "pitstops":
        show_neom_pitstops_view(project)


def show_neom_training_init_page():
    """Display NEOM Training on AI course initialization page"""
    # Check if a training project is already loaded
    if 'neom_project' in st.session_state and st.session_state.neom_project:
        project = st.session_state.neom_project
        # Verify this is actually a training project by checking phase structure
        if project.phases and len(project.phases) == 7:
            # Check if phases look like training chapters (they should have names like "Chapter 1")
            if "Chapter" in project.phases[0].name:
                st.session_state.current_page = "neom_training_pathway"
                st.rerun()
                return

        # Wrong project type - clear it
        st.session_state.neom_project = None

    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_training_init"):
        st.session_state.current_page = "welcome"
        st.rerun()

    st.title("🎓 NEOM Training on AI - Interactive Course")

    st.markdown("""
    ### Start Your Trustworthy AI Learning Journey

    This comprehensive interactive course guides you through **7 chapters** covering all aspects of trustworthy AI:
    1. 📖 **Introduction & Overview** - Why Trustworthy AI Matters
    2. 🔒 **Data & Privacy** - Privacy by design and data governance
    3. 🛡️ **Security** - AI-specific security threats and countermeasures
    4. ⚖️ **Risk & Fairness** - Identifying biases and fairness metrics
    5. 💡 **Explainability** - Making AI decisions transparent
    6. 📝 **Technology Development Record** - Documentation requirements
    7. 📊 **Post Market Monitoring** - Ongoing compliance and monitoring

    Each chapter includes detailed content, key takeaways, and interactive learning checkpoints.
    """)

    st.markdown("---")
    st.subheader("Learner Information")

    with st.form("neom_training_form"):
        project_name = st.text_input(
            "Your Name *",
            placeholder="e.g., John Smith",
            help="Your name for tracking course progress"
        )

        ai_system_name = st.text_input(
            "Organization (Optional)",
            placeholder="e.g., NEOM Tech Division",
            help="Your organization or team (optional)"
        )

        ai_system_purpose = st.text_area(
            "Learning Goals (Optional)",
            placeholder="What do you want to learn from this course?",
            height=100,
            help="Describe what you hope to achieve by completing this course (optional)"
        )

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.form_submit_button("← Back", use_container_width=True):
                st.session_state.current_page = "welcome"
                st.rerun()

        with col2:
            submit = st.form_submit_button("Start Course →", type="primary", use_container_width=True)

        if submit:
            if not project_name:
                st.error("Please enter your name")
            else:
                # Create NEOM training "project" (learning progress tracker)
                project_id = str(uuid.uuid4())

                # Create project folder structure
                st.session_state.storage_manager.create_project_folder(project_id)

                # Initialize minimal RACI matrix (for compatibility)
                raci_matrix = RACIMatrix(
                    project_id=project_id,
                    entries=[
                        RACIEntry(
                            task_name="Course Completion",
                            responsible=[project_name],
                            accountable=[project_name],
                            consulted=[],
                            informed=[]
                        )
                    ]
                )

                # Create NEOM training project
                neom_project = NEOMProject(
                    project_id=project_id,
                    project_name=f"Training: {project_name}",
                    ai_system_name=ai_system_name or "Trustworthy AI Course",
                    ai_system_purpose=ai_system_purpose or "Learning trustworthy AI principles and compliance",
                    raci_matrix=raci_matrix,
                    phases=[],
                    evidence=[],
                    pitstops=[]
                )

                # Initialize training pathway and chapters
                pathway = NEOMTrainingPathway()
                chapters = pathway.create_chapters(project_id)
                neom_project.phases = chapters  # Store chapters as "phases" for compatibility

                # Store in session
                st.session_state.neom_project = neom_project
                st.session_state.email_notifications_enabled = False  # No emails for training

                # Save project to storage
                st.session_state.storage_manager.save_project(neom_project)

                st.success(f"✅ Welcome to the course, {project_name}!")
                st.info(f"📁 Course Progress ID: `{project_id}`")

                st.session_state.current_page = "neom_training_pathway"
                st.rerun()


def _generate_quiz_questions(chapter_idx: int, section_title: str):
    """Generate quiz questions for each training section"""
    # Quiz questions bank organized by chapter and section
    quiz_bank = {
        # Chapter 1
        (1, "Introduction & Overview - Why Trustworthy AI Matters"): [
            {
                "question": "What percentage of consumers say knowing a company's AI policies before purchasing is important?",
                "options": ["52%", "62%", "72%", "82%"],
                "correct": "72%",
                "explanation": "72% of consumers say that knowing a company's AI policies before making a purchase is important, highlighting the business value of transparent AI practices."
            },
            {
                "question": "How much faster do companies focused on data protection and AI Ethics grow on average?",
                "options": ["1.2x faster", "1.4x faster", "1.6x faster", "2.0x faster"],
                "correct": "1.6x faster",
                "explanation": "Companies that prioritize data protection and AI ethics grow 1.6x faster on average, demonstrating a clear competitive advantage."
            },
            {
                "question": "How many pages of requirements does the EU AI Act contain?",
                "options": ["46 pages", "75 pages", "123 pages", "200 pages"],
                "correct": "123 pages",
                "explanation": "The EU AI Act contains 123 pages of processes, documents, and controls that organizations must comply with."
            },
            {
                "question": "According to the bulletproof vest example, what makes an AI system truly 'work'?",
                "options": ["High accuracy on test data", "Fast inference speed", "Works reliably for all people, not just some", "Low computational cost"],
                "correct": "Works reliably for all people, not just some",
                "explanation": "For an AI system to truly 'work', it needs to do more than produce the right outcome some of the time, for some people - it must work reliably for everyone."
            },
            {
                "question": "How many pages of AI Ethics Principles does Saudi Arabia's SDAIA have?",
                "options": ["23 pages", "46 pages", "75 pages", "123 pages"],
                "correct": "46 pages",
                "explanation": "Saudi Arabia's SDAIA has published 46 pages of AI Ethics Principles that organizations must follow."
            }
        ],

        # Chapter 2 - Data & Privacy
        (2, "Data & Privacy - RACI and Governance"): [
            {
                "question": "What does RACI stand for?",
                "options": ["Responsible, Accountable, Consulted, Informed", "Reviewed, Approved, Consulted, Implemented", "Required, Assigned, Completed, Inspected", "Responsible, Assigned, Checked, Integrated"],
                "correct": "Responsible, Accountable, Consulted, Informed",
                "explanation": "RACI stands for Responsible (does the work), Accountable (ultimately answerable), Consulted (provides input), and Informed (kept updated)."
            },
            {
                "question": "According to the content, what is 'privacy by design'?",
                "options": ["Adding privacy features after development", "Building privacy protections from the ground up", "Encrypting all data at rest", "Having a DPO review the system"],
                "correct": "Building privacy protections from the ground up",
                "explanation": "Privacy by design means building privacy protections into your AI system from the ground up, rather than adding them as an afterthought."
            },
            {
                "question": "Which role must sign off on all data governance decisions in high-risk AI systems?",
                "options": ["CEO", "CTO", "Data Protection Officer (DPO)", "Legal Counsel"],
                "correct": "Data Protection Officer (DPO)",
                "explanation": "The Data Protection Officer (DPO) must review and sign off on all data governance decisions, ensuring privacy and legal compliance."
            },
            {
                "question": "What is the key difference between 'Responsible' and 'Accountable' in RACI?",
                "options": ["They mean the same thing", "Responsible does the work; Accountable is ultimately answerable", "Accountable does more work", "Responsible has higher authority"],
                "correct": "Responsible does the work; Accountable is ultimately answerable",
                "explanation": "In RACI, 'Responsible' means the person who actually does the work, while 'Accountable' is the person who is ultimately answerable for the decision or task being completed correctly."
            },
            {
                "question": "Why is specificity important in RACI assignments?",
                "options": ["It looks more professional", "It prevents costly gaps and misunderstandings", "It's required by law", "It makes the matrix larger"],
                "correct": "It prevents costly gaps and misunderstandings",
                "explanation": "Specificity in RACI assignments is crucial because vague assignments lead to gaps where critical tasks fall through the cracks, potentially causing serious compliance and privacy issues."
            }
        ],

        (2, "Data & Privacy - Sensitive Data and Legal Basis"): [
            {
                "question": "Which of the following is NOT considered a special category of sensitive personal data under GDPR?",
                "options": ["Racial or ethnic origin", "Political opinions", "Email address", "Health data"],
                "correct": "Email address",
                "explanation": "Email address is regular personal data. Special categories include racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data, health data, and data about sex life or sexual orientation."
            },
            {
                "question": "What is the most demanding legal basis for processing personal data?",
                "options": ["Contract", "Legitimate Interest", "Consent", "Legal Obligation"],
                "correct": "Consent",
                "explanation": "Consent is the most demanding legal basis because it must be freely given, specific, informed, and unambiguous. Pre-ticked boxes don't count, and users must be able to easily withdraw consent."
            },
            {
                "question": "What must you conduct before relying on legitimate interest as your legal basis?",
                "options": ["Privacy Impact Assessment", "Legitimate Interest Assessment", "Data Protection Impact Assessment", "Risk Assessment"],
                "correct": "Legitimate Interest Assessment",
                "explanation": "Before relying on legitimate interest, you must conduct a Legitimate Interest Assessment (LIA) that balances your interests against the data subject's rights and freedoms."
            },
            {
                "question": "Which type of data includes biometric data and genetic data?",
                "options": ["Regular personal data", "Special category (sensitive) data", "Anonymous data", "Aggregated data"],
                "correct": "Special category (sensitive) data",
                "explanation": "Biometric data and genetic data are classified as special categories of sensitive personal data under GDPR, requiring extra protection."
            },
            {
                "question": "What requirement makes consent the most demanding legal basis?",
                "options": ["Must be documented in writing", "Must be freely given, specific, informed, and unambiguous", "Must be renewed annually", "Must be approved by DPO"],
                "correct": "Must be freely given, specific, informed, and unambiguous",
                "explanation": "Consent must meet strict criteria: freely given (not coerced), specific (for particular purposes), informed (users understand what they're agreeing to), and unambiguous (clear affirmative action required)."
            }
        ],

        (2, "Data & Privacy - Privacy Impact Assessments (PIA)"): [
            {
                "question": "How many parts does a Privacy Impact Assessment have?",
                "options": ["3 parts", "5 parts", "7 parts", "10 parts"],
                "correct": "5 parts",
                "explanation": "A PIA has 5 parts: 1) Description of intended processing, 2) Assessment of risks, 3) Measures to address risks, 4) Safeguards and security measures, 5) Justification for processing."
            },
            {
                "question": "Which scenario definitely requires a PIA?",
                "options": ["Processing employee email addresses", "Small-scale customer surveys", "Large-scale profiling with significant effects", "Processing publicly available data"],
                "correct": "Large-scale profiling with significant effects",
                "explanation": "Large-scale profiling that has significant effects on individuals is specifically listed as high-risk processing that requires a PIA."
            },
            {
                "question": "Who must review the PIA at project pitstop meetings?",
                "options": ["Only the project lead", "The CEO", "The Data Protection Officer", "External auditors"],
                "correct": "The Data Protection Officer",
                "explanation": "The DPO must review the PIA at pitstop meetings to ensure privacy risks are properly assessed and mitigated."
            },
            {
                "question": "What type of processing activities trigger PIA requirements?",
                "options": ["All data processing", "Only international transfers", "High-risk processing activities", "Only government data"],
                "correct": "High-risk processing activities",
                "explanation": "PIAs are required for high-risk data processing activities, such as large-scale profiling, systematic monitoring, or processing special categories of data."
            },
            {
                "question": "What is the first part of a PIA?",
                "options": ["Risk assessment", "Description of intended processing", "Security measures", "Justification"],
                "correct": "Description of intended processing",
                "explanation": "The first part of a PIA is the description of intended processing, which outlines what data will be collected, how it will be used, and why."
            }
        ],

        (2, "Data & Privacy - Anonymization and Privacy Enhancing Technologies (PETs)"): [
            {
                "question": "Which PET enables insights from encrypted data without decrypting it?",
                "options": ["Synthetic Data", "Differential Privacy", "Homomorphic Encryption", "Federated Learning"],
                "correct": "Homomorphic Encryption",
                "explanation": "Homomorphic Encryption allows computations to be performed on encrypted data while preserving statistical properties, without needing to decrypt it."
            },
            {
                "question": "What is the main benefit of Federated Learning?",
                "options": ["Faster training", "Lower costs", "Data never leaves local devices", "Better accuracy"],
                "correct": "Data never leaves local devices",
                "explanation": "Federated Learning's key advantage is that data never leaves local devices - only model updates are shared, protecting privacy."
            },
            {
                "question": "What does Differential Privacy do?",
                "options": ["Encrypts sensitive fields", "Removes PII from datasets", "Adds carefully calibrated noise to protect individuals", "Creates synthetic copies of data"],
                "correct": "Adds carefully calibrated noise to protect individuals",
                "explanation": "Differential Privacy manipulates data by adding carefully calibrated noise so it no longer reflects identifiable individuals while preserving overall statistical properties."
            },
            {
                "question": "What is the main risk with data anonymization?",
                "options": ["It's too expensive", "It slows down processing", "Re-identification is possible with auxiliary data", "It requires special hardware"],
                "correct": "Re-identification is possible with auxiliary data",
                "explanation": "Even anonymized data can potentially be re-identified when combined with auxiliary information from other sources, making it critical to assess re-identification risks."
            },
            {
                "question": "What does Synthetic Data generation do?",
                "options": ["Encrypts real data", "Creates artificial data that mimics real data patterns", "Compresses data files", "Validates data quality"],
                "correct": "Creates artificial data that mimics real data patterns",
                "explanation": "Synthetic Data generation creates artificial datasets that preserve the statistical properties and patterns of real data without containing actual personal information."
            }
        ],

        # Chapter 3 - Security
        (3, "Security - Introduction to AI Security Threats"): [
            {
                "question": "Why is AI security different from traditional software security?",
                "options": ["AI uses more servers", "AI systems learn from data, creating new attack surfaces", "AI is newer technology", "AI processes more data"],
                "correct": "AI systems learn from data, creating new attack surfaces",
                "explanation": "AI systems are fundamentally different because they learn behavior from data, making them susceptible to entirely new classes of attacks that target the learning process, training data, and decision-making patterns."
            },
            {
                "question": "Which attack surface is unique to AI systems?",
                "options": ["Network vulnerabilities", "Training data poisoning", "SQL injection", "DDoS attacks"],
                "correct": "Training data poisoning",
                "explanation": "Training data poisoning is unique to AI - attackers can manipulate the model's behavior by corrupting the data it learns from, a threat that doesn't exist in traditional software."
            },
            {
                "question": "Who must both sign off on AI security measures?",
                "options": ["CEO and CTO", "CISO and DPO", "Legal and Compliance", "Dev and Ops teams"],
                "correct": "CISO and DPO",
                "explanation": "Both the CISO (Chief Information Security Officer) and DPO (Data Protection Officer) must sign off, ensuring both traditional security and AI-specific concerns are addressed."
            },
            {
                "question": "What makes AI attack surfaces more complex than traditional software?",
                "options": ["Larger codebases", "More users", "Attacks can target data, learning process, and decision patterns", "More network connections"],
                "correct": "Attacks can target data, learning process, and decision patterns",
                "explanation": "AI systems have complex attack surfaces because adversaries can attack not just the code and infrastructure, but also manipulate training data, corrupt the learning process, and exploit decision-making patterns."
            },
            {
                "question": "What is a key AI-specific security concern that doesn't exist in traditional software?",
                "options": ["Password vulnerabilities", "Model behavior manipulation through data", "Network firewall breaches", "SQL injection attacks"],
                "correct": "Model behavior manipulation through data",
                "explanation": "Unlike traditional software where behavior is explicitly programmed, AI systems learn from data, making them vulnerable to manipulation through corrupted or malicious training data."
            }
        ],

        (3, "Security - Training Data and Model Threats"): [
            {
                "question": "What is the main risk of training data leaks?",
                "options": ["Slowing down training", "Revealing model architecture", "Adversaries gain blueprints for attacking the model", "Increased storage costs"],
                "correct": "Adversaries gain blueprints for attacking the model",
                "explanation": "When training data leaks, adversaries can study patterns, edge cases, and biases to reverse-engineer the model's decision boundaries and find weaknesses."
            },
            {
                "question": "What percentage of training data needs to be poisoned to significantly alter model behavior?",
                "options": ["1%", "3%", "10%", "25%"],
                "correct": "3%",
                "explanation": "Research shows that poisoning just 3% of training data can significantly alter model behavior, making this attack particularly dangerous at scale."
            },
            {
                "question": "What is a 'BadNets' attack?",
                "options": ["Stealing model parameters", "Poisoning pre-trained models with backdoors", "DDoS on training infrastructure", "Extracting training data"],
                "correct": "Poisoning pre-trained models with backdoors",
                "explanation": "BadNets is a supply chain attack where pre-trained models are poisoned with backdoors that persist even after fine-tuning for specific applications."
            },
            {
                "question": "Why is data poisoning particularly dangerous at scale?",
                "options": ["It requires expensive infrastructure", "Only 3% poisoned data can alter behavior", "It only works on small models", "It's easy to detect"],
                "correct": "Only 3% poisoned data can alter behavior",
                "explanation": "Data poisoning is dangerous because research shows that poisoning as little as 3% of training data can significantly alter a model's behavior, and this is difficult to detect in large datasets."
            },
            {
                "question": "What happens to backdoors in BadNets attacks after fine-tuning?",
                "options": ["They are removed", "They persist even after fine-tuning", "They become stronger", "They only work on original tasks"],
                "correct": "They persist even after fine-tuning",
                "explanation": "The danger of BadNets attacks is that the backdoors embedded in pre-trained models persist even after the model is fine-tuned for specific applications, making them a serious supply chain threat."
            }
        ],

        (3, "Security - Adversarial Attacks and Inference Threats"): [
            {
                "question": "What makes adversarial examples particularly dangerous?",
                "options": ["They require insider access", "They look normal to humans but fool AI", "They crash the system", "They're expensive to create"],
                "correct": "They look normal to humans but fool AI",
                "explanation": "Adversarial examples are inputs that look normal or imperceptibly different to humans but cause AI systems to make completely wrong predictions."
            },
            {
                "question": "What is 'transferability' in the context of adversarial attacks?",
                "options": ["Attacks can be automated", "Attacks work across different models", "Attacks transfer between networks", "Models transfer attack resistance"],
                "correct": "Attacks work across different models",
                "explanation": "Transferability means adversarial examples crafted for one model often fool other similar models, even with different architectures, making attacks easier to scale."
            },
            {
                "question": "What is model inversion?",
                "options": ["Running the model backwards", "Using model outputs to reconstruct training data", "Inverting prediction confidence", "Reversing model updates"],
                "correct": "Using model outputs to reconstruct training data",
                "explanation": "Model inversion attacks use careful querying of a model's outputs to infer and potentially reconstruct information about the data it was trained on."
            },
            {
                "question": "What is the key characteristic of adversarial perturbations?",
                "options": ["They are large and obvious", "They are imperceptible to humans but change AI predictions", "They corrupt the entire input", "They require physical access"],
                "correct": "They are imperceptible to humans but change AI predictions",
                "explanation": "Adversarial perturbations are carefully crafted, tiny modifications that are imperceptible or barely noticeable to humans but cause significant changes in AI model predictions."
            },
            {
                "question": "Why is transferability a major concern for AI security?",
                "options": ["It makes attacks slower", "Attackers can fool multiple models without access to them", "It only affects old models", "It's easy to prevent"],
                "correct": "Attackers can fool multiple models without access to them",
                "explanation": "Transferability means an attacker can create adversarial examples against a surrogate model and use them to attack other models they don't have access to, making these attacks practical and scalable."
            }
        ],

        # Chapter 4 - Risk & Fairness
        (4, "Risk & Fairness - Establishing Context and Identifying Issues"): [
            {
                "question": "What are the two interwoven threads in AI systems?",
                "options": ["Performance and Accuracy", "Risk and Fairness", "Speed and Reliability", "Cost and Quality"],
                "correct": "Risk and Fairness",
                "explanation": "Risk ('What could go wrong?') and Fairness ('Could this treat people unfairly?') are two distinct but deeply connected concerns that must be addressed in parallel."
            },
            {
                "question": "Which is an example of Civil and Political Rights impact?",
                "options": ["Access to fair wages", "Healthcare availability", "Free expression and privacy", "Educational opportunities"],
                "correct": "Free expression and privacy",
                "explanation": "Civil and Political Rights include liberty, free expression, privacy, and freedom from discrimination - fundamental individual rights."
            },
            {
                "question": "Why is environmental impact considered a fairness issue?",
                "options": ["It increases costs", "It reduces performance", "Future generations bear the cost", "It slows down training"],
                "correct": "Future generations bear the cost",
                "explanation": "Environmental impact from AI's energy consumption is a fairness issue because future generations will bear the environmental costs of today's AI convenience."
            },
            {
                "question": "What does the 'Risk' thread in AI systems primarily ask?",
                "options": ["How fast can it run?", "What could go wrong?", "How much does it cost?", "How accurate is it?"],
                "correct": "What could go wrong?",
                "explanation": "The Risk thread focuses on identifying what could go wrong with the AI system, assessing potential harms and their likelihood."
            },
            {
                "question": "Which category of rights includes access to education and healthcare?",
                "options": ["Civil and Political Rights", "Economic, Social and Cultural Rights", "Environmental Rights", "Property Rights"],
                "correct": "Economic, Social and Cultural Rights",
                "explanation": "Economic, Social and Cultural Rights include access to education, healthcare, fair wages, and adequate standard of living."
            }
        ],

        (4, "Risk & Fairness - Biased Feedback Loops and Mitigation"): [
            {
                "question": "How many steps are in the bias escalation process?",
                "options": ["3 steps", "4 steps", "5 steps", "7 steps"],
                "correct": "5 steps",
                "explanation": "The bias escalation process has 5 steps: Biased Input Data → AI Decision Making → Feedback Loop → Reinforcement → Escalation."
            },
            {
                "question": "What is 'automation bias'?",
                "options": ["AI making biased decisions", "Tendency to over-trust AI recommendations", "Biased training data", "Discriminatory algorithms"],
                "correct": "Tendency to over-trust AI recommendations",
                "explanation": "Automation bias is the human tendency to over-trust AI recommendations, even when told the AI might be wrong, leading people to defer to AI inappropriately."
            },
            {
                "question": "For high-stakes decisions, what type of human oversight is required?",
                "options": ["Out-of-the-loop", "In-the-loop", "Automated", "Delayed review"],
                "correct": "In-the-loop",
                "explanation": "High-stakes decisions (hiring, lending, medical diagnoses) require human-in-the-loop (HITL) oversight where the AI recommends but humans ultimately decide."
            },
            {
                "question": "What is the third step in the bias escalation process?",
                "options": ["Biased Input Data", "AI Decision Making", "Feedback Loop", "Escalation"],
                "correct": "Feedback Loop",
                "explanation": "The bias escalation process follows: 1) Biased Input Data, 2) AI Decision Making, 3) Feedback Loop, 4) Reinforcement, 5) Escalation."
            },
            {
                "question": "Why is automation bias particularly concerning in AI systems?",
                "options": ["It makes AI slower", "People defer to AI even when it might be wrong", "It increases costs", "It makes training harder"],
                "correct": "People defer to AI even when it might be wrong",
                "explanation": "Automation bias is concerning because people tend to over-trust AI recommendations and defer to them inappropriately, even when warned the AI might be wrong, potentially amplifying errors."
            }
        ],

        (4, "Risk & Fairness - Types of Bias"): [
            {
                "question": "What is survivorship bias?",
                "options": ["Bias toward recent data", "Only seeing survivors, missing what didn't survive", "Bias from measurement errors", "Cultural bias in datasets"],
                "correct": "Only seeing survivors, missing what didn't survive",
                "explanation": "Survivorship bias occurs when you only analyze things that 'survived' some process, missing crucial information about what didn't survive to be measured."
            },
            {
                "question": "Which bias occurs when measurement processes systematically skew results?",
                "options": ["Sampling bias", "Measurement bias", "Recency bias", "Confirmation bias"],
                "correct": "Measurement bias",
                "explanation": "Measurement bias occurs when measurement methods or instruments systematically skew data, like blood pressure cuffs that give inaccurate readings for certain body sizes."
            },
            {
                "question": "What is confirmation bias in the context of AI development?",
                "options": ["Model confirms predictions", "Interpreting data to support pre-existing beliefs", "Confirming test results", "Bias in confirmation emails"],
                "correct": "Interpreting data to support pre-existing beliefs",
                "explanation": "Confirmation bias is when humans interpret data and select features in ways that support their pre-existing beliefs, affecting what goes into the model."
            },
            {
                "question": "What is sampling bias?",
                "options": ["Errors in data collection", "Training data not representative of real-world population", "Measuring the wrong variables", "Using outdated data"],
                "correct": "Training data not representative of real-world population",
                "explanation": "Sampling bias occurs when training data is not representative of the population the model will serve, leading to poor performance for under-represented groups."
            },
            {
                "question": "Why is measurement bias particularly problematic in healthcare AI?",
                "options": ["Healthcare data is expensive", "Instruments may give inaccurate readings for certain groups", "Healthcare AI is new", "Doctors don't trust AI"],
                "correct": "Instruments may give inaccurate readings for certain groups",
                "explanation": "Measurement bias in healthcare is problematic because instruments like blood pressure cuffs or pulse oximeters may systematically give less accurate readings for certain body sizes or skin tones, introducing bias into training data."
            }
        ],

        (4, "Risk & Fairness - Fairness Metrics and Thresholds"): [
            {
                "question": "What does the '80% rule' state?",
                "options": ["Models must be 80% accurate", "80% of users must be satisfied", "Selection rate for any group should be at least 80% of the highest rate", "Training data must be 80% complete"],
                "correct": "Selection rate for any group should be at least 80% of the highest rate",
                "explanation": "The 80% rule states that the selection rate for any group should be at least 80% of the rate for the highest-selected group, indicating potential discrimination if lower."
            },
            {
                "question": "What is the difference between Equal Opportunity and Equalized Odds?",
                "options": ["They're the same", "EO balances TPR only; EOdds balances TPR and FPR", "EO is stricter", "EOdds only applies to binary classification"],
                "correct": "EO balances TPR only; EOdds balances TPR and FPR",
                "explanation": "Equal Opportunity balances True Positive Rates across groups, while Equalized Odds balances both True Positive Rates AND False Positive Rates, making it more stringent."
            },
            {
                "question": "Can you simultaneously satisfy all fairness definitions?",
                "options": ["Yes, with enough data", "Yes, with the right algorithm", "No, they can be mathematically incompatible", "Only for simple models"],
                "correct": "No, they can be mathematically incompatible",
                "explanation": "In many real-world scenarios, different fairness definitions are mathematically incompatible - optimizing for one may worsen another, requiring careful choices."
            },
            {
                "question": "What does TPR stand for in fairness metrics?",
                "options": ["Total Prediction Rate", "True Positive Rate", "Training Performance Ratio", "Test Pass Rate"],
                "correct": "True Positive Rate",
                "explanation": "TPR stands for True Positive Rate, which measures the proportion of actual positive cases that are correctly identified by the model."
            },
            {
                "question": "Which fairness metric is more stringent?",
                "options": ["Demographic Parity", "Equal Opportunity", "Equalized Odds", "The 80% rule"],
                "correct": "Equalized Odds",
                "explanation": "Equalized Odds is more stringent because it requires balancing both True Positive Rates and False Positive Rates across groups, whereas Equal Opportunity only balances TPR."
            }
        ],

        # Chapter 5 - Explainability
        (5, "Explainability - Foundations and Techniques"): [
            {
                "question": "What does SHAP stand for?",
                "options": ["Systematic Hybrid Analysis Protocol", "SHapley Additive exPlanations", "Structured Hierarchical AI Processing", "Secure Hashing Algorithm Protocol"],
                "correct": "SHapley Additive exPlanations",
                "explanation": "SHAP stands for SHapley Additive exPlanations, using game theory to assign each feature a contribution to the prediction."
            },
            {
                "question": "What is the main advantage of LIME?",
                "options": ["It's faster than other methods", "It works for any model type", "It provides global explanations", "It requires no computation"],
                "correct": "It works for any model type",
                "explanation": "LIME (Local Interpretable Model-agnostic Explanations) is model-agnostic, meaning it can explain predictions from any type of model."
            },
            {
                "question": "Which technique is best for explaining computer vision models?",
                "options": ["SHAP values", "Decision trees", "Saliency maps", "Linear regression coefficients"],
                "correct": "Saliency maps",
                "explanation": "Saliency maps are visualization techniques that highlight which pixels in an image most influenced the model's prediction, ideal for computer vision."
            },
            {
                "question": "What does LIME stand for?",
                "options": ["Linear Interpretation Model Explanation", "Local Interpretable Model-agnostic Explanations", "Learning Integrated Model Evaluation", "Layered Inference Mapping Engine"],
                "correct": "Local Interpretable Model-agnostic Explanations",
                "explanation": "LIME stands for Local Interpretable Model-agnostic Explanations, a technique that explains individual predictions by fitting simple models locally."
            },
            {
                "question": "What theoretical foundation does SHAP use?",
                "options": ["Linear algebra", "Game theory", "Probability theory", "Information theory"],
                "correct": "Game theory",
                "explanation": "SHAP uses Shapley values from cooperative game theory to fairly distribute the prediction contribution among features, ensuring consistent and fair feature attributions."
            }
        ],

        (5, "Explainability - Communicating with End Users"): [
            {
                "question": "What are the two essential elements of AI explanation?",
                "options": ["Technical details and code", "How it operates generally and why it made a specific decision", "Accuracy metrics and training data", "Model architecture and parameters"],
                "correct": "How it operates generally and why it made a specific decision",
                "explanation": "Users need two things: 1) General understanding of how the AI operates, and 2) Specific explanation of why it made a particular decision about them."
            },
            {
                "question": "When must users be informed about AI-generated content?",
                "options": ["Never, it's obvious", "Only for images", "When it could be mistaken for human-created content", "Only if asked"],
                "correct": "When it could be mistaken for human-created content",
                "explanation": "Users must be informed when content is AI-generated, especially if it could be mistaken for human-created content or real imagery (deepfakes)."
            },
            {
                "question": "What must you do BEFORE deploying your AI system?",
                "options": ["Train all users", "Get regulatory approval", "Validate explanations with actual users", "Publish documentation"],
                "correct": "Validate explanations with actual users",
                "explanation": "You must validate your communication channels with actual users BEFORE deployment to ensure they truly understand how the AI works and its limitations."
            },
            {
                "question": "Why is user testing of AI explanations critical before deployment?",
                "options": ["It's required by law", "To ensure users truly understand how the AI works", "To reduce development costs", "To speed up deployment"],
                "correct": "To ensure users truly understand how the AI works",
                "explanation": "User testing is critical because what seems clear to developers may not be clear to users. You must validate that actual users understand the AI's operation and limitations before deployment."
            },
            {
                "question": "What type of content requires AI disclosure to prevent deepfake concerns?",
                "options": ["All AI content", "Only text content", "AI-generated imagery that could be mistaken for real", "Only audio content"],
                "correct": "AI-generated imagery that could be mistaken for real",
                "explanation": "AI-generated imagery that could be mistaken for real (deepfakes) must be disclosed to users to prevent deception and maintain trust."
            }
        ],

        # Chapter 6 - Technology Development Record
        (6, "Technology Development Record - Planning and Design Phase"): [
            {
                "question": "What is the main purpose of the Technology Development Record (TDR)?",
                "options": ["To store training data", "To document all decisions and changes from design through operations", "To backup model weights", "To track bugs"],
                "correct": "To document all decisions and changes from design through operations",
                "explanation": "The TDR is a comprehensive record documenting every significant decision, test, and change from initial design through operational life."
            },
            {
                "question": "Why must success criteria be defined BEFORE building the model?",
                "options": ["It's required by law", "To prevent reverse-engineering easier goals after seeing model capabilities", "To speed up training", "To reduce costs"],
                "correct": "To prevent reverse-engineering easier goals after seeing model capabilities",
                "explanation": "Defining success criteria before building prevents the temptation to set thresholds that match whatever your model achieved rather than what's actually needed."
            },
            {
                "question": "What can failure to maintain a proper TDR for high-risk AI systems in the EU result in?",
                "options": ["Warning letter", "Fines up to €35 million or 7% of global turnover", "System shutdown", "Mandatory retraining"],
                "correct": "Fines up to €35 million or 7% of global turnover",
                "explanation": "Under the EU AI Act, high-risk AI systems without proper TDRs can face fines up to €35 million or 7% of global annual turnover, whichever is higher."
            },
            {
                "question": "When should the TDR documentation begin?",
                "options": ["After deployment", "During testing", "At initial design phase", "After model training"],
                "correct": "At initial design phase",
                "explanation": "The TDR must begin at the initial design phase, documenting every significant decision, test, and change throughout the entire lifecycle from design through operations."
            },
            {
                "question": "What is the risk of defining success criteria after seeing model performance?",
                "options": ["It takes more time", "You may set easier goals to match what the model achieved", "It violates privacy rules", "It increases training costs"],
                "correct": "You may set easier goals to match what the model achieved",
                "explanation": "Defining criteria after seeing performance creates the risk of reverse-engineering easier goals that match what your model happened to achieve, rather than defining what's truly needed for the use case."
            }
        ],

        (6, "Technology Development Record - Data Preparation and Build Phases"): [
            {
                "question": "What should you do about data coverage gaps?",
                "options": ["Ignore them", "Document them explicitly", "Fill them with synthetic data", "Train anyway"],
                "correct": "Document them explicitly",
                "explanation": "You should explicitly document coverage gaps and known limitations so users can calibrate their trust appropriately. Don't pretend your data is perfect."
            },
            {
                "question": "What is the key requirement for model building documentation?",
                "options": ["Must fit on one page", "Must be technical enough that experts can reproduce it", "Must be approved by legal", "Must include all code"],
                "correct": "Must be technical enough that experts can reproduce it",
                "explanation": "Model building must be documented in sufficient detail that an independent expert could reproduce your exact model and results."
            },
            {
                "question": "What should you include in data cards?",
                "options": ["Only data size", "Provenance, composition, quality issues, known biases", "Just the file names", "Only the collection date"],
                "correct": "Provenance, composition, quality issues, known biases",
                "explanation": "Data cards should comprehensively document provenance, size and composition, collection methodology, known biases, labeling process, and quality issues."
            },
            {
                "question": "Why is documenting data coverage gaps important?",
                "options": ["It's required by law", "Users can calibrate their trust appropriately", "It speeds up training", "It reduces liability"],
                "correct": "Users can calibrate their trust appropriately",
                "explanation": "Explicitly documenting coverage gaps and limitations allows users to understand where the model may be less reliable and calibrate their trust accordingly, rather than assuming the data is comprehensive."
            },
            {
                "question": "What level of detail is required for model building documentation?",
                "options": ["High-level overview only", "Enough for experts to reproduce the exact model", "Just hyperparameters", "Only the final accuracy"],
                "correct": "Enough for experts to reproduce the exact model",
                "explanation": "Documentation must be sufficiently detailed that an independent expert could reproduce your exact model and results, ensuring transparency and reproducibility."
            }
        ],

        # Chapter 7 - Post Market Monitoring
        (7, "Post Market Monitoring - Governance and Continuous Monitoring"): [
            {
                "question": "Why do AI systems change after deployment even if the model is frozen?",
                "options": ["Hardware degradation", "User base evolution and data distribution shift", "Software bugs", "Network issues"],
                "correct": "User base evolution and data distribution shift",
                "explanation": "Even frozen models face changing conditions: user bases evolve, feedback loops emerge, the world changes, causing distribution shift and performance degradation."
            },
            {
                "question": "How many tonnes of CO2 per year might a model on 10 A100 GPUs at 60% utilization emit?",
                "options": ["1.2 tonnes", "2.5 tonnes", "4.1 tonnes", "8.3 tonnes"],
                "correct": "4.1 tonnes",
                "explanation": "According to the calculation in the content: 0.96kW × 24h × 30 days × 12 months × 0.5kg CO2/kWh ≈ 4.1 tonnes CO2/year."
            },
            {
                "question": "What triggers an investigation if Disparate Impact falls below threshold?",
                "options": ["Immediately", "After 24 hours", "After 7 days", "After 30 days"],
                "correct": "After 24 hours",
                "explanation": "According to the example, if Disparate Impact falls below 0.78 for 2 consecutive days (48 hours), it becomes critical and triggers VP escalation."
            },
            {
                "question": "What is data distribution shift?",
                "options": ["Moving data between servers", "Real-world data patterns changing over time", "Redistributing training data", "Changing data formats"],
                "correct": "Real-world data patterns changing over time",
                "explanation": "Data distribution shift occurs when the patterns in real-world data change over time, causing the distribution the model sees in production to differ from its training distribution, degrading performance."
            },
            {
                "question": "Why is continuous monitoring necessary even for frozen models?",
                "options": ["Models decay over time", "The world and user base evolve", "Hardware becomes outdated", "Regulations change"],
                "correct": "The world and user base evolve",
                "explanation": "Even if the model code is frozen, the world evolves - user bases change, feedback loops emerge, societal contexts shift - all causing the model's performance and fairness to degrade over time."
            }
        ],

        (7, "Post Market Monitoring - Assessments and Technology Development Record Updates"): [
            {
                "question": "How often should high-risk AI systems undergo periodic assessments?",
                "options": ["Monthly", "Quarterly", "Semi-annually", "Annually"],
                "correct": "Quarterly",
                "explanation": "High-risk AI systems require quarterly assessments at minimum, with a comprehensive annual review, to ensure ongoing compliance and performance."
            },
            {
                "question": "What is the target comprehension rate for UI effectiveness testing?",
                "options": ["≥60%", "≥70%", "≥80%", "≥90%"],
                "correct": "≥80%",
                "explanation": "UI assessments should target ≥80% of users correctly answering comprehension questions about how the AI works and its limitations."
            },
            {
                "question": "What must happen when you make changes to your AI system?",
                "options": ["Nothing special", "Update the TDR before deployment", "Get CEO approval", "Retrain the model"],
                "correct": "Update the TDR before deployment",
                "explanation": "All changes require updating the Technology Development Record BEFORE deployment, maintaining an accurate, current record throughout the system's lifecycle."
            },
            {
                "question": "What is included in quarterly assessments for high-risk AI systems?",
                "options": ["Only performance metrics", "Performance, fairness, security, and compliance checks", "Just user feedback", "Only technical bugs"],
                "correct": "Performance, fairness, security, and compliance checks",
                "explanation": "Quarterly assessments comprehensively evaluate performance metrics, fairness indicators, security vulnerabilities, and ongoing compliance with regulations."
            },
            {
                "question": "When must the TDR be updated?",
                "options": ["Only at deployment", "Annually", "Before deploying any changes", "After incidents occur"],
                "correct": "Before deploying any changes",
                "explanation": "The TDR must be updated BEFORE deploying any changes to the AI system, maintaining a current and accurate record throughout the entire lifecycle."
            }
        ],
    }

    # Return quiz for this section, or default questions if not found
    key = (chapter_idx, section_title)
    return quiz_bank.get(key, [
        {
            "question": "Did you understand the key concepts in this section?",
            "options": ["Yes", "Somewhat", "No", "Need to review"],
            "correct": "Yes",
            "explanation": "Make sure to review the material if you're not confident with the concepts covered."
        }
    ])


def show_neom_training_pathway_page():
    """Display NEOM Training AI pathway with 7 chapters"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_neom_training_pathway"):
        st.session_state.current_page = "welcome"
        st.rerun()

    project = st.session_state.neom_project

    if not project:
        st.error("No training course found. Please start the course first.")
        if st.button("← Back to Home"):
            st.session_state.current_page = "welcome"
            st.rerun()
        return

    # Header
    st.title(f"🎓 {project.project_name}")
    st.markdown(f"**Course:** {project.ai_system_name}")
    if project.ai_system_purpose != "Learning trustworthy AI principles and compliance":
        st.markdown(f"**Learning Goals:** {project.ai_system_purpose}")

    # Navigation buttons
    st.markdown("### Course Navigation")
    col1, col2 = st.columns([3, 1])

    with col1:
        if st.button("📚 View Chapters", key="view_chapters", use_container_width=True):
            st.session_state.neom_view = "phases"
            st.rerun()

    with col2:
        if st.button("💾 Save Progress", key="save_training"):
            st.session_state.storage_manager.save_project(project)
            st.success("✅ Progress saved!")

    st.markdown("---")

    # Progress Overview
    if project.phases:
        total_chapters = len(project.phases)
        # Chapter status is derived from steps
        completed_chapters = sum(1 for chapter in project.phases
                                if all(step.status == StepStatus.COMPLETED for step in chapter.steps))
        in_progress_chapters = sum(1 for chapter in project.phases
                                  if any(step.status == StepStatus.IN_PROGRESS for step in chapter.steps)
                                  and not all(step.status == StepStatus.COMPLETED for step in chapter.steps))

        st.markdown("### 📈 Course Progress")
        progress_pct = (completed_chapters / total_chapters * 100) if total_chapters > 0 else 0
        st.progress(progress_pct / 100)
        st.markdown(f"**{completed_chapters}** of **{total_chapters}** chapters completed ({progress_pct:.0f}%)")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ Completed", completed_chapters)
        with col2:
            st.metric("🔄 In Progress", in_progress_chapters)
        with col3:
            st.metric("📝 Not Started", total_chapters - completed_chapters - in_progress_chapters)

    st.markdown("---")

    # Show chapters
    st.markdown("### 📚 Course Chapters")

    for idx, chapter in enumerate(project.phases, 1):
        # Chapter status is derived from its steps
        if all(step.status == StepStatus.COMPLETED for step in chapter.steps):
            chapter_status = StepStatus.COMPLETED
        elif any(step.status == StepStatus.IN_PROGRESS for step in chapter.steps):
            chapter_status = StepStatus.IN_PROGRESS
        else:
            chapter_status = StepStatus.NOT_STARTED

        status_icon = {
            StepStatus.COMPLETED: "✅",
            StepStatus.IN_PROGRESS: "🔄",
            StepStatus.NOT_STARTED: "⭕"
        }.get(chapter_status, "⭕")

        with st.expander(f"{status_icon} {chapter.name}", expanded=(chapter_status == StepStatus.IN_PROGRESS)):
            st.markdown(chapter.description)

            # Show each step in the chapter
            for step in chapter.steps:
                st.markdown(f"#### {step.title}")
                st.markdown(step.description)

                # Show learning objectives
                if step.checklist_items:
                    st.markdown("**Learning Objectives:**")
                    for item in step.checklist_items:
                        st.markdown(f"- {item}")

                # Add quiz for this section
                st.markdown("---")
                st.markdown("### 📝 Knowledge Check Quiz")
                st.markdown("*Select an answer for each question to see if you're correct!*")

                # Initialize quiz state
                if f"quiz_{step.id}" not in st.session_state:
                    st.session_state[f"quiz_{step.id}"] = {"answers": {}}

                quiz_state = st.session_state[f"quiz_{step.id}"]

                # Generate quiz questions based on section content
                # Strip "Chapter X: " prefix from title for quiz lookup
                title_without_prefix = step.title.replace(f"Chapter {idx}: ", "")
                quiz_questions = _generate_quiz_questions(idx, title_without_prefix)

                # Show quiz questions with immediate feedback
                for q_idx, question in enumerate(quiz_questions):
                    st.markdown(f"**Question {q_idx + 1}:** {question['question']}")

                    # Get the current answer for this question
                    current_answer = quiz_state["answers"].get(q_idx)

                    # Display each option as a checkbox
                    for option in question['options']:
                        # Create a unique key for this checkbox
                        checkbox_key = f"quiz_{step.id}_q{q_idx}_{option}"

                        # Determine if this option is selected
                        is_selected = (current_answer == option)

                        # Create columns for checkbox and feedback
                        col1, col2 = st.columns([0.9, 0.1])

                        with col1:
                            # When checkbox is clicked, update the answer
                            if st.checkbox(option, value=is_selected, key=checkbox_key):
                                # User selected this option
                                quiz_state["answers"][q_idx] = option
                                # Uncheck other options by triggering a rerun
                                if current_answer != option:
                                    st.rerun()
                            elif is_selected:
                                # User unchecked the currently selected option
                                quiz_state["answers"][q_idx] = None
                                st.rerun()

                        with col2:
                            # Show tick or cross if this option is selected
                            if is_selected:
                                if option == question['correct']:
                                    st.markdown("✅")
                                else:
                                    st.markdown("❌")

                    # Show explanation if an answer has been selected
                    if current_answer is not None:
                        if current_answer == question['correct']:
                            st.success("Correct! " + question['explanation'])
                        else:
                            st.error(f"Incorrect. The correct answer is: **{question['correct']}**")
                            st.info(question['explanation'])

                    st.markdown("")

                # Calculate and show progress
                answered = sum(1 for q_idx in range(len(quiz_questions))
                             if quiz_state["answers"].get(q_idx) is not None)
                correct = sum(1 for q_idx, q in enumerate(quiz_questions)
                            if quiz_state["answers"].get(q_idx) == q['correct'])

                if answered > 0:
                    st.markdown(f"**Progress:** {answered}/{len(quiz_questions)} questions answered")
                    if answered == len(quiz_questions):
                        score = (correct / len(quiz_questions)) * 100
                        if score == 100:
                            st.success(f"🎉 Perfect score! You got all {len(quiz_questions)} questions correct!")
                        elif score >= 80:
                            st.success(f"🎉 Excellent! You scored {score:.0f}% ({correct}/{len(quiz_questions)})")
                        elif score >= 60:
                            st.info(f"👍 Good job! You scored {score:.0f}% ({correct}/{len(quiz_questions)})")
                        else:
                            st.warning(f"📖 You scored {score:.0f}% ({correct}/{len(quiz_questions)}). Consider reviewing the material.")

                        # Reset button
                        if st.button("Reset Quiz", key=f"reset_quiz_{step.id}"):
                            quiz_state["answers"] = {}
                            st.rerun()

                st.markdown("---")

                # Status update for each step
                col1, col2, col3 = st.columns([2, 2, 2])
                with col1:
                    if st.button("Mark as In Progress", key=f"progress_{step.id}"):
                        step.status = StepStatus.IN_PROGRESS
                        st.session_state.storage_manager.save_project(project)
                        st.rerun()

                with col2:
                    if st.button("Mark as Completed", key=f"complete_{step.id}"):
                        step.status = StepStatus.COMPLETED
                        st.session_state.storage_manager.save_project(project)
                        st.success(f"✅ {step.title} completed!")
                        st.rerun()

                with col3:
                    if st.button("Reset", key=f"reset_{step.id}"):
                        step.status = StepStatus.NOT_STARTED
                        st.session_state.storage_manager.save_project(project)
                        st.rerun()

                st.markdown("---")

    # Completion message
    if all(all(step.status == StepStatus.COMPLETED for step in chapter.steps) for chapter in project.phases):
        st.balloons()
        st.success("🎉 Congratulations! You've completed all 7 chapters of the Trustworthy AI course!")
        st.info("You now have a comprehensive understanding of AI compliance requirements and best practices.")


def show_ropa_init_page():
    """Display ROPA project initialization page"""
    # Check if a ROPA project is already loaded
    if 'neom_project' in st.session_state and st.session_state.neom_project:
        project = st.session_state.neom_project
        # Verify this is actually a ROPA project by checking phase structure
        if project.phases and len(project.phases) == 4:
            # Check if phases look like ROPA phases (they should start with "Phase 1: Planning & Scoping")
            if "Phase 1: Planning & Scoping" in project.phases[0].name or "ROPA" in project.project_name.upper():
                st.session_state.current_page = "ropa_pathway"
                st.rerun()
                return

        # Wrong project type - clear it
        st.session_state.neom_project = None

    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_ropa_init"):
        st.session_state.current_page = "welcome"
        st.rerun()

    st.title("📋 ROPA (Record of Processing Activities) - Project Initialization")

    st.markdown("""
    ### Create Your UK GDPR Article 30 Compliant ROPA

    This comprehensive pathway guides you through **9 structured steps** for creating and maintaining a Record of Processing Activities:

    **Phase 1: Planning & Scoping**
    1. 📊 **Determine ROPA Obligations** - Assess scope and legal requirements
    2. 👥 **Assign Responsibility** - Set up project team and resources

    **Phase 2: Data Collection & Mapping**
    3. 🗺️ **Map Processing Activities** - Identify all data processing across organization
    4. 📝 **Define ROPA Requirements** - Establish required fields and template
    5. 📥 **Collect Information** - Gather detailed data for each activity

    **Phase 3: Documentation & Integration**
    6. ✍️ **Document Activities** - Format and record all processing in ROPA
    7. 🔗 **Integrate Frameworks** - Link ROPA with DPIAs, notices, and agreements
    8. 🛠️ **Leverage Tools** - Set up templates and management systems

    **Phase 4: Maintenance**
    9. 🔄 **Maintain & Update** - Establish ongoing review and update processes

    Each step includes detailed guidance on **why it matters**, **what to do**, and **how to proceed**.
    """)

    st.markdown("---")
    st.subheader("Project Information")

    with st.form("ropa_form"):
        project_name = st.text_input(
            "Project Name *",
            placeholder="e.g., 2025 ROPA Creation Project",
            help="Internal name for tracking this ROPA project"
        )

        ai_system_name = st.text_input(
            "Organization Name *",
            placeholder="e.g., Acme Corporation",
            help="Your organization's legal name"
        )

        ai_system_purpose = st.text_area(
            "Project Scope *",
            placeholder="Describe the scope of this ROPA (e.g., UK operations, all processing activities)...",
            height=100,
            help="Define what this ROPA will cover"
        )

        st.markdown("### RACI Matrix Setup")
        st.markdown("Define key stakeholders for ROPA creation")

        col1, col2 = st.columns(2)

        with col1:
            project_lead_name = st.text_input("ROPA Project Lead Name *", help="Often the DPO or Privacy Officer")
            project_lead_email = st.text_input("Project Lead Email *")

        with col2:
            pdpo_name = st.text_input("DPO Name *", help="Data Protection Officer")
            pdpo_email = st.text_input("DPO Email *")

        st.markdown("### Notification Settings")
        email_notifications = st.checkbox(
            "Enable email notifications for review checkpoints",
            value=True,
            help="Send notifications when ROPA milestones are reached"
        )

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.form_submit_button("← Back", use_container_width=True):
                st.session_state.current_page = "welcome"
                st.rerun()

        with col2:
            submit = st.form_submit_button("Create ROPA Project →", type="primary", use_container_width=True)

        if submit:
            if not all([project_name, ai_system_name, ai_system_purpose,
                       project_lead_name, project_lead_email, pdpo_name, pdpo_email]):
                st.error("Please fill in all required fields marked with *")
            else:
                # Create ROPA project
                project_id = str(uuid.uuid4())

                # Create project folder structure
                st.session_state.storage_manager.create_project_folder(project_id)

                # Initialize RACI matrix
                raci_matrix = RACIMatrix(
                    project_id=project_id,
                    entries=[
                        RACIEntry(
                            task_name="ROPA Creation and Maintenance",
                            responsible=[project_lead_email],
                            accountable=[project_lead_email],
                            consulted=[pdpo_email],
                            informed=[]
                        )
                    ]
                )

                # Create ROPA project using NEOMProject structure
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

                # Generate ROPA pathway phases
                ropa_pathway = ROPAPathway()
                phases = ropa_pathway.create_phases(project_id)
                neom_project.phases = phases

                # Save project
                st.session_state.storage_manager.save_project(neom_project)

                # Store in session
                st.session_state.neom_project = neom_project

                # Send notification if enabled
                if email_notifications and 'email_service' in st.session_state:
                    try:
                        st.session_state.email_service.send_project_started_notification(
                            to_email=project_lead_email,
                            project_name=project_name,
                            ai_system_name=ai_system_name
                        )
                    except Exception as e:
                        st.warning(f"Project created but email notification failed: {str(e)}")

                st.success(f"✅ ROPA project '{project_name}' created successfully!")
                st.session_state.current_page = "ropa_pathway"
                st.rerun()


def show_ropa_pathway_page():
    """Display ROPA pathway with 9 structured steps"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_ropa_pathway"):
        st.session_state.current_page = "welcome"
        st.rerun()

    project = st.session_state.neom_project

    if not project:
        st.error("No ROPA project found. Please create a project first.")
        if st.button("← Back to Home"):
            st.session_state.current_page = "welcome"
            st.rerun()
        return

    # Header
    st.title(f"📋 {project.project_name}")
    st.markdown(f"**Organization:** {project.ai_system_name}")
    st.markdown(f"**Scope:** {project.ai_system_purpose}")

    # Navigation buttons
    st.markdown("### Navigation")
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        if st.button("📚 View All Steps", key="view_phases_ropa", use_container_width=True):
            st.session_state.neom_view = "phases"
            st.rerun()

    with col2:
        if st.button("📊 View Dashboard", key="view_dashboard_ropa", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()

    with col3:
        if st.button("💾 Save", key="save_ropa"):
            st.session_state.storage_manager.save_project(project)
            st.success("✅ Saved!")

    st.markdown("---")

    # Progress Overview
    if project.phases:
        total_steps = sum(len(phase.steps) for phase in project.phases)
        completed_steps = sum(1 for phase in project.phases
                             for step in phase.steps
                             if step.status == StepStatus.COMPLETED)

        st.markdown("### 📈 Progress Overview")
        progress_pct = (completed_steps / total_steps * 100) if total_steps > 0 else 0
        st.progress(progress_pct / 100)
        st.markdown(f"**{completed_steps}** of **{total_steps}** steps completed ({progress_pct:.0f}%)")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ Completed", completed_steps)
        with col2:
            in_progress = sum(1 for phase in project.phases
                            for step in phase.steps
                            if step.status == StepStatus.IN_PROGRESS)
            st.metric("🔄 In Progress", in_progress)
        with col3:
            not_started = total_steps - completed_steps - in_progress
            st.metric("📝 Not Started", not_started)

    st.markdown("---")

    # Show all phases and steps
    st.markdown("### 📚 ROPA Creation Steps")

    for idx, phase in enumerate(project.phases, 1):
        # Phase status
        phase_complete = all(step.status == StepStatus.COMPLETED for step in phase.steps)
        phase_in_progress = any(step.status == StepStatus.IN_PROGRESS for step in phase.steps)

        status_icon = "✅" if phase_complete else ("🔄" if phase_in_progress else "⭕")

        with st.expander(f"{status_icon} {phase.name}", expanded=phase_in_progress):
            st.markdown(phase.description)

            # Show each step
            for step in phase.steps:
                st.markdown(f"#### {step.title}")
                st.markdown(step.description)

                # Three-box layout for AI generation, model answer, and gap analysis
                st.markdown("---")
                st.markdown("### 📝 Document Your Response")

                # AI Generation button (uses documents uploaded in sidebar)
                st.markdown("**🤖 AI-Assisted Completion:**")
                st.info("💡 Upload your organization's documents using the sidebar, then click below to generate an analysis.")

                # Generate question based on step
                question = f"{step.title}: {step.description}"

                if st.button("✨ Generate Answer from Documents", key=f"rag_gen_{step.id}"):
                    if not hasattr(st.session_state, 'rag_system') or not st.session_state.rag_system:
                        st.warning("⚠️ Please upload documents using the sidebar first.")
                    else:
                        with st.spinner("Analyzing your project documents..."):
                            result = st.session_state.rag_system.answer_question(question)

                            if result["answer"] or result["guidance"]:
                                st.session_state[f"draft_answer_{step.id}"] = result["answer"]
                                st.session_state[f"draft_guidance_{step.id}"] = result["guidance"]
                                st.session_state[f"draft_gap_analysis_{step.id}"] = result["gap_analysis"]
                                st.session_state[f"draft_sources_{step.id}"] = result["sources"]
                                st.session_state[f"draft_confidence_{step.id}"] = result["confidence"]
                                st.rerun()

                st.markdown("---")

                # Top row: Current state (left) and Model answer (right)
                col1, col2 = st.columns([1, 1])

                with col1:
                    st.markdown("**Your Organization's Current State**")
                    st.markdown("*What you currently have in place (AI-generated or manually entered)*")

                    # Show AI-generated answer if available
                    if f"draft_answer_{step.id}" in st.session_state:
                        confidence = st.session_state.get(f"draft_confidence_{step.id}", 0)
                        confidence_color = "green" if confidence > 0.7 else "orange" if confidence > 0.5 else "red"
                        st.markdown(f"**AI Analysis** (Confidence: :{confidence_color}[{confidence:.0%}])")

                        # Editable answer from documents
                        edited_answer = st.text_area(
                            "Information found in your documents:",
                            value=st.session_state[f"draft_answer_{step.id}"],
                            height=250,
                            key=f"edit_answer_{step.id}",
                            help="This is what the AI found in your uploaded documents. Edit as needed."
                        )

                        # Show sources
                        if st.session_state.get(f"draft_sources_{step.id}"):
                            with st.expander("📚 View Sources"):
                                for source in st.session_state[f"draft_sources_{step.id}"]:
                                    st.markdown(f"- {source}")
                    else:
                        # Manual input if no AI answer generated yet
                        user_input = st.text_area(
                            "Describe your current state",
                            key=f"input_{step.id}",
                            height=250,
                            placeholder="Describe what your organization currently has in place for this step...\n\nOr use the 'Generate Answer from Documents' button above to auto-populate from your uploaded documents."
                        )

                with col2:
                    st.markdown("**Model Answer / Best Practice**")
                    st.markdown("*What a complete response should include*")

                    # Show AI-generated guidance if available, otherwise show checklist
                    if f"draft_guidance_{step.id}" in st.session_state:
                        guidance_text = st.session_state.get(f"draft_guidance_{step.id}", "")
                        st.text_area(
                            "Ideal answer should include:",
                            value=guidance_text,
                            height=250,
                            key=f"guidance_{step.id}",
                            disabled=True,
                            help="Guidance on what a complete answer should cover"
                        )
                    else:
                        # Display checklist items as model answer guidance
                        if step.checklist_items:
                            st.markdown("**Key requirements:**")
                            for item in step.checklist_items:
                                st.markdown(f"- {item}")

                # Bottom row: Gap analysis
                st.markdown("---")
                st.markdown("**⚠️ Gap Analysis - What's Missing**")
                st.markdown("*Identify gaps between your current state and best practice*")

                # Show AI-generated gap analysis if available
                if f"draft_gap_analysis_{step.id}" in st.session_state:
                    gap_analysis_text = st.session_state.get(f"draft_gap_analysis_{step.id}", "")
                    gap_analysis = st.text_area(
                        "Gaps and areas for improvement:",
                        value=gap_analysis_text,
                        height=150,
                        key=f"gap_analysis_{step.id}",
                        help="Review and edit the AI-identified gaps as needed"
                    )
                else:
                    gap_analysis = st.text_area(
                        "Document gaps between current state and best practice",
                        key=f"gaps_{step.id}",
                        height=150,
                        placeholder="List what needs to be addressed to meet the requirements...\n\nThis will be auto-populated when you generate an answer from your documents."
                    )

                # Status update buttons
                st.markdown("---")
                col1, col2, col3 = st.columns([2, 2, 2])
                with col1:
                    if st.button("Mark as In Progress", key=f"progress_{step.id}"):
                        step.status = StepStatus.IN_PROGRESS
                        st.session_state.storage_manager.save_project(project)
                        st.rerun()

                with col2:
                    if st.button("Mark as Completed", key=f"complete_{step.id}"):
                        step.status = StepStatus.COMPLETED
                        step.completed_at = datetime.now()

                        # Save the answers to the step for ROPA record
                        # Try AI-generated answer first, then fall back to manual input
                        if f"draft_answer_{step.id}" in st.session_state:
                            step.current_state_answer = st.session_state.get(f"edit_answer_{step.id}",
                                                                             st.session_state.get(f"draft_answer_{step.id}", ""))
                        elif f"input_{step.id}" in st.session_state:
                            step.current_state_answer = st.session_state.get(f"input_{step.id}", "")

                        # Save gap analysis
                        if f"draft_gap_analysis_{step.id}" in st.session_state:
                            step.gap_analysis_answer = st.session_state.get(f"gap_analysis_{step.id}",
                                                                            st.session_state.get(f"draft_gap_analysis_{step.id}", ""))
                        elif f"gaps_{step.id}" in st.session_state:
                            step.gap_analysis_answer = st.session_state.get(f"gaps_{step.id}", "")

                        st.session_state.storage_manager.save_project(project)
                        st.success(f"✅ {step.title} completed and saved to ROPA record!")
                        st.rerun()

                with col3:
                    if st.button("Reset", key=f"reset_{step.id}"):
                        step.status = StepStatus.NOT_STARTED
                        st.session_state.storage_manager.save_project(project)
                        st.rerun()

                st.markdown("---")

    # Completion check and ROPA Record button
    if all(all(step.status == StepStatus.COMPLETED for step in phase.steps) for phase in project.phases):
        st.balloons()
        st.success("🎉 Congratulations! You've completed all 9 steps of the ROPA creation process!")
        st.info("Your Record of Processing Activities is now complete and ready for ICO inspection.")

        st.markdown("---")
        if st.button("📄 View Complete ROPA Record", type="primary", use_container_width=True):
            st.session_state.current_page = "ropa_record_view"
            st.rerun()
    elif any(step.status == StepStatus.COMPLETED for phase in project.phases for step in phase.steps):
        # Show button if at least one step is completed
        st.markdown("---")
        st.markdown("### 📄 ROPA Record")
        completed_count = sum(1 for phase in project.phases for step in phase.steps if step.status == StepStatus.COMPLETED)
        st.info(f"You have completed {completed_count} of 9 steps. View your progress in the ROPA record.")
        if st.button("📄 View ROPA Record (In Progress)", use_container_width=True):
            st.session_state.current_page = "ropa_record_view"
            st.rerun()


def show_ropa_record_view():
    """Display the compiled ROPA record from all completed steps"""
    st.markdown("# 📄 Record of Processing Activities (ROPA)")

    # Return to pathway button at the top
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Return to Pathway", use_container_width=True):
            st.session_state.current_page = "ropa_pathway"
            st.rerun()

    # Get current project
    project = st.session_state.get('neom_project')
    if not project:
        st.error("No ROPA project found. Please start a new ROPA project.")
        return

    st.markdown("---")

    # Project metadata section
    st.markdown("## Project Information")
    metadata_col1, metadata_col2 = st.columns(2)

    with metadata_col1:
        st.markdown(f"**Organization:** {project.ai_system_name}")
        st.markdown(f"**Project Name:** {project.project_name}")
        if project.description:
            st.markdown(f"**Project Scope:** {project.description}")

    with metadata_col2:
        st.markdown(f"**Created:** {project.created_at.strftime('%d %B %Y')}")
        st.markdown(f"**Last Updated:** {project.updated_at.strftime('%d %B %Y')}")

        # Count completed steps
        total_steps = sum(len(phase.steps) for phase in project.phases)
        completed_steps = sum(1 for phase in project.phases for step in phase.steps if step.status == StepStatus.COMPLETED)
        st.markdown(f"**Completion Status:** {completed_steps} of {total_steps} steps ({int(completed_steps/total_steps*100)}%)")

    # RACI information if available
    if project.raci_matrix and project.raci_matrix.entries:
        st.markdown("### Governance")
        raci_col1, raci_col2 = st.columns(2)
        with raci_col1:
            if project.project_lead:
                st.markdown(f"**ROPA Project Lead:** {project.project_lead}")
        with raci_col2:
            if project.pdpo_contact:
                st.markdown(f"**Data Protection Officer:** {project.pdpo_contact}")

    st.markdown("---")

    # Display completed steps organized by phase
    st.markdown("## ROPA Contents")

    has_completed_steps = False

    for phase in project.phases:
        # Check if this phase has any completed steps
        phase_completed_steps = [step for step in phase.steps if step.status == StepStatus.COMPLETED]

        if phase_completed_steps:
            has_completed_steps = True

            # Phase header
            st.markdown(f"### {phase.name}")
            if phase.description:
                st.markdown(f"*{phase.description}*")
            st.markdown("")

            # Display each completed step
            for step in phase_completed_steps:
                st.markdown(f"#### {step.title}")

                # Current state answer
                if step.current_state_answer:
                    st.markdown("**Current State of Processing Activity:**")
                    st.markdown(f"> {step.current_state_answer}")
                    st.markdown("")

                # Gap analysis
                if step.gap_analysis_answer:
                    st.markdown("**Gap Analysis & Improvement Areas:**")
                    st.warning(step.gap_analysis_answer)
                    st.markdown("")

                # Completion info
                if step.completed_at:
                    st.caption(f"✅ Completed on {step.completed_at.strftime('%d %B %Y at %H:%M')}")

                # User notes if any
                if step.user_notes:
                    with st.expander("📝 Additional Notes"):
                        st.markdown(step.user_notes)

                st.markdown("---")

    if not has_completed_steps:
        st.info("No completed steps yet. Complete steps in the pathway to build your ROPA record.")

    # Export options section
    st.markdown("## Export Options")
    st.markdown("**Export formats** (coming soon):")

    export_col1, export_col2, export_col3 = st.columns(3)
    with export_col1:
        st.button("📥 Download as PDF", disabled=True, use_container_width=True)
    with export_col2:
        st.button("📥 Download as Word", disabled=True, use_container_width=True)
    with export_col3:
        st.button("📥 Download as CSV", disabled=True, use_container_width=True)

    st.caption("Export functionality will be available in a future update.")

    # Footer with return button
    st.markdown("---")
    if st.button("← Return to Pathway", key="return_bottom", type="primary", use_container_width=True):
        st.session_state.current_page = "ropa_pathway"
        st.rerun()


def show_dpia_init_page():
    """Display DPIA project initialization page"""
    # Check if a DPIA project is already loaded
    if 'neom_project' in st.session_state and st.session_state.neom_project:
        project = st.session_state.neom_project
        # Verify this is actually a DPIA project by checking phase structure
        if project.phases and len(project.phases) == 4:
            # Check if phases look like DPIA phases (they should start with "Phase 1: Screening & Scoping")
            if "Phase 1: Screening & Scoping" in project.phases[0].name or "DPIA" in project.project_name.upper():
                st.session_state.current_page = "dpia_pathway"
                st.rerun()
                return

        # Wrong project type - clear it
        st.session_state.neom_project = None

    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_dpia_init"):
        st.session_state.current_page = "welcome"
        st.rerun()

    st.title("🔒 DPIA (Data Protection Impact Assessment) - Project Initialization")

    st.markdown("""
    ### Conduct a Comprehensive DPIA under UK GDPR

    This pathway guides you through **8 structured steps** for conducting Data Protection Impact Assessments:

    **Phase 1: Screening & Scoping**
    1. 🔍 **Identify the Need** - Screen against mandatory DPIA criteria
    2. 📋 **Describe the Processing** - Document nature, scope, context, and purposes

    **Phase 2: Consultation & Assessment**
    3. 💬 **Consider Consultation** - Engage data subjects, DPO, and stakeholders
    4. ⚖️ **Assess Necessity** - Evaluate necessity and proportionality

    **Phase 3: Risk Analysis**
    5. ⚠️ **Identify Risks** - Assess likelihood and severity of privacy risks
    6. 🛡️ **Mitigating Measures** - Develop strategies to reduce or eliminate risks

    **Phase 4: Completion & Maintenance**
    7. ✅ **Sign Off** - Document outcomes and determine ICO consultation needs
    8. 🔄 **Monitor & Review** - Establish ongoing review and monitoring processes

    Each step includes detailed guidance on **why it matters**, **what to do**, and **how to proceed**.
    """)

    st.markdown("---")
    st.subheader("Project Information")

    with st.form("dpia_form"):
        project_name = st.text_input(
            "Project Name *",
            placeholder="e.g., Customer Profiling System DPIA",
            help="Internal name for tracking this DPIA"
        )

        ai_system_name = st.text_input(
            "Processing Activity / System Name *",
            placeholder="e.g., AI-powered customer recommendation engine",
            help="Name of the processing activity or system being assessed"
        )

        ai_system_purpose = st.text_area(
            "Processing Purpose & Scope *",
            placeholder="Describe what the processing will do, what data will be used, and its intended purpose...",
            height=100,
            help="Clear description of the processing activity and its objectives"
        )

        st.markdown("### DPIA Team Setup")
        st.markdown("Define key stakeholders for conducting the DPIA")

        col1, col2 = st.columns(2)

        with col1:
            project_lead_name = st.text_input("DPIA Lead Name *", help="Person responsible for conducting the DPIA")
            project_lead_email = st.text_input("DPIA Lead Email *")

        with col2:
            pdpo_name = st.text_input("DPO Name *", help="Data Protection Officer (must be consulted)")
            pdpo_email = st.text_input("DPO Email *")

        st.markdown("### Notification Settings")
        email_notifications = st.checkbox(
            "Enable email notifications for review checkpoints",
            value=True,
            help="Send notifications when DPIA milestones are reached"
        )

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.form_submit_button("← Back", use_container_width=True):
                st.session_state.current_page = "welcome"
                st.rerun()

        with col2:
            submit = st.form_submit_button("Create DPIA Project →", type="primary", use_container_width=True)

        if submit:
            if not all([project_name, ai_system_name, ai_system_purpose,
                       project_lead_name, project_lead_email, pdpo_name, pdpo_email]):
                st.error("Please fill in all required fields marked with *")
            else:
                # Create DPIA project
                project_id = str(uuid.uuid4())

                # Create project folder structure
                st.session_state.storage_manager.create_project_folder(project_id)

                # Initialize RACI matrix
                raci_matrix = RACIMatrix(
                    project_id=project_id,
                    entries=[
                        RACIEntry(
                            task_name="DPIA Conduct and Review",
                            responsible=[project_lead_email],
                            accountable=[project_lead_email],
                            consulted=[pdpo_email],
                            informed=[]
                        )
                    ]
                )

                # Create DPIA project using NEOMProject structure
                neom_project = NEOMProject(
                    project_id=project_id,
                    project_name=project_name,
                    ai_system_name=ai_system_name,
                    ai_system_purpose=ai_system_purpose,
                    raci_matrix=raci_matrix,
                    phases=[],
                    evidence=[],
                    pitstops=[],
                    project_lead=project_lead_name,
                    pdpo_contact=pdpo_name
                )

                # Generate DPIA pathway phases
                dpia_pathway = DPIAPathway()
                phases = dpia_pathway.create_phases(project_id)
                neom_project.phases = phases

                # Save project
                st.session_state.storage_manager.save_project(neom_project)

                # Store in session
                st.session_state.neom_project = neom_project

                # Send notification if enabled
                if email_notifications and 'email_service' in st.session_state:
                    try:
                        st.session_state.email_service.send_project_started_notification(
                            to_email=project_lead_email,
                            project_name=project_name,
                            ai_system_name=ai_system_name
                        )
                    except Exception as e:
                        st.warning(f"Project created but email notification failed: {str(e)}")

                st.success(f"✅ DPIA project '{project_name}' created successfully!")
                st.session_state.current_page = "dpia_pathway"
                st.rerun()


def show_dpia_pathway_page():
    """Display DPIA pathway with 8 structured steps"""
    # Return to home button
    if st.button("🏠 Return to Home Page", key="home_dpia_pathway"):
        st.session_state.current_page = "welcome"
        st.rerun()

    project = st.session_state.get('neom_project')
    if not project:
        st.error("No DPIA project found. Please create a project first.")
        if st.button("← Back to Home"):
            st.session_state.current_page = "welcome"
            st.rerun()
        return

    # Header
    st.title(f"🔒 {project.project_name}")
    st.markdown(f"**Processing Activity:** {project.ai_system_name}")
    st.markdown(f"**Purpose:** {project.ai_system_purpose}")
    st.markdown("---")

    # Progress overview
    total_steps = sum(len(phase.steps) for phase in project.phases)
    completed_steps = sum(1 for phase in project.phases for step in phase.steps if step.status == StepStatus.COMPLETED)
    progress_pct = int((completed_steps / total_steps) * 100) if total_steps > 0 else 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Steps", f"{total_steps}")
    with col2:
        st.metric("Completed", f"{completed_steps}")
    with col3:
        st.metric("Progress", f"{progress_pct}%")

    st.markdown("---")

    # Display phases and steps
    for phase_idx, phase in enumerate(project.phases):
        with st.expander(f"### {phase.name}", expanded=(phase_idx == 0)):
            st.markdown(f"*{phase.description}*")
            st.markdown("")

            for step in phase.steps:
                # Step header with status
                status_icon = {
                    StepStatus.NOT_STARTED: "⚪",
                    StepStatus.IN_PROGRESS: "🟡",
                    StepStatus.COMPLETED: "✅"
                }.get(step.status, "⚪")

                st.markdown(f"## {status_icon} {step.title}")
                st.markdown(f"**{step.description}**")

                # Display guidance
                if step.guidance:
                    with st.expander("📖 Guidance - Why, What, How"):
                        st.markdown(step.guidance)

                # Display checklist
                if step.checklist_items:
                    with st.expander("✅ Key Requirements Checklist"):
                        for item in step.checklist_items:
                            st.markdown(f"- {item}")

                st.markdown("### 📝 Document Your Response")

                # AI Generation button
                st.markdown("**🤖 AI-Assisted Completion:**")
                st.info("💡 Upload your organization's documents using the sidebar, then click below to generate an analysis.")

                question = f"{step.title}: {step.description}"

                if st.button("✨ Generate Answer from Documents", key=f"rag_gen_{step.id}"):
                    if not hasattr(st.session_state, 'rag_system') or not st.session_state.rag_system:
                        st.warning("⚠️ Please upload documents using the sidebar first.")
                    else:
                        with st.spinner("Analyzing your project documents..."):
                            result = st.session_state.rag_system.answer_question(question)

                            if result["answer"] or result["guidance"]:
                                st.session_state[f"draft_answer_{step.id}"] = result["answer"]
                                st.session_state[f"draft_guidance_{step.id}"] = result["guidance"]
                                st.session_state[f"draft_gap_analysis_{step.id}"] = result["gap_analysis"]
                                st.session_state[f"draft_sources_{step.id}"] = result["sources"]
                                st.session_state[f"draft_confidence_{step.id}"] = result["confidence"]
                                st.rerun()
                            else:
                                st.warning("⚠️ Could not generate analysis. Please check your uploaded documents.")

                # Three-box layout
                col1, col2 = st.columns(2)

                # Left box: Current State
                with col1:
                    st.markdown("**Your Organization's Current State**")
                    if f"draft_answer_{step.id}" in st.session_state:
                        confidence = st.session_state.get(f"draft_confidence_{step.id}", 0)
                        confidence_color = "green" if confidence > 0.7 else "orange" if confidence > 0.5 else "red"
                        st.markdown(f"**AI Analysis** (Confidence: :{confidence_color}[{confidence:.0%}])")

                        edited_answer = st.text_area(
                            "Information found in your documents:",
                            value=st.session_state[f"draft_answer_{step.id}"],
                            height=250,
                            key=f"edit_answer_{step.id}",
                            help="This is what the AI found in your uploaded documents. Edit as needed."
                        )

                        # Show sources
                        if st.session_state.get(f"draft_sources_{step.id}"):
                            with st.expander("📚 Sources"):
                                for source in st.session_state[f"draft_sources_{step.id}"]:
                                    st.caption(f"• {source}")
                    else:
                        st.text_area(
                            "Your current state:",
                            height=250,
                            key=f"manual_answer_{step.id}",
                            placeholder="Describe your organization's current approach to this requirement...",
                            help="Enter your response manually or use AI generation above"
                        )

                # Right box: Model Answer
                with col2:
                    st.markdown("**Model Answer / Best Practice**")
                    if f"draft_guidance_{step.id}" in st.session_state:
                        guidance_text = st.session_state.get(f"draft_guidance_{step.id}", "")
                        st.text_area(
                            "Ideal answer should include:",
                            value=guidance_text,
                            height=250,
                            disabled=True,
                            key=f"guidance_display_{step.id}"
                        )
                    else:
                        # Show checklist items as fallback
                        if step.checklist_items:
                            st.markdown("**Key requirements:**")
                            checklist_preview = step.checklist_items[:5]  # Show first 5
                            for item in checklist_preview:
                                st.markdown(f"- {item}")
                            if len(step.checklist_items) > 5:
                                st.caption(f"... and {len(step.checklist_items) - 5} more (see checklist above)")

                # Bottom box: Gap Analysis
                st.markdown("**⚠️ Gap Analysis - What's Missing**")
                if f"draft_gap_analysis_{step.id}" in st.session_state:
                    gap_analysis_text = st.session_state.get(f"draft_gap_analysis_{step.id}", "")
                    gap_analysis = st.text_area(
                        "Gaps and areas for improvement:",
                        value=gap_analysis_text,
                        height=150,
                        key=f"gap_analysis_{step.id}",
                        help="AI-identified gaps between your current state and best practice. Edit as needed."
                    )
                else:
                    gap_analysis = st.text_area(
                        "Gaps and areas for improvement:",
                        height=150,
                        key=f"manual_gaps_{step.id}",
                        placeholder="Identify what's missing or needs improvement...",
                        help="Document gaps between your current state and requirements"
                    )

                # Action buttons
                st.markdown("---")
                col1, col2 = st.columns(2)

                with col1:
                    if step.status != StepStatus.IN_PROGRESS:
                        if st.button("▶️ Mark as In Progress", key=f"start_{step.id}", use_container_width=True):
                            step.status = StepStatus.IN_PROGRESS
                            st.session_state.storage_manager.save_project(project)
                            st.rerun()

                with col2:
                    if st.button("✅ Mark as Completed", key=f"complete_{step.id}", use_container_width=True, type="primary"):
                        step.status = StepStatus.COMPLETED
                        step.completed_at = datetime.now()

                        # Save the answers to the step for DPIA record
                        if f"edit_answer_{step.id}" in st.session_state:
                            step.current_state_answer = st.session_state[f"edit_answer_{step.id}"]
                        elif f"manual_answer_{step.id}" in st.session_state:
                            step.current_state_answer = st.session_state[f"manual_answer_{step.id}"]

                        # Save gap analysis
                        if f"gap_analysis_{step.id}" in st.session_state:
                            step.gap_analysis_answer = st.session_state[f"gap_analysis_{step.id}"]
                        elif f"manual_gaps_{step.id}" in st.session_state:
                            step.gap_analysis_answer = st.session_state[f"manual_gaps_{step.id}"]

                        st.session_state.storage_manager.save_project(project)
                        st.success(f"✅ {step.title} completed and saved to DPIA record!")
                        st.rerun()

                st.markdown("---")

    # Completion check and DPIA Record button
    if all(all(step.status == StepStatus.COMPLETED for step in phase.steps) for phase in project.phases):
        st.balloons()
        st.success("🎉 Congratulations! You've completed all 8 steps of the DPIA process!")
        st.info("Your Data Protection Impact Assessment is now complete and ready for review.")

        st.markdown("---")
        if st.button("📄 View Complete DPIA Document", type="primary", use_container_width=True):
            st.session_state.current_page = "dpia_record_view"
            st.rerun()
    elif any(step.status == StepStatus.COMPLETED for phase in project.phases for step in phase.steps):
        # Show button if at least one step is completed
        st.markdown("---")
        st.markdown("### 📄 DPIA Document")
        completed_count = sum(1 for phase in project.phases for step in phase.steps if step.status == StepStatus.COMPLETED)
        st.info(f"You have completed {completed_count} of {total_steps} steps. View your progress in the DPIA document.")
        if st.button("📄 View DPIA Document (In Progress)", use_container_width=True):
            st.session_state.current_page = "dpia_record_view"
            st.rerun()


def show_dpia_record_view():
    """Display the compiled DPIA document from all completed steps"""
    st.markdown("# 🔒 Data Protection Impact Assessment (DPIA)")

    # Return to pathway button at the top
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Return to Pathway", use_container_width=True):
            st.session_state.current_page = "dpia_pathway"
            st.rerun()

    # Get current project
    project = st.session_state.get('neom_project')
    if not project:
        st.error("No DPIA project found. Please start a new DPIA project.")
        return

    st.markdown("---")

    # Project metadata section
    st.markdown("## DPIA Information")
    metadata_col1, metadata_col2 = st.columns(2)

    with metadata_col1:
        st.markdown(f"**Processing Activity:** {project.ai_system_name}")
        st.markdown(f"**Project Name:** {project.project_name}")
        if project.ai_system_purpose:
            st.markdown(f"**Purpose & Scope:** {project.ai_system_purpose}")

    with metadata_col2:
        st.markdown(f"**Created:** {project.created_at.strftime('%d %B %Y')}")
        st.markdown(f"**Last Updated:** {project.updated_at.strftime('%d %B %Y')}")

        # Count completed steps
        total_steps = sum(len(phase.steps) for phase in project.phases)
        completed_steps = sum(1 for phase in project.phases for step in phase.steps if step.status == StepStatus.COMPLETED)
        st.markdown(f"**Completion Status:** {completed_steps} of {total_steps} steps ({int(completed_steps/total_steps*100)}%)")

    # DPIA Team information
    if project.project_lead or project.pdpo_contact:
        st.markdown("### DPIA Team")
        team_col1, team_col2 = st.columns(2)
        with team_col1:
            if project.project_lead:
                st.markdown(f"**DPIA Lead:** {project.project_lead}")
        with team_col2:
            if project.pdpo_contact:
                st.markdown(f"**Data Protection Officer:** {project.pdpo_contact}")

    st.markdown("---")

    # Display completed steps organized by phase
    st.markdown("## DPIA Assessment Details")

    has_completed_steps = False

    for phase in project.phases:
        # Check if this phase has any completed steps
        phase_completed_steps = [step for step in phase.steps if step.status == StepStatus.COMPLETED]

        if phase_completed_steps:
            has_completed_steps = True

            # Phase header
            st.markdown(f"### {phase.name}")
            if phase.description:
                st.markdown(f"*{phase.description}*")
            st.markdown("")

            # Display each completed step
            for step in phase_completed_steps:
                st.markdown(f"#### {step.title}")

                # Current state answer
                if step.current_state_answer:
                    st.markdown("**Current State Assessment:**")
                    st.markdown(f"> {step.current_state_answer}")
                    st.markdown("")

                # Gap analysis
                if step.gap_analysis_answer:
                    st.markdown("**Identified Gaps & Risks:**")
                    st.warning(step.gap_analysis_answer)
                    st.markdown("")

                # Completion info
                if step.completed_at:
                    st.caption(f"✅ Completed on {step.completed_at.strftime('%d %B %Y at %H:%M')}")

                # User notes if any
                if step.user_notes:
                    with st.expander("📝 Additional Notes"):
                        st.markdown(step.user_notes)

                st.markdown("---")

    if not has_completed_steps:
        st.info("No completed steps yet. Complete steps in the pathway to build your DPIA document.")

    # Export options section
    st.markdown("## Export Options")
    st.markdown("**Export formats** (coming soon):")

    export_col1, export_col2, export_col3 = st.columns(3)
    with export_col1:
        st.button("📥 Download as PDF", disabled=True, use_container_width=True)
    with export_col2:
        st.button("📥 Download as Word", disabled=True, use_container_width=True)
    with export_col3:
        st.button("📥 Submit to ICO", disabled=True, use_container_width=True, help="For high-risk DPIAs requiring ICO consultation")

    st.caption("Export functionality will be available in a future update.")

    # Footer with return button
    st.markdown("---")
    if st.button("← Return to Pathway", key="return_bottom", type="primary", use_container_width=True):
        st.session_state.current_page = "dpia_pathway"
        st.rerun()


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
    elif st.session_state.current_page == "neom_procuring_init":
        show_neom_procuring_init_page()
    elif st.session_state.current_page == "neom_procuring_pathway":
        show_neom_procuring_pathway_page()
    elif st.session_state.current_page == "neom_operating_init":
        show_neom_operating_init_page()
    elif st.session_state.current_page == "neom_operating_pathway":
        show_neom_operating_pathway_page()
    elif st.session_state.current_page == "neom_training_init":
        show_neom_training_init_page()
    elif st.session_state.current_page == "neom_training_pathway":
        show_neom_training_pathway_page()
    elif st.session_state.current_page == "ropa_init":
        show_ropa_init_page()
    elif st.session_state.current_page == "ropa_pathway":
        show_ropa_pathway_page()
    elif st.session_state.current_page == "ropa_record_view":
        show_ropa_record_view()
    elif st.session_state.current_page == "dpia_init":
        show_dpia_init_page()
    elif st.session_state.current_page == "dpia_pathway":
        show_dpia_pathway_page()
    elif st.session_state.current_page == "dpia_record_view":
        show_dpia_record_view()
    elif st.session_state.current_page == "project_dashboard":
        show_project_dashboard()


if __name__ == "__main__":
    main()
