"""Enterprise Risk Management pathway - for construction and project risk management"""

from typing import List, Optional, Dict, Any, Tuple
import uuid
import json
from pathlib import Path

from src.models import (
    PathwayType,
    PathwayConfig,
    RegulatoryFramework,
    ERMProject,
    ERMProjectPhase,
    ProjectActivity,
    IdentifiedRisk,
    MitigatingMeasure,
    ControlMapping,
    ResidualRiskAssessment,
    RiskCategory,
    RiskSeverity,
    ControlType,
)
from src.pathways.base import BasePathway
from src.llm.openai_client import ComplianceGuidanceGenerator


# Excel reading functionality
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False


class ERMPathway(BasePathway):
    """Pathway for Enterprise Risk Management in construction/project management"""

    def get_config(self) -> PathwayConfig:
        """Get pathway configuration"""
        return PathwayConfig(
            pathway_type=PathwayType.ENTERPRISE_RISK_MANAGEMENT,
            name="Enterprise Risk Management",
            description="Comprehensive risk management for construction and project management, from planning through execution",
            icon="🏗️",
            default_steps=[
                "Step 1: Project Planning & Phase Identification",
                "Step 2: Risk Identification",
                "Step 3: Mitigating Measures Assignment",
                "Step 4: Control Mapping",
                "Step 5: Residual Risk Assessment",
            ],
            regulatory_focus=[],  # ERM is process-focused, not regulatory
        )

    def get_default_steps(self) -> List[str]:
        """Get default step titles"""
        return self.get_config().default_steps

    # ========================================================================
    # STEP 1: PROJECT PLANNING & PHASE IDENTIFICATION
    # ========================================================================

    def generate_project_plan_from_documents(
        self,
        document_contents: List[Dict[str, str]],
        rag_system: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Analyze uploaded documents to extract project phases and activities.

        Args:
            document_contents: List of dicts with 'name' and 'content'
            rag_system: Optional RAG system for advanced querying

        Returns:
            Dict with 'phases' (list of phase dicts with activities)
        """
        if not document_contents:
            # Return default construction project phases
            return self._get_default_construction_phases()

        # Combine all document content
        combined_content = "\n\n".join(
            [f"=== {doc['name']} ===\n{doc['content']}" for doc in document_contents]
        )

        # Use AI to analyze and extract project structure
        prompt = f"""
        Analyze the following project documents and extract a comprehensive project plan.

        Your task:
        1. Identify all project phases (e.g., Planning, Design, Construction, Commissioning, etc.)
        2. For each phase, list all activities - both explicitly stated and implicitly required
        3. Group activities logically under their respective phases
        4. Include typical construction project activities even if not explicitly mentioned

        Documents:
        {combined_content[:15000]}  # Limit to avoid token limits

        Return your response as a JSON object with this structure:
        {{
            "project_name": "extracted or inferred project name",
            "project_description": "brief description of the project",
            "phases": [
                {{
                    "name": "Phase Name",
                    "description": "Brief phase description",
                    "activities": [
                        {{
                            "name": "Activity name",
                            "description": "Activity description",
                            "explicit": true/false (true if explicitly mentioned in docs)
                        }}
                    ]
                }}
            ]
        }}

        Be comprehensive but realistic. Include standard construction activities.
        """

        try:
            # Use the LLM to generate the project plan
            response = self.llm_client.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert construction project manager. Analyze documents and create comprehensive project plans.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.7,
            )

            result = json.loads(response.choices[0].message.content)
            return result

        except Exception as e:
            print(f"Error generating project plan: {e}")
            # Fallback to default
            return self._get_default_construction_phases()

    def _get_default_construction_phases(self) -> Dict[str, Any]:
        """Return default construction project phases"""
        return {
            "project_name": "Construction Project",
            "project_description": "Standard construction project workflow",
            "phases": [
                {
                    "name": "Planning & Design",
                    "description": "Initial planning, feasibility studies, and design work",
                    "activities": [
                        {
                            "name": "Feasibility Study",
                            "description": "Assess project viability",
                            "explicit": False,
                        },
                        {
                            "name": "Site Selection & Survey",
                            "description": "Identify and survey construction site",
                            "explicit": False,
                        },
                        {
                            "name": "Architectural Design",
                            "description": "Create architectural plans and drawings",
                            "explicit": False,
                        },
                        {
                            "name": "Engineering Design",
                            "description": "Structural, MEP, and civil engineering",
                            "explicit": False,
                        },
                        {
                            "name": "Permit Applications",
                            "description": "Submit and obtain necessary permits",
                            "explicit": False,
                        },
                    ],
                },
                {
                    "name": "Procurement",
                    "description": "Procurement of materials, equipment, and contractors",
                    "activities": [
                        {
                            "name": "Contractor Selection",
                            "description": "Select general and subcontractors",
                            "explicit": False,
                        },
                        {
                            "name": "Material Procurement",
                            "description": "Order construction materials",
                            "explicit": False,
                        },
                        {
                            "name": "Equipment Rental/Purchase",
                            "description": "Secure necessary construction equipment",
                            "explicit": False,
                        },
                    ],
                },
                {
                    "name": "Construction",
                    "description": "Main construction phase",
                    "activities": [
                        {
                            "name": "Site Preparation",
                            "description": "Clear and prepare construction site",
                            "explicit": False,
                        },
                        {
                            "name": "Foundation Work",
                            "description": "Excavation and foundation construction",
                            "explicit": False,
                        },
                        {
                            "name": "Structural Construction",
                            "description": "Build main structure",
                            "explicit": False,
                        },
                        {
                            "name": "MEP Installation",
                            "description": "Install mechanical, electrical, and plumbing systems",
                            "explicit": False,
                        },
                        {
                            "name": "Finishes",
                            "description": "Interior and exterior finishing work",
                            "explicit": False,
                        },
                    ],
                },
                {
                    "name": "Commissioning & Handover",
                    "description": "Testing, commissioning, and project handover",
                    "activities": [
                        {
                            "name": "Systems Testing",
                            "description": "Test all building systems",
                            "explicit": False,
                        },
                        {
                            "name": "Inspections",
                            "description": "Final inspections and approvals",
                            "explicit": False,
                        },
                        {
                            "name": "Documentation",
                            "description": "Compile as-built drawings and manuals",
                            "explicit": False,
                        },
                        {
                            "name": "Client Handover",
                            "description": "Transfer to client",
                            "explicit": False,
                        },
                    ],
                },
            ],
        }

    # ========================================================================
    # STEP 2: RISK IDENTIFICATION
    # ========================================================================

    def load_risk_register(self, file_path: str) -> Optional[pd.DataFrame]:
        """
        Load the construction risk register from Excel.

        Args:
            file_path: Path to Full_Risk_Register_Construction_Focused.xlsx

        Returns:
            DataFrame with risk register, or None if error
        """
        if not PANDAS_AVAILABLE:
            print("pandas not available")
            return None

        try:
            df = pd.read_excel(file_path)
            return df
        except FileNotFoundError:
            print(f"Risk register not found at {file_path}")
            return None
        except Exception as e:
            print(f"Error loading risk register: {e}")
            return None

    def identify_risks_for_activities(
        self,
        activities: List[ProjectActivity],
        risk_register_df: Optional[pd.DataFrame] = None,
    ) -> List[IdentifiedRisk]:
        """
        Identify risks for each activity using AI and knowledge base (sequential).

        Args:
            activities: List of project activities
            risk_register_df: Risk register DataFrame (optional)

        Returns:
            List of identified risks
        """
        risks = []

        for activity in activities:
            # Use AI to identify relevant risks
            activity_risks = self._identify_risks_for_activity(
                activity, risk_register_df
            )
            risks.extend(activity_risks)

        return risks

    def identify_risks_for_activities_parallel(
        self,
        activities: List[ProjectActivity],
        risk_register_df: Optional[pd.DataFrame] = None,
        progress_callback: Optional[callable] = None,
        max_workers: int = 5,
    ) -> List[IdentifiedRisk]:
        """
        Identify risks for each activity using AI and knowledge base (parallel).

        This is much faster than sequential processing as it runs multiple
        API calls concurrently.

        Args:
            activities: List of project activities
            risk_register_df: Risk register DataFrame (optional)
            progress_callback: Optional callback function(current, total)
            max_workers: Maximum number of parallel API calls (default: 5)

        Returns:
            List of identified risks
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        risks = []
        completed = 0
        total = len(activities)

        # Function to process a single activity
        def process_activity(activity):
            return self._identify_risks_for_activity(activity, risk_register_df)

        # Process activities in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_activity = {
                executor.submit(process_activity, activity): activity
                for activity in activities
            }

            # Collect results as they complete
            for future in as_completed(future_to_activity):
                activity = future_to_activity[future]
                try:
                    activity_risks = future.result()
                    risks.extend(activity_risks)
                    completed += 1

                    # Call progress callback if provided
                    if progress_callback:
                        progress_callback(completed, total)

                    print(f"✓ Completed {activity.name}: {len(activity_risks)} risks identified")

                except Exception as e:
                    print(f"✗ Error processing {activity.name}: {e}")
                    completed += 1
                    if progress_callback:
                        progress_callback(completed, total)

        return risks

    def _identify_risks_for_activity(
        self,
        activity: ProjectActivity,
        risk_register_df: Optional[pd.DataFrame],
    ) -> List[IdentifiedRisk]:
        """Identify risks for a single activity"""

        # Build context from risk register if available
        kb_context = ""
        if risk_register_df is not None:
            # Sample 20 random risks from the register for context
            sample_risks = risk_register_df.sample(min(20, len(risk_register_df)))
            kb_context = "Reference risks from knowledge base:\n"
            for _, row in sample_risks.iterrows():
                kb_context += f"- {row.to_dict()}\n"

        prompt = f"""
        Identify potential risks for the following construction activity:

        Activity: {activity.name}
        Description: {activity.description or 'N/A'}

        {kb_context}

        Identify 3-5 significant risks for this activity. For each risk, provide:
        - A clear description of the risk
        - Category (safety, financial, schedule, quality, environmental, legal_regulatory, technical, stakeholder, resource, other)
        - Likelihood (1-5, where 1=Very Low, 5=Very High)
        - Impact (1-5, where 1=Very Low, 5=Very High)

        Return as JSON array:
        [
            {{
                "risk_description": "description",
                "category": "category",
                "likelihood": 1-5,
                "impact": 1-5
            }}
        ]
        """

        try:
            response = self.llm_client.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a construction risk management expert.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.7,
            )

            result = json.loads(response.choices[0].message.content)
            risk_list = result.get("risks", [])

            # Convert to IdentifiedRisk objects
            identified_risks = []
            for risk_data in risk_list:
                try:
                    likelihood = risk_data.get("likelihood", 3)
                    impact = risk_data.get("impact", 3)

                    risk = IdentifiedRisk(
                        id=str(uuid.uuid4()),
                        activity_id=activity.id,
                        risk_description=risk_data.get("risk_description", "Unknown risk"),
                        category=RiskCategory(risk_data.get("category", "other")),
                        likelihood=likelihood,
                        impact=impact,
                        inherent_risk_score=likelihood * impact,
                        source="ai_generated",
                    )
                    identified_risks.append(risk)
                except Exception as e:
                    print(f"Error creating risk: {e}")
                    continue

            return identified_risks

        except Exception as e:
            print(f"Error identifying risks for activity {activity.name}: {e}")
            return []

    # ========================================================================
    # STEP 3: MITIGATING MEASURES
    # ========================================================================

    def generate_mitigating_measures(
        self, risks: List[IdentifiedRisk]
    ) -> List[MitigatingMeasure]:
        """
        Generate mitigating measures for identified risks (sequential).

        Args:
            risks: List of identified risks

        Returns:
            List of mitigating measures
        """
        measures = []

        for risk in risks:
            risk_measures = self._generate_measures_for_risk(risk)
            measures.extend(risk_measures)

        return measures

    def generate_mitigating_measures_parallel(
        self,
        risks: List[IdentifiedRisk],
        progress_callback: Optional[callable] = None,
        max_workers: int = 5,
    ) -> List[MitigatingMeasure]:
        """
        Generate mitigating measures for identified risks (parallel).

        Args:
            risks: List of identified risks
            progress_callback: Optional callback function(current, total)
            max_workers: Maximum number of parallel API calls (default: 5)

        Returns:
            List of mitigating measures
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        measures = []
        completed = 0
        total = len(risks)

        def process_risk(risk):
            return self._generate_measures_for_risk(risk)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_risk = {
                executor.submit(process_risk, risk): risk
                for risk in risks
            }

            for future in as_completed(future_to_risk):
                risk = future_to_risk[future]
                try:
                    risk_measures = future.result()
                    measures.extend(risk_measures)
                    completed += 1

                    if progress_callback:
                        progress_callback(completed, total)

                    print(f"✓ Generated {len(risk_measures)} measures for risk")

                except Exception as e:
                    print(f"✗ Error generating measures: {e}")
                    completed += 1
                    if progress_callback:
                        progress_callback(completed, total)

        return measures

    def _generate_measures_for_risk(
        self, risk: IdentifiedRisk
    ) -> List[MitigatingMeasure]:
        """Generate mitigating measures for a single risk"""

        prompt = f"""
        Generate 2-3 effective mitigating measures for the following construction risk:

        Risk: {risk.risk_description}
        Category: {risk.category.value}
        Likelihood: {risk.likelihood}/5
        Impact: {risk.impact}/5
        Risk Score: {risk.inherent_risk_score}

        For each mitigation measure, provide:
        - Description of the measure
        - Suggested responsible party (role, not name)
        - Timeline for implementation
        - Effectiveness rating (1-5, how effective this measure is at reducing the risk)

        Return as JSON array:
        [
            {{
                "measure_description": "description",
                "responsible_party": "role",
                "timeline": "timeline",
                "effectiveness_rating": 1-5
            }}
        ]
        """

        try:
            response = self.llm_client.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a construction risk mitigation expert.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.7,
            )

            result = json.loads(response.choices[0].message.content)
            measures_list = result.get("measures", [])

            # Convert to MitigatingMeasure objects
            mitigating_measures = []
            for measure_data in measures_list:
                measure = MitigatingMeasure(
                    id=str(uuid.uuid4()),
                    risk_id=risk.id,
                    measure_description=measure_data.get("measure_description", ""),
                    responsible_party=measure_data.get("responsible_party"),
                    timeline=measure_data.get("timeline"),
                    effectiveness_rating=measure_data.get("effectiveness_rating", 3),
                    implementation_status="planned",
                )
                mitigating_measures.append(measure)

            return mitigating_measures

        except Exception as e:
            print(f"Error generating measures for risk {risk.id}: {e}")
            return []

    # ========================================================================
    # STEP 4: CONTROL MAPPING
    # ========================================================================

    def load_controls_knowledge_base(self, file_path: str) -> Optional[pd.DataFrame]:
        """
        Load the GRC Controls Knowledge Base from Excel.

        Args:
            file_path: Path to GRC Controls Knowledge_Base.xlsx

        Returns:
            DataFrame with controls, or None if error
        """
        if not PANDAS_AVAILABLE:
            print("pandas not available")
            return None

        try:
            df = pd.read_excel(file_path)
            return df
        except FileNotFoundError:
            print(f"Controls KB not found at {file_path}")
            return None
        except Exception as e:
            print(f"Error loading controls KB: {e}")
            return None

    def map_controls_to_risks(
        self,
        risks: List[IdentifiedRisk],
        mitigations: List[MitigatingMeasure],
        controls_kb_df: Optional[pd.DataFrame] = None,
    ) -> List[ControlMapping]:
        """
        Map controls from knowledge base to mitigated risks (sequential).

        Args:
            risks: List of identified risks
            mitigations: List of mitigating measures
            controls_kb_df: Controls knowledge base DataFrame (optional)

        Returns:
            List of control mappings
        """
        control_mappings = []

        for risk in risks:
            # Find mitigations for this risk
            risk_mitigations = [m for m in mitigations if m.risk_id == risk.id]

            for mitigation in risk_mitigations:
                # Map controls to this risk/mitigation pair
                controls = self._map_controls_for_mitigation(
                    risk, mitigation, controls_kb_df
                )
                control_mappings.extend(controls)

        return control_mappings

    def map_controls_to_risks_parallel(
        self,
        risks: List[IdentifiedRisk],
        mitigations: List[MitigatingMeasure],
        controls_kb_df: Optional[pd.DataFrame] = None,
        progress_callback: Optional[callable] = None,
        max_workers: int = 5,
    ) -> List[ControlMapping]:
        """
        Map controls from knowledge base to mitigated risks (parallel).

        Args:
            risks: List of identified risks
            mitigations: List of mitigating measures
            controls_kb_df: Controls knowledge base DataFrame (optional)
            progress_callback: Optional callback function(current, total)
            max_workers: Maximum number of parallel API calls (default: 5)

        Returns:
            List of control mappings
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        control_mappings = []
        tasks = []

        # Create task list: (risk, mitigation) pairs
        for risk in risks:
            risk_mitigations = [m for m in mitigations if m.risk_id == risk.id]
            for mitigation in risk_mitigations:
                tasks.append((risk, mitigation))

        completed = 0
        total = len(tasks)

        def process_risk_mitigation(risk, mitigation):
            return self._map_controls_for_mitigation(risk, mitigation, controls_kb_df)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_task = {
                executor.submit(process_risk_mitigation, risk, mitigation): (risk, mitigation)
                for risk, mitigation in tasks
            }

            for future in as_completed(future_to_task):
                risk, mitigation = future_to_task[future]
                try:
                    controls = future.result()
                    control_mappings.extend(controls)
                    completed += 1

                    if progress_callback:
                        progress_callback(completed, total)

                    print(f"✓ Mapped {len(controls)} controls for risk/mitigation pair")

                except Exception as e:
                    print(f"✗ Error mapping controls: {e}")
                    completed += 1
                    if progress_callback:
                        progress_callback(completed, total)

        return control_mappings

    def _map_controls_for_mitigation(
        self,
        risk: IdentifiedRisk,
        mitigation: MitigatingMeasure,
        controls_kb_df: Optional[pd.DataFrame],
    ) -> List[ControlMapping]:
        """Map controls for a specific risk/mitigation pair"""

        # Build context from controls KB if available
        kb_context = ""
        if controls_kb_df is not None:
            sample_controls = controls_kb_df.sample(min(15, len(controls_kb_df)))
            kb_context = "Reference controls from knowledge base:\n"
            for _, row in sample_controls.iterrows():
                kb_context += f"- {row.to_dict()}\n"

        prompt = f"""
        Map appropriate controls for the following risk and mitigation:

        Risk: {risk.risk_description}
        Category: {risk.category.value}
        Mitigation Measure: {mitigation.measure_description}

        {kb_context}

        Identify 1-2 appropriate controls. For each control:
        - Control name
        - Control type (preventive, detective, corrective, directive)
        - Brief description
        - Frequency (e.g., Daily, Weekly, Monthly, As needed)
        - Control owner (role)

        Return as JSON array:
        [
            {{
                "control_name": "name",
                "control_type": "type",
                "control_description": "description",
                "frequency": "frequency",
                "control_owner": "role"
            }}
        ]
        """

        try:
            response = self.llm_client.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a GRC (Governance, Risk, Compliance) controls expert.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.7,
            )

            result = json.loads(response.choices[0].message.content)
            controls_list = result.get("controls", [])

            # Convert to ControlMapping objects
            control_mappings = []
            for control_data in controls_list:
                try:
                    control = ControlMapping(
                        id=str(uuid.uuid4()),
                        risk_id=risk.id,
                        mitigation_id=mitigation.id,
                        control_name=control_data.get("control_name", ""),
                        control_type=ControlType(
                            control_data.get("control_type", "preventive")
                        ),
                        control_description=control_data.get("control_description"),
                        frequency=control_data.get("frequency"),
                        control_owner=control_data.get("control_owner"),
                    )
                    control_mappings.append(control)
                except Exception as e:
                    print(f"Error creating control mapping: {e}")
                    continue

            return control_mappings

        except Exception as e:
            print(f"Error mapping controls: {e}")
            return []

    # ========================================================================
    # STEP 5: RESIDUAL RISK ASSESSMENT
    # ========================================================================

    def calculate_residual_risks(
        self,
        risks: List[IdentifiedRisk],
        mitigations: List[MitigatingMeasure],
        controls: List[ControlMapping],
    ) -> List[ResidualRiskAssessment]:
        """
        Calculate residual risk scores after mitigations and controls.

        Args:
            risks: List of identified risks
            mitigations: List of mitigating measures
            controls: List of control mappings

        Returns:
            List of residual risk assessments
        """
        residual_risks = []

        for risk in risks:
            # Find mitigations and controls for this risk
            risk_mitigations = [m for m in mitigations if m.risk_id == risk.id]
            risk_controls = [c for c in controls if c.risk_id == risk.id]

            # Calculate residual risk
            residual = self._calculate_residual_risk(
                risk, risk_mitigations, risk_controls
            )
            residual_risks.append(residual)

        return residual_risks

    def _calculate_residual_risk(
        self,
        risk: IdentifiedRisk,
        mitigations: List[MitigatingMeasure],
        controls: List[ControlMapping],
    ) -> ResidualRiskAssessment:
        """Calculate residual risk for a single risk"""

        # Average effectiveness of mitigations
        if mitigations:
            avg_mitigation_effectiveness = sum(
                m.effectiveness_rating for m in mitigations
            ) / len(mitigations)
        else:
            avg_mitigation_effectiveness = 0

        # Count and weight controls
        control_count = len(controls)
        control_effectiveness = min(control_count * 0.5, 2.5)  # Max 2.5 reduction

        # Calculate overall control effectiveness (1-5 scale)
        overall_effectiveness = min(
            int((avg_mitigation_effectiveness + control_effectiveness) / 2), 5
        )

        # Reduce likelihood and impact based on effectiveness
        reduction_factor = overall_effectiveness / 10  # 0.1 to 0.5

        residual_likelihood = max(1, int(risk.likelihood * (1 - reduction_factor)))
        residual_impact = max(1, int(risk.impact * (1 - reduction_factor)))
        residual_score = residual_likelihood * residual_impact

        # Determine severity
        if residual_score >= 20:
            severity = RiskSeverity.CRITICAL
        elif residual_score >= 12:
            severity = RiskSeverity.HIGH
        elif residual_score >= 6:
            severity = RiskSeverity.MEDIUM
        else:
            severity = RiskSeverity.LOW

        return ResidualRiskAssessment(
            id=str(uuid.uuid4()),
            risk_id=risk.id,
            residual_likelihood=residual_likelihood,
            residual_impact=residual_impact,
            residual_risk_score=residual_score,
            risk_severity=severity,
            control_effectiveness=overall_effectiveness,
            notes=f"Reduced from inherent score of {risk.inherent_risk_score} through {len(mitigations)} mitigations and {len(controls)} controls",
        )

    def get_risk_summary(
        self,
        risks: List[IdentifiedRisk],
        residual_risks: List[ResidualRiskAssessment],
    ) -> Dict[str, Any]:
        """
        Generate summary statistics for risk assessment.

        Args:
            risks: List of identified risks
            residual_risks: List of residual risk assessments

        Returns:
            Dict with summary statistics
        """
        # Overall counts
        total_risks = len(risks)

        # Severity distribution
        severity_counts = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
        }

        for residual in residual_risks:
            severity_counts[residual.risk_severity.value] += 1

        # Category distribution
        category_counts = {}
        for risk in risks:
            cat = risk.category.value
            category_counts[cat] = category_counts.get(cat, 0) + 1

        # Average risk reduction
        if risks and residual_risks:
            avg_inherent = sum(r.inherent_risk_score for r in risks) / len(risks)
            avg_residual = sum(r.residual_risk_score for r in residual_risks) / len(
                residual_risks
            )
            avg_reduction = ((avg_inherent - avg_residual) / avg_inherent) * 100
        else:
            avg_inherent = 0
            avg_residual = 0
            avg_reduction = 0

        # Top risks
        residual_dict = {r.risk_id: r for r in residual_risks}
        risks_with_scores = [
            {
                "risk": risk,
                "residual": residual_dict.get(risk.id),
            }
            for risk in risks
        ]
        risks_with_scores.sort(
            key=lambda x: (
                x["residual"].residual_risk_score if x["residual"] else 0
            ),
            reverse=True,
        )
        top_10_risks = risks_with_scores[:10]

        return {
            "total_risks": total_risks,
            "severity_distribution": severity_counts,
            "category_distribution": category_counts,
            "average_inherent_score": round(avg_inherent, 2),
            "average_residual_score": round(avg_residual, 2),
            "average_reduction_percent": round(avg_reduction, 2),
            "top_10_risks": top_10_risks,
        }
