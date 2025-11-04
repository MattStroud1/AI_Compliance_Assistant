"""
NEOM Operating AI Pathway - Post-Market Monitoring & Compliance
Based on NEOM Trustworthy AI Playbook operational compliance requirements
"""

from typing import List
from datetime import datetime
import uuid

from ..models import (
    NEOMPhase,
    ComplianceStep,
    PhaseType,
    StepStatus,
)


class NEOMOperatingAIPathway:
    """
    NEOM-compliant pathway for operating and monitoring AI systems post-deployment
    Focuses on ongoing compliance, monitoring, and maintenance
    """

    def __init__(self):
        self.pathway_name = "NEOM Operating AI"

    def create_phases(self, project_id: str) -> List[NEOMPhase]:
        """Create all 7 phases for Operating AI pathway"""
        phases = [
            self._create_phase1_project_documentation(project_id),
            self._create_phase2_privacy_data(project_id),
            self._create_phase3_security(project_id),
            self._create_phase4_fairness_risk(project_id),
            self._create_phase5_explainability(project_id),
            self._create_phase6_technology_robustness(project_id),
            self._create_phase7_postmarket_monitoring(project_id),
        ]

        return phases

    def _create_phase1_project_documentation(self, project_id: str) -> NEOMPhase:
        """Phase 1: Project Setup & Documentation (Questions 1-13)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Name of Project",
                description="Please put the official name, so the AI can be easily tracked over time",
                checklist_items=[
                    "Enter official project name",
                    "Ensure name is unique and traceable",
                    "Verify name matches pre-launch documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Name of AI System Owner",
                description="Please put the name of the business lead who is sponsoring the project",
                checklist_items=[
                    "Identify business sponsor",
                    "Document their authority level",
                    "Confirm ongoing commitment"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Business Unit / NEOM Entity",
                description="Please put your legal entity name",
                checklist_items=[
                    "Identify legal entity",
                    "Confirm jurisdiction",
                    "Document entity structure"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Assessment Completion Details",
                description="Please enter details of who completed, reviewed, and signed-off this assessment",
                checklist_items=[
                    "Name, role and department of person who completed assessment",
                    "Name, role and department of person who reviewed assessment",
                    "Name and role of DPO officer who signed-off assessment",
                    "Assessment outcome, date and link to rationale and remedial measures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="System Deployment Form Changes",
                description="Has the form your AI system will be deployed into the market changed? Your description should be a paragraph or two and include: The type of AI used, whether it is a cloud service or part of a product, its broader context.",
                checklist_items=[
                    "Review current deployment form",
                    "Compare to pre-launch documentation",
                    "Document any changes in AI type",
                    "Document any changes in cloud vs product deployment",
                    "Update broader context if changed"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Project Purpose Changes",
                description="Has the purpose of your project changed? Your description should encompass both the aims of the deploying entity and of the end user - what benefits each derives from using your AI system.",
                checklist_items=[
                    "Review current project purpose",
                    "Assess deploying entity's objectives",
                    "Assess end user benefits",
                    "Document any changes from pre-launch",
                    "Justify any purpose modifications"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Use Case Changes",
                description="Have the intended use cases for the AI system changed? If there are multiple use cases which are materially the same, group them into a 'class' of use cases.",
                checklist_items=[
                    "List current use cases",
                    "Group similar use cases into classes",
                    "Compare to pre-launch use cases",
                    "Document any new use cases",
                    "Document any discontinued use cases"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Geographic & Language Changes",
                description="Have the geographies and languages in which it will be deployed changed? The geographic description should be at the level of country or region. Languages should include official and significant minority languages.",
                checklist_items=[
                    "List current target countries/regions",
                    "Identify current official languages",
                    "Document significant minority languages",
                    "Compare to pre-launch documentation",
                    "Assess impact on fairness & explainability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Stakeholder Changes",
                description="Have the types of individuals who will use the AI system & other stakeholders changed? Please identify different groups, segment them, and describe each segment noting vulnerabilities and potential for misuse.",
                checklist_items=[
                    "Identify current user groups",
                    "Identify current subject groups",
                    "Segment each group",
                    "Document vulnerabilities per segment",
                    "Assess misuse potential per segment",
                    "Compare to pre-launch stakeholder analysis"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="RACI Matrix Updates",
                description="Has your RACI changed? If so please attach an updated version. See the 'Trustworthy AI Toolbox' for a template RACI which you can edit and adapt to your project.",
                checklist_items=[
                    "Review current RACI matrix",
                    "Compare to pre-launch RACI",
                    "Document any role changes",
                    "Obtain sign-off from new participants",
                    "Update RACI documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,
            name="Project Setup & Documentation",
            description="Review and update project documentation and governance for operational AI system",
            order=1,
            steps=steps
        )

    def _create_phase2_privacy_data(self, project_id: str) -> NEOMPhase:
        """Phase 2: Privacy & Data Governance (Questions 14-20)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Data Processing Changes",
                description="Has the type of data you are processing changed? Does your processing fall into categories requiring special protection? Are you processing sensitive data or data relating to children or vulnerable groups?",
                checklist_items=[
                    "Review current data processing activities",
                    "Check against LIST 1 categories",
                    "Identify sensitive data processing",
                    "Document children/vulnerable groups data",
                    "Explain necessity of sensitive data use",
                    "Compare to pre-launch assessment"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Legal Basis Justification",
                description="Please justify on what basis the data is being processed. The legal basis could be legitimate interest, contract, consent or other. Please see the ICO for guidance and consult with the DPO if necessary.",
                checklist_items=[
                    "Review legal basis for processing",
                    "Consult ICO guidance",
                    "Consult with DPO if needed",
                    "Document chosen legal basis",
                    "Justify decision logic",
                    "Verify alignment with pre-launch basis"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Privacy Risk Analysis",
                description="Analyse and document the privacy risks arising from normal use and foreseeable misuse. Consider inability to exercise rights, access services, loss of control, discrimination, identity theft, financial loss, reputational damage, physical harm, loss of confidentiality, re-identification, and other economic/social disadvantage.",
                checklist_items=[
                    "Identify privacy risks in normal use",
                    "Identify privacy risks in foreseeable misuse",
                    "Assess each user segment separately",
                    "Document all identified risks",
                    "Estimate impact and likelihood",
                    "Compare to pre-launch risk assessment"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Data Labelling & Quality Verification",
                description="Has any new data been labelled, categorized and the data quality determined and verified? Your response should include data model, metadata and data governance framework. Describe steps to ensure error-free dataset.",
                checklist_items=[
                    "Document new data labelling activities",
                    "Describe categorization methodology",
                    "Document data quality verification",
                    "Describe governance framework adherence",
                    "Verify error-free status",
                    "Update data quality documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Anonymisation & PETs Implementation",
                description="Has anonymisation and Privacy Enhancing Technologies (PETs) been maximally applied? Describe opportunities identified to use PETs, their benefits and issues, and what you chose to implement.",
                checklist_items=[
                    "Identify PET opportunities in design",
                    "Document potential benefits of PETs",
                    "Document implementation issues",
                    "Describe implemented PETs",
                    "Verify anonymisation robustness",
                    "Update PET implementation documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Risk Remediation & Residual Risk",
                description="What other risk remediation measures were undertaken? Estimate residual risk by: 1) estimating impact on individuals, 2) estimating users impacted, 3) risk without mitigation, 4) describing mitigating measures, 5) calculating residual risk with mitigation.",
                checklist_items=[
                    "Document additional mitigation measures",
                    "Estimate impact per risk (scale 1-10)",
                    "Estimate percentage of users affected",
                    "Calculate risk without mitigation",
                    "Describe all mitigating measures",
                    "Calculate residual risk with mitigation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Residual Risk Acceptance Justification",
                description="Why was the residual risk judged acceptable? Your answer should take the form of a balance test, weighing the residual risk against the benefits to the end user and other stakeholders - including wider society.",
                checklist_items=[
                    "Document residual risk level",
                    "Document benefits to end users",
                    "Document benefits to stakeholders",
                    "Document benefits to wider society",
                    "Perform balance test",
                    "Justify risk acceptance decision"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Privacy & Data Governance",
            description="Monitor and update privacy controls and data governance for operational AI",
            order=2,
            steps=steps
        )

    def _create_phase3_security(self, project_id: str) -> NEOMPhase:
        """Phase 3: Security Framework (Questions 21-24)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Security Changes Documentation",
                description="Have there been any security related changes to your AI system since the 'Pre-Launch AI Impact Assessment' - if so please document.",
                checklist_items=[
                    "Review security architecture changes",
                    "Document infrastructure modifications",
                    "Document access control changes",
                    "Document encryption changes",
                    "Compare to pre-launch security design",
                    "Update security documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Emerging Security Threats",
                description="Analyse and document any new security threats that have emerged since the 'Pre-launch AI Impact Assessment'.",
                checklist_items=[
                    "Identify new threat vectors",
                    "Assess adversarial attack risks",
                    "Document data poisoning threats",
                    "Document model extraction risks",
                    "Assess infrastructure vulnerabilities",
                    "Update threat assessment documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Security Threat Mitigation",
                description="Describe the measures taken to mitigate any emerging security threats.",
                checklist_items=[
                    "Document threat mitigation strategies",
                    "Describe technical controls implemented",
                    "Describe procedural controls implemented",
                    "Document monitoring mechanisms",
                    "Describe incident response procedures",
                    "Update security controls documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Residual Security Risks",
                description="Given the security measures implemented, describe what residual risks do you foresee? Include: 1) identify risks, 2) estimate impact on individual, 3) estimate % users impacted, 4) risk without mitigation, 5) mitigating measures, 6) residual risk with mitigation and justification.",
                checklist_items=[
                    "Identify residual security risks",
                    "Estimate impact per risk (scale 1-10)",
                    "Estimate percentage of users affected",
                    "Calculate risk without mitigation",
                    "Describe all mitigating measures",
                    "Calculate residual risk with mitigation",
                    "Justify acceptance of residual risk"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Security Framework",
            description="Monitor and enhance security controls for operational AI system",
            order=3,
            steps=steps
        )

    def _create_phase4_fairness_risk(self, project_id: str) -> NEOMPhase:
        """Phase 4: Fairness & Risk Mitigation (Questions 25-39)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Human Rights & Cultural Impact",
                description="Have any new risks to human rights and culture arisen from this AI system? Document diversity analysis of user segments and contexts. Justify that benefits outweigh harm to human rights and cultural values.",
                checklist_items=[
                    "Analyse user segment diversity",
                    "Document range of usage contexts",
                    "Identify human rights impacts",
                    "Identify cultural value impacts",
                    "Justify benefits vs harms balance",
                    "Document segments/contexts with misalignment"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Environmental Resource Impact",
                description="What steps have you taken to reduce resource usage of the AI system? Estimate resource impact vs next best design. If next best had less impact, justify your choice. Consider training electricity, model outputs impact, and societal impact.",
                checklist_items=[
                    "Estimate current design resource impact",
                    "Estimate next best design resource impact",
                    "Justify design choice if higher impact",
                    "Document electricity consumption",
                    "Document output environmental effects",
                    "Analyse societal impact"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Feedback Loop Identification & Mitigation",
                description="What steps have you taken to identify and mitigate feedback loops that may have arisen while the AI system is operational? Where models continue learning, previous predictions may shape future predictions, creating bias amplification.",
                checklist_items=[
                    "Identify potential feedback loops",
                    "Document observed feedback patterns",
                    "Analyse bias amplification risks",
                    "Implement loop detection mechanisms",
                    "Describe mitigation strategies",
                    "Monitor for emergent feedback loops"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Foreseeable Errors & Misuse",
                description="Identify and document any newly foreseeable errors and misuse. Foreseeable errors might include default data settings like '999' or '0000'. Foreseeable misuse might include use in contexts for which it's not designed. Include consequences of false positives and negatives.",
                checklist_items=[
                    "Identify foreseeable input errors",
                    "Document default/invalid value handling",
                    "Identify foreseeable misuse scenarios",
                    "Analyse false positive consequences",
                    "Analyse false negative consequences",
                    "Update error handling documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Data Quality & Representativeness Review",
                description="Is there any reason to believe the data credibility, quality, sample size, or representativeness has changed? Document: 1) validate data quality, 2) justify sample size adequacy, 3) justify dataset representativeness of end users.",
                checklist_items=[
                    "Validate current data quality",
                    "Assess sample size adequacy",
                    "Verify dataset representativeness",
                    "Compare to pre-launch data quality",
                    "Document any quality degradation",
                    "Justify continued fitness for purpose"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="New Bias Sources Identification",
                description="Are there any new sources of bias which may have arisen? Please respond explicitly to each form of bias cited in tasks 4.8 to 4.13 of the 'Pre-Launch AI Impact Assessment'. Analyse how each data attribute can be interpreted and identify measurement errors.",
                checklist_items=[
                    "Review selection bias",
                    "Review historical bias",
                    "Review survivor bias",
                    "Review availability bias",
                    "Review outlier bias",
                    "Review evaluation bias",
                    "Analyse data attribute interpretations",
                    "Document measurement errors",
                    "Document data ambiguity"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Quality & Bias Risk Mitigation",
                description="How have these new quality and bias risks been mitigated? Document any additional data acquired, new sampling approaches, or other mitigation strategies.",
                checklist_items=[
                    "Document additional data acquired",
                    "Describe new sampling approaches",
                    "Document bias correction techniques",
                    "Describe feature engineering changes",
                    "Document model adjustments",
                    "Verify mitigation effectiveness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Impact on Fairness Metrics",
                description="What are the impacts of any changes from questions 29, 30, 31 on the fairness metrics? Referencing the fairness metrics defined in TASK 3.28 - Analyse and document the impact of your choices of features and champion models.",
                checklist_items=[
                    "Review defined fairness metrics",
                    "Analyse impact of feature changes",
                    "Analyse impact of model changes",
                    "Document metric value changes",
                    "Assess threshold compliance",
                    "Update fairness metric documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Risk Measurement & Control Process",
                description="Describe process you have implemented to measure and control the risks identified. Describe design changes to mitigate risks. Where risks cannot be removed by design, describe human oversight controls and training.",
                checklist_items=[
                    "Document risk measurement process",
                    "Describe design-based mitigations",
                    "Document human oversight controls",
                    "Describe operator training program",
                    "Document escalation procedures",
                    "Verify process effectiveness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="Human Oversight Effectiveness",
                description="Evidence that the processes which you have established to enable human oversight are implemented and effective. Describe how humans have effective oversight - what tools do operators have? How are they empowered to intervene when detecting anomalous or risky processing?",
                checklist_items=[
                    "Document operator monitoring tools",
                    "Describe system output visualization",
                    "Document intervention mechanisms",
                    "Describe escalation authority",
                    "Evidence training effectiveness",
                    "Document oversight process adherence"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=11,
                title="Residual Risk Estimation",
                description="Estimate any changes to the residual risk based on operational experience and mitigation measures implemented.",
                checklist_items=[
                    "Calculate current residual risk levels",
                    "Compare to pre-launch estimates",
                    "Document risk changes",
                    "Assess mitigation effectiveness",
                    "Update risk register"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=12,
                title="Residual Risk Justification",
                description="Justify why this residual risk is acceptable. Document features and processes incorporated to mitigate risks. Estimate residual risk: 1) impact on individual, 2) users impacted, 3) risk without mitigation, 4) mitigating measures, 5) residual risk with mitigation.",
                checklist_items=[
                    "Document mitigation features",
                    "Document mitigation processes",
                    "Estimate impact per risk (scale 1-10)",
                    "Estimate percentage users affected",
                    "Calculate residual risk",
                    "Justify acceptance of residual risk"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=13,
                title="Fairness Metric Threshold Justification",
                description="Justify the values you set for the fairness metric thresholds are still appropriate. Define end user segments at risk, quantify model output, define acceptable variability thresholds, create metrics for all output parameters.",
                checklist_items=[
                    "Define at-risk user segments",
                    "Quantify model outputs",
                    "Define acceptable variability",
                    "Set metric thresholds",
                    "Create comprehensive metrics",
                    "Justify threshold appropriateness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=14,
                title="Fairness Metrics Threshold Compliance",
                description="Evidence that the fairness metrics are still within thresholds. Based on the AI model validation dataset, document validation process to test whether fairness metrics are below thresholds and record the outcome.",
                checklist_items=[
                    "Test metrics against validation data",
                    "Document validation methodology",
                    "Record metric values",
                    "Compare to thresholds",
                    "Document compliance outcome",
                    "Update validation records"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=15,
                title="Ongoing Fairness Monitoring & Sign-off",
                description="Evidence that you have monitored & kept fairness metrics below their thresholds and this has been signed off by the AI assessor. Process must include RACI, measurement frequency, governance structure. Measurements stored in auditable form.",
                checklist_items=[
                    "Document monitoring RACI",
                    "Define measurement frequency",
                    "Describe governance structure",
                    "Store measurements in auditable form",
                    "Obtain AI assessor sign-off",
                    "Evidence ongoing process operation"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Fairness & Risk Mitigation",
            description="Monitor fairness metrics and mitigate emerging risks in operational AI",
            order=4,
            steps=steps
        )

    def _create_phase5_explainability(self, project_id: str) -> NEOMPhase:
        """Phase 5: Explainability Framework (Questions 40-46)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="User Notification of AI Interaction",
                description="Evidence that you have informed users when they are interacting with AI. When the system results in fake/manipulative content or uses biometrics/emotional recognition, how will you inform users? Document justification that this enables effective decisions. Include fact-checking means for AI-generated content.",
                checklist_items=[
                    "Document user notification mechanism",
                    "Describe notification for fake content",
                    "Describe notification for biometric use",
                    "Justify notification effectiveness",
                    "Implement fact-checking capability",
                    "Evidence notification implementation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Explanatory Text & Process Effectiveness",
                description="Evidence that the explanatory text & process you have implemented to explain your AI system's decisions to operators and users are effective. Create explanatory text for end users. Implement and document process through which end users can get decisions explained.",
                checklist_items=[
                    "Create user-friendly explanatory text",
                    "Describe AI system purpose clearly",
                    "Describe AI system impact clearly",
                    "Implement decision explanation process",
                    "Document explanation request procedure",
                    "Evidence explanation effectiveness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Operational Input Data Documentation",
                description="Is the operational input data used documented and archived? Your response should include data model, metadata and data governance framework adhered to. Describe steps to ensure error-free dataset.",
                checklist_items=[
                    "Document input data model",
                    "Document metadata structure",
                    "Describe governance framework",
                    "Implement data archiving process",
                    "Verify error-free status",
                    "Evidence documentation completeness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Decision Traceability & Auditability",
                description="Evidence that your AI system's decisions are traceable and auditable. Explain and document how the information can be used to demonstrate whether the AI system was working as intended during its interaction with a specific user.",
                checklist_items=[
                    "Implement decision logging",
                    "Document traceability mechanism",
                    "Create audit trail process",
                    "Enable user-specific decision review",
                    "Document intended operation verification",
                    "Evidence audit capability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Stakeholder Reporting Process",
                description="Evidence that your process to report fairness metrics, breakdowns, and breaches to stakeholders is implemented and working effectively. Design, document and implement governed process to share metric values, thresholds and corrective measures. Conduct periodic UI assessments.",
                checklist_items=[
                    "Design stakeholder reporting process",
                    "Document reporting governance",
                    "Share metric values regularly",
                    "Share threshold information",
                    "Share corrective measures taken",
                    "Conduct periodic UI assessments",
                    "Evidence process effectiveness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Complaints Procedure Effectiveness",
                description="Evidence that the complaints procedure which you have established works effectively. Design and document process that end users, operators and deploying entities can use to lodge a complaint and monitor that complaint until resolution.",
                checklist_items=[
                    "Design complaint lodging process",
                    "Document complaint handling procedure",
                    "Implement complaint tracking system",
                    "Enable complaint status monitoring",
                    "Document resolution process",
                    "Evidence procedure effectiveness"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Explainability Framework",
            description="Ensure transparency and explainability of AI decisions to all stakeholders",
            order=5,
            steps=steps
        )

    def _create_phase6_technology_robustness(self, project_id: str) -> NEOMPhase:
        """Phase 6: Technology Development & Robustness (Questions 47-55)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="System Lifecycle Dates",
                description="Please give the dates of deployment, all upgrades and the intended retirement date of your AI system.",
                checklist_items=[
                    "Record initial deployment date",
                    "Document all upgrade dates",
                    "Document upgrade descriptions",
                    "Set intended retirement date",
                    "Maintain lifecycle timeline",
                    "Update dates as system evolves"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Out-of-Range Data Detection",
                description="Evidence whether the AI system has encountered in operation any data which is outside of the range of the outliers used in the training dataset. Describe and document how you've established expected data ranges and ensured training/validation datasets contain sufficient extreme data.",
                checklist_items=[
                    "Establish expected data ranges",
                    "Define outlier thresholds",
                    "Verify training data includes outliers",
                    "Verify validation data includes outliers",
                    "Monitor for out-of-range inputs",
                    "Document out-of-range incidents"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Extreme Input Handling Validation",
                description="Demonstrate that your AI system functioned as intended in response to any extreme data input events. Analyse and document likely input errors, identify these and ensure safeguards prevent harmful outputs (e.g., defaults to '0000' or '9999' should trigger warnings).",
                checklist_items=[
                    "Identify likely input errors",
                    "Implement input validation safeguards",
                    "Test extreme input scenarios",
                    "Document system response to extremes",
                    "Verify warning mechanisms work",
                    "Evidence safe handling of edge cases"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Data Archiving Process Updates",
                description="Have there been any changes to your data archiving process? Describe and document your data backup procedures and processes, and record when these have happened.",
                checklist_items=[
                    "Document backup procedures",
                    "Describe backup frequency",
                    "Document backup storage locations",
                    "Record backup execution dates",
                    "Verify backup integrity",
                    "Document any process changes"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="System Integration Changes",
                description="Have there been any changes to how the AI system interacts or can be used to interact with hardware or software that is not part of the AI system itself? Describe the context - what systems is it connected to, which systems does its output feed into, and what's the net effect?",
                checklist_items=[
                    "Document connected systems",
                    "Describe input sources",
                    "Describe output destinations",
                    "Document integration points",
                    "Analyse net effect of integrations",
                    "Update system context documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Hardware Platform Description",
                description="Describe the hardware on which the AI system is running. May include intended hardware platform and brief discussion about where the system could run given minimum hardware requirements (e.g., cloud, MacBook, mobile phone).",
                checklist_items=[
                    "Document current hardware platform",
                    "Specify minimum hardware requirements",
                    "Describe deployment environment",
                    "Document scalability considerations",
                    "Verify hardware compatibility",
                    "Update hardware documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Software & Firmware Version Management",
                description="Record the AI system's versions of relevant software or firmware and any requirement related to version updates. Documented record of hardware and software versions through lifecycle. Include process to keep this record up to date.",
                checklist_items=[
                    "Record current software versions",
                    "Record current firmware versions",
                    "Document version dependencies",
                    "Document update requirements",
                    "Maintain version history log",
                    "Implement version tracking process"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Installation & User Instructions Updates",
                description="Have there been any changes to the installations, operator or user instructions. If so, please explain. (TASK 5.13 should have already led to user instructions in the Explainability Framework. This adds them to Technology Development Framework.)",
                checklist_items=[
                    "Review current installation instructions",
                    "Review current operator instructions",
                    "Review current user instructions",
                    "Document any instruction changes",
                    "Verify instruction accuracy",
                    "Update instruction documentation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="System Lifecycle Change Log",
                description="Please describe any other changes made to the system through its lifecycle. Building on TASK 6.16, describe and document what functional changes occurred as a result of each hardware or software change. Include process to keep this record up to date.",
                checklist_items=[
                    "Maintain comprehensive change log",
                    "Document functional impact of changes",
                    "Link changes to version updates",
                    "Describe change rationale",
                    "Implement ongoing tracking process",
                    "Update change documentation regularly"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Technology Development & Robustness",
            description="Monitor technical robustness, safety, and system changes throughout operation",
            order=6,
            steps=steps
        )

    def _create_phase7_postmarket_monitoring(self, project_id: str) -> NEOMPhase:
        """Phase 7: Post-Market Monitoring (Question 56)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Post-Market Assessment Compliance",
                description="Evidence that these 'Post-market AI Impact Assessments' have been conducted with the frequency defined in the original 'Post-Market Monitoring Plan' described in the Pre-Deployment AI Impact Assessment and signed off by the AI Compliance Officer.",
                checklist_items=[
                    "Review Post-Market Monitoring Plan",
                    "Verify assessment frequency compliance",
                    "Conduct scheduled assessments",
                    "Document assessment findings",
                    "Obtain AI Compliance Officer sign-off",
                    "Maintain assessment records",
                    "Update monitoring plan as needed"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Post-Market Monitoring",
            description="Ensure ongoing compliance through regular post-market impact assessments",
            order=7,
            steps=steps
        )
