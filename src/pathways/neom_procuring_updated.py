"""NEOM Procuring AI pathway - Comprehensive AI procurement assessment"""

from typing import List
import uuid
from src.models import (
    NEOMPhase,
    ComplianceStep,
    StepStatus,
    PhaseType
)


class NEOMProcuringAIPathway:
    """
    Comprehensive pathway for procuring AI systems following NEOM trustworthy AI principles
    Organized into 7 phases with detailed compliance controls and evidence requirements
    """

    def create_phases(self, project_id: str) -> List[NEOMPhase]:
        """Create all phases for the procuring AI pathway"""

        phases = [
            self._create_phase1_project_setup(project_id),
            self._create_phase2_privacy_data(project_id),
            self._create_phase3_security(project_id),
            self._create_phase4_fairness_risk(project_id),
            self._create_phase5_explainability(project_id),
            self._create_phase6_technology(project_id),
            self._create_phase7_monitoring(project_id),
        ]

        return phases

    def _create_phase1_project_setup(self, project_id: str) -> NEOMPhase:
        """Phase 1: Project Setup & Assessment (Questions 1-14)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Name of Project",
                description="Please put the official name, so the AI can be easily tracked over time",
                checklist_items=[
                    "Enter official project name",
                    "Ensure name is unique and traceable",
                    "Document project naming convention"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Name of AI System owner",
                description="Please put the name of the business lead who is sponsoring the project",
                checklist_items=[
                    "Identify business sponsor",
                    "Document their authority level",
                    "Confirm their commitment"
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
                    "Assessment outcome, date and link to rational and remedial measures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="System Description",
                description="Give a short, high-level description of your project, including what form your AI system will be deployed. Your description should include: The type of AI used, whether it is a cloud service or part of a product, and its broader context.",
                checklist_items=[
                    "Describe AI type and deployment form",
                    "Explain cloud vs product context",
                    "Document broader system context"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Project Purpose",
                description="Describe the purpose of your project. Your description should encompass both the aims of the deploying entity and of the end user - what benefits each derives from using your AI system.",
                checklist_items=[
                    "Define deployer's objectives",
                    "Define end user benefits",
                    "Document value proposition"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Intended Use Cases",
                description="Describe the intended use cases for the AI system. If there are multiple use cases which are materially the same, group them into a 'class' of use cases.",
                checklist_items=[
                    "List all intended use cases",
                    "Group similar use cases into classes",
                    "Document each class with examples"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Geographic Deployment & Languages",
                description="Describe the intended geographies and languages in which the AI system will be deployed. The geographic description should be at the level of country or region. Include official languages and significant minority languages.",
                checklist_items=[
                    "List target countries/regions",
                    "Identify official languages",
                    "Document significant minority languages",
                    "Consider language needs for fairness & explainability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Stakeholder Identification",
                description="Describe the type of individuals who will use, and be the subject of, the AI system, and any other stakeholders. Please identify different groups, segment them, and describe each segment noting vulnerabilities and potential for misuse.",
                checklist_items=[
                    "Identify user groups",
                    "Identify subject groups (data subjects)",
                    "Segment each group",
                    "Document vulnerabilities per segment",
                    "Assess misuse potential per segment"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="Life Cycle - Deployment Date",
                description="Estimated date when the system will be deployed (DD/MM/YYYY). This is the date you are aiming for, subject to approvals.",
                checklist_items=[
                    "Set target deployment date",
                    "Document approval dependencies",
                    "Plan timeline milestones"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=11,
                title="Create Project RACI",
                description="Create a RACI for your project and document each individual's sign-off agreeing to participate in the project in that capacity. This should include the procure, integrate and operate phases. See the 'Trustworthy AI Toolbox' for a template RACI which you can edit and adapt to your project.",
                checklist_items=[
                    "Create RACI matrix for procure phase",
                    "Create RACI matrix for integrate phase",
                    "Create RACI matrix for operate phase",
                    "Obtain sign-off from all participants",
                    "Document all commitments"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,
            name="Project Setup & Assessment",
            description="Define project scope, stakeholders, and governance structure for AI procurement",
            order=1,
            steps=steps
        )


    def _create_phase2_privacy_data(self, project_id: str) -> NEOMPhase:
        """Phase 2: Privacy & Data Governance (Questions 15-29)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Privacy & Data Governance Introduction",
                description="Write an introduction to the Privacy and Data Governance Framework. Summarise what you did and its outcome to help the reader understand your approach.",
                checklist_items=[
                    "Summarize privacy approach",
                    "Document key outcomes",
                    "Provide reader guidance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Dataset Documentation",
                description="Document the dataset that you intend to use, including data categorization, labelling, provenance, structure, quality and the data governance process. Include data model, metadata and governance framework. Describe steps taken to ensure the data set is error free.",
                checklist_items=[
                    "Document data categorization",
                    "Describe labelling methodology",
                    "Document data provenance",
                    "Describe data structure",
                    "Document quality assurance process",
                    "Describe governance framework",
                    "Verify error-free status"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Sensitive Data Processing Justification",
                description="If processing sensitive data, describe why its use is unavoidable given your AI system's objective. Does processing fall into sensitive categories or relate to children/vulnerable groups? If so, describe the data, how it is processed and explain why this is necessary.",
                checklist_items=[
                    "Identify sensitive data categories",
                    "Assess children/vulnerable groups impact",
                    "Justify necessity of sensitive data",
                    "Document processing methods",
                    "Explain unavoidability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Legal Basis for Data Processing",
                description="Decide the legal basis upon which you will process the data and document the logic of that decision. The legal basis could be legitimate interest, contract, consent or other. Please see the ICO for guidance and consult with the DPO if necessary.",
                checklist_items=[
                    "Review legal basis options",
                    "Consult ICO guidance",
                    "Consult with DPO if needed",
                    "Document chosen legal basis",
                    "Justify the decision logic"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Privacy Risk Analysis",
                description="Analyse and document any privacy risks that may result from your data processing activities. Consider risks in normal use and foreseeable misuse for each user segment. Consider: inability to exercise rights, inability to access services, loss of control over data, discrimination, identity theft, financial loss, reputational damage, physical harm, loss of confidentiality, re-identification of pseudonymised data, and other economic or social disadvantage.",
                checklist_items=[
                    "Identify privacy risks in normal use",
                    "Identify privacy risks in foreseeable misuse",
                    "Assess each user segment separately",
                    "Document all identified risks",
                    "Estimate impact and likelihood"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Data Anonymisation",
                description="Where possible anonymise the data, write up how this was done and explain why the anonymisation is robust. If personally identifiable data has to be used, justify why. Explain how you have adhered to best-practice anonymisation per ICO Code of Practice. If anonymisation is not possible, justify using identifiable data through a balance test weighing risks against benefits.",
                checklist_items=[
                    "Attempt anonymisation where possible",
                    "Document anonymisation methodology",
                    "Explain robustness of anonymisation",
                    "If PII required, justify necessity",
                    "Conduct balance test if needed",
                    "Reference ICO Code of Practice"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Sensitive Data & Proxy Identification",
                description="What attempts were made to identify and remove sensitive data and its proxies? Describe use of sensitive data. Justify why non-sensitive data types are not acting as proxies for sensitive data. Techniques such as association rules can identify proxies.",
                checklist_items=[
                    "Identify sensitive data in dataset",
                    "Search for proxy variables",
                    "Use association rule mining",
                    "Document removal attempts",
                    "Justify remaining sensitive data"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Dataset Combination Risks",
                description="Document any additional risks arising from combining datasets. If datasets are to be combined, describe risks of individuals becoming identifiable and what new insights might become derivable. Consider how these risks depend on the complexity of deriving such insights.",
                checklist_items=[
                    "Identify dataset combinations",
                    "Assess re-identification risks",
                    "Document new insights possible",
                    "Evaluate complexity of deriving insights",
                    "Document mitigation measures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Privacy-Enhancing Technologies (PETs)",
                description="Explain why you did or did not use PETs in your design. Describe the opportunities identified to use PETs, what benefits they could bring, what issues might arise, and conclude with what you chose to implement.",
                checklist_items=[
                    "Identify PET opportunities",
                    "Assess potential benefits",
                    "Identify potential issues",
                    "Document implementation decision",
                    "Justify final choice"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="Privacy by Design",
                description="Justify that your design and operational processes embody privacy by design. Justify minimum data usage, use of anonymisation and PETs. Explain user information and controls. Explain cyber-security protections. Justify default settings. Describe organizational processes and third-party processor safeguards. Refer to ICO Privacy by Design guide.",
                checklist_items=[
                    "Justify minimum data collection",
                    "Document anonymisation & PETs use",
                    "Describe user information & controls",
                    "Explain cyber-security measures",
                    "Justify default settings",
                    "Describe organizational processes",
                    "Document third-party safeguards"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=11,
                title="Privacy Risk Mitigation & Residual Risk",
                description="Describe any other remediation steps taken to mitigate privacy risks and estimate residual risk. For each risk: 1) Estimate impact on individual, 2) Estimate number of users impacted, 3) Calculate risk without mitigation, 4) Describe mitigating measures, 5) Recalculate residual risk with mitigation. (Use scales of 1-10)",
                checklist_items=[
                    "List all mitigation measures",
                    "Estimate impact per risk (1-10)",
                    "Estimate users impacted (1-10)",
                    "Calculate unmitigated risk",
                    "Document mitigations",
                    "Calculate residual risk"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=12,
                title="Privacy Balance Test",
                description="Justify why the benefits of the proposed data processing outweigh the residual risk. Your answer should take the form of a balance test, weighing the residual risk against the benefits to the end user and other stakeholders - including wider society.",
                checklist_items=[
                    "Quantify residual risks",
                    "Quantify benefits to users",
                    "Quantify benefits to stakeholders",
                    "Quantify societal benefits",
                    "Perform balance test",
                    "Document justification"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=13,
                title="Data Recording & Archiving",
                description="Record and describe the data used to train, validate and operate the AI system and ensure it's archived. Build on dataset documentation and create 'data cards' for each dataset. Include how datasets were used, relationships between datasets, and archiving policy with access details.",
                checklist_items=[
                    "Create data card for training data",
                    "Create data card for validation data",
                    "Create data card for operational data",
                    "Document dataset relationships",
                    "Define archiving policy",
                    "Document archive access procedure"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=14,
                title="Data Preparation Phase Sign-off",
                description="Document how you have archived the data associated with the data preparation phase. Then ensure that the data preparation phase is signed off by the project owner and the PDPO Compliance Officer assigned to the project.",
                checklist_items=[
                    "Archive all data preparation documentation",
                    "Obtain project owner sign-off",
                    "Obtain PDPO Compliance Officer sign-off",
                    "Document all approvals"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Privacy & Data Governance",
            description="Ensure data processing complies with privacy regulations and governance standards",
            order=2,
            steps=steps
        )

    def _create_phase3_security(self, project_id: str) -> NEOMPhase:
        """Phase 3: Security Framework (Questions 30-40)"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Security Framework Introduction",
                description="Write an introduction to the Security Framework. Summarise what you did and its outcome to help the reader understand your approach to security.",
                checklist_items=[
                    "Summarize security approach",
                    "Document key outcomes",
                    "Provide reader guidance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Security Methodology",
                description="Document your Security methodology to prevent the AI system being hacked and how you will apply it. Document how you plan to implement an appropriate security standard embodying a methodology endorsed by NEOM CISO (e.g., ISO 27001). Check with CISO that they agree you are following an appropriate standard.",
                checklist_items=[
                    "Select appropriate security standard",
                    "Document chosen methodology",
                    "Get CISO endorsement",
                    "Describe implementation plan",
                    "Define security controls"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="AI Algorithm Security",
                description="Write up security aspects of your choice of AI algorithm & what security vulnerabilities might arise. Document why you chose your AI approach and algorithm, and the security implications. What attack vectors does this choice open up?",
                checklist_items=[
                    "Document AI algorithm choice",
                    "Justify algorithm selection",
                    "Identify security vulnerabilities",
                    "Document attack vectors",
                    "Assess security implications"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="System Robustness Features",
                description="Describe the features of the AI system's design that make it robust to being hacked. Describe security features such as perimeter security measures, network anomaly monitoring etc, and how they interact to create a robust security posture.",
                checklist_items=[
                    "Document perimeter security",
                    "Describe network monitoring",
                    "Explain access controls",
                    "Document intrusion detection",
                    "Describe security integration"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Adversarial Attack Prevention",
                description="Describe measures taken to prevent adversarial attacks and other input manipulation techniques. Use tools from the Trustworthy AI Toolbox to test for adversarial weaknesses. Describe how you tested, what steps you took to harden your model, and what residual risk remains.",
                checklist_items=[
                    "Test for adversarial examples",
                    "Document testing tools used",
                    "Describe hardening measures",
                    "Document mitigation steps",
                    "Assess residual risk"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Data Poisoning Prevention",
                description="Describe measures taken to prevent data poisoning attacks during training. Describe how you ensured data quality and integrity from 1) data creation to custody, 2) during model training/validation, 3) in post-market context. Describe robust model architecture design. Measures should be proportionate to risks.",
                checklist_items=[
                    "Ensure data provenance integrity",
                    "Protect data during training",
                    "Monitor post-market data quality",
                    "Design resistant architecture",
                    "Document proportionate measures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Model Inversion Attack Prevention",
                description="Describe measures taken to prevent model inversion attacks and learning transfer attacks. Include 1) limiting model access to sensitive data, 2) controlling model outputs (e.g., limiting granularity), 3) monitoring model queries for anomalous behavior. Measures should be proportionate to risks.",
                checklist_items=[
                    "Limit sensitive data access",
                    "Control output granularity",
                    "Monitor query patterns",
                    "Detect anomalous behavior",
                    "Document proportionate measures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Data Supply Chain Integrity",
                description="Explain how you ensured your data supply chain integrity to ensure training data has not been poisoned. Include how you implemented IAM and justify if it is appropriately robust. Highlight how this differs from original plans and justify IAM procedures including authentication and verification.",
                checklist_items=[
                    "Document data supply chain security",
                    "Implement IAM controls",
                    "Describe authentication methods",
                    "Describe verification procedures",
                    "Justify robustness of measures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Security Residual Risk Assessment",
                description="Given security measures implemented, identify foreseeable residual risks, mitigation steps, and final residual risk. Include: 1) Identify risks, 2) estimate impact on individual, 3) estimate % users impacted, 4) calculate risk without mitigation, 5) describe mitigations, 6) recalculate residual risk and justify why it's acceptable.",
                checklist_items=[
                    "Identify all security risks",
                    "Estimate individual impact",
                    "Estimate users affected",
                    "Calculate unmitigated risk",
                    "Document mitigations",
                    "Calculate residual risk",
                    "Justify acceptability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="Security Validation Evidence",
                description="Provide evidence that you have validated the model's robustness against adversarial, data poisoning, model inversion attacks, and other identified attacks. Documentation should include validation methodology, system configuration, parameter space explored and outcome in sufficient detail for expert reproduction.",
                checklist_items=[
                    "Document validation methodology",
                    "Record system configuration",
                    "Document parameter space tested",
                    "Record validation outcomes",
                    "Ensure reproducibility"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=11,
                title="Security Sign-off",
                description="Document that the security methodology, design and validation work is signed-off by the project owner and the PDPO AI Compliance Officer. Archive documentation associated with security methodology and validation. Seek sign-off during PITSTOP meeting at end of 'Build and Design' phase.",
                checklist_items=[
                    "Archive security documentation",
                    "Schedule PITSTOP meeting",
                    "Obtain project owner sign-off",
                    "Obtain PDPO Compliance Officer sign-off",
                    "Document all approvals"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Security Framework",
            description="Establish comprehensive security measures to protect the AI system from attacks",
            order=3,
            steps=steps
        )

    def _create_phase4_fairness_risk(self, project_id: str) -> NEOMPhase:
        """Phase 4: Fairness & Risk Mitigation - Part 1 of fairness questions (Questions 41-60)"""
        # Note: Due to size, splitting fairness into multiple methods

        steps = self._get_fairness_steps_part1()

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Fairness & Risk Mitigation",
            description="Ensure fairness, identify biases, and mitigate risks throughout the AI lifecycle",
            order=4,
            steps=steps
        )

    def _get_fairness_steps_part1(self) -> List[ComplianceStep]:
        """Helper method for fairness steps - all fairness and bias questions"""
        return [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Fairness & Risk Mitigation Introduction",
                description="Write an introduction to the Fairness & Risk Mitigation Framework. Summarise what you did and its outcome.",
                checklist_items=[
                    "Summarize fairness approach",
                    "Document key outcomes",
                    "Provide reader guidance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Legal & Ethical Data Acquisition",
                description="Evidence that any data used or to be used was acquired legally and ethically - including not breaching copyright. The ethical test should include justifying why a typical end user would feel processing their sensitive data in the planned way would be fair, reasonable and in their best interests.",
                checklist_items=[
                    "Verify legal data acquisition",
                    "Check copyright compliance",
                    "Document ethical justification",
                    "Consider user perspective",
                    "Obtain necessary consents"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Data Credibility & Representativeness",
                description="Justify that the data credibility, quality & sample size is representative and sufficient for the intended purpose. Document: 1) Validate data quality, 2) Justify adequate sample size, 3) Justify dataset is representative of intended end users.",
                checklist_items=[
                    "Validate data quality",
                    "Analyze sample size adequacy",
                    "Assess representativeness",
                    "Document justification",
                    "Identify any gaps"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Human Rights & Cultural Values Alignment",
                description="Analyse and document how the AI system will align to human rights and cultural values. Document analysis of diversity of user segments and contexts. Justify why benefits to users and society outweigh any harm to human rights and cultural values. Identify segments/contexts where system may not be aligned.",
                checklist_items=[
                    "Analyze user diversity",
                    "Assess usage contexts",
                    "Evaluate human rights impact",
                    "Evaluate cultural values impact",
                    "Document benefit vs harm analysis",
                    "Identify misalignment risks"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Societal & Environmental Impact",
                description="Describe and document how your design choices impact society and the environment, including minimizing resource usage. Estimate resource impact of chosen design and next best design. If next best had less impact, justify your choice. Consider inputs (electricity for training) and outputs (e.g., efficient traffic flows). Conduct similar analysis for societal impact.",
                checklist_items=[
                    "Estimate environmental impact",
                    "Compare design alternatives",
                    "Justify design choice",
                    "Assess societal impact",
                    "Document mitigation strategies"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Data Representation & Ambiguities",
                description="Analyse what the data represents, ambiguities in interpretation and errors. Analyse how each data attribute can be interpreted and how it could indicate different underlying states. Identify nature and scale of measurement errors. Document any ambiguity in data interpretation.",
                checklist_items=[
                    "Analyze data attributes",
                    "Identify interpretation ambiguities",
                    "Document measurement errors",
                    "Assess error scales",
                    "Document interpretation challenges"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Feedback Loop Fairness Analysis",
                description="Identify and estimate fairness issues from biased feedback loops and document the analysis. Where AI models continue learning during operation, feedback loops may develop because previous predictions shape future predictions. Example: if model predicts people with attribute X succeed more in task Y, people lacking X may be denied opportunity, reinforcing the bias.",
                checklist_items=[
                    "Identify feedback mechanisms",
                    "Analyze bias amplification risk",
                    "Document potential loops",
                    "Estimate fairness impact",
                    "Design loop prevention measures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Error & Misuse Fairness Issues",
                description="Identify and estimate fairness issues from foreseeable errors or misuse. Foreseeable errors might include default data settings ('999', '0000'). Foreseeable misuse might include using AI in contexts for which it wasn't designed. Analysis must be documented including consequences of false positives and negatives.",
                checklist_items=[
                    "Identify foreseeable errors",
                    "Identify foreseeable misuse",
                    "Analyze false positive impact",
                    "Analyze false negative impact",
                    "Document all scenarios"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Other AI Lifecycle Fairness Issues",
                description="Identify and estimate any other fairness issues that may arise in the AI system lifecycle and document the analysis. Building on human rights analysis, identify and document fairness risks in build, validate, deploy and post-market phases. Include consideration of children or other vulnerable groups.",
                checklist_items=[
                    "Identify build phase risks",
                    "Identify validation phase risks",
                    "Identify deployment phase risks",
                    "Identify post-market risks",
                    "Consider vulnerable groups",
                    "Document all findings"
                ],
                status=StepStatus.NOT_STARTED
            ),
            # Bias identification questions (Q49-Q54)
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="Selection Bias Identification",
                description="Identify and document sources of selection bias. Selection bias occurs when your data isn't representative of the population due to sampling issues. Justify why you think your data sample is representative of the total population of measurements, and if it isn't, explain what impact on the model this bias will have.",
                checklist_items=[
                    "Analyze sampling methodology",
                    "Compare sample to population",
                    "Identify selection biases",
                    "Document representativeness",
                    "Assess impact on model"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=11,
                title="Historical Bias Identification",
                description="Identify and document sources of historical bias. Historical bias occurs when the population has changed since the data was sampled. Justify why you think your sample is representative of the current population, and if it isn't, explain what impact on the model this bias will have.",
                checklist_items=[
                    "Analyze data collection timing",
                    "Assess population changes",
                    "Identify historical biases",
                    "Document temporal relevance",
                    "Assess impact on model"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=12,
                title="Survivor Bias Identification",
                description="Identify and document sources of Survivor bias. The data sample differs from the population because some members survive longer and so are more likely to be sampled. Justify why you think your sample is not subject to survivor bias, and if it is, explain what impact on the model this bias will have.",
                checklist_items=[
                    "Analyze survival effects",
                    "Identify survivor biases",
                    "Document sampling duration effects",
                    "Assess representativeness",
                    "Assess impact on model"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=13,
                title="Availability Bias Identification",
                description="Identify and document sources of Availability bias. The data available does not statistically reflect the population being modelled. Consider whether data is available that truly reflects the population you are trying to model. Please describe what coverage limitations exist in your data (e.g., Your model is applied to all of Saudi Arabia, but data was only available from one province).",
                checklist_items=[
                    "Analyze data coverage",
                    "Identify geographic limitations",
                    "Identify demographic limitations",
                    "Document availability biases",
                    "Assess impact on model"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=14,
                title="Outlier Bias Identification",
                description="Identify and document sources of Outlier bias. The population has regions dominated by outliers, which region averages fail to capture and leads to inaccuracies. Justify and document why you think your sample is not subject to outlier bias, and if it is, explain what impact on the model this bias will have.",
                checklist_items=[
                    "Analyze data distribution",
                    "Identify outlier-dominated regions",
                    "Document outlier treatment",
                    "Assess representativeness",
                    "Assess impact on model"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=15,
                title="Evaluation Bias Identification",
                description="Identify and document sources of Evaluation bias. The target evaluation dataset is not appropriate for the population (e.g., image recognition AI trained to recognise white faces and applied to a mixed ethnicity population). Justify and document why you think your sample is not subject to evaluation bias, and if it is, explain what impact on the model this bias will have.",
                checklist_items=[
                    "Analyze evaluation data",
                    "Compare to target population",
                    "Identify evaluation biases",
                    "Document appropriateness",
                    "Assess impact on model"
                ],
                status=StepStatus.NOT_STARTED
            ),
            # Bias correction and fairness measures (Q55-Q65)
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=16,
                title="Dataset Bias Correction",
                description="Explain how you have corrected for the sources of weakness and bias in the dataset. Document any additional data you have acquired to mitigate the issues identified and/or new approaches to sampling the population.",
                checklist_items=[
                    "Document correction methods",
                    "Describe additional data acquired",
                    "Explain sampling improvements",
                    "Validate corrections",
                    "Measure improvement"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=17,
                title="Feature Selection Fairness Impact",
                description="Analyse and document the impact of your choice of feature selection on fairness. Document why you believe your selection of model data features were no worse and ideally better than your alternative possible choices, in creating a final model that was free of bias and functions in a safe and fair manner.",
                checklist_items=[
                    "Document feature selection process",
                    "Compare alternative features",
                    "Analyze fairness implications",
                    "Justify feature choices",
                    "Validate fairness impact"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=18,
                title="Champion Model Selection Fairness Impact",
                description="Analyse and document the impact of your choice of champion selection on fairness. Document why you believe your selection of the champion model was no worse and ideally better than your alternative possible choices, in creating a final model that was free of bias and functions in a safe and fair manner.",
                checklist_items=[
                    "Document model selection process",
                    "Compare alternative models",
                    "Analyze fairness implications",
                    "Justify model choice",
                    "Validate fairness impact"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=19,
                title="Develop Fairness Metrics & Thresholds",
                description="Evidence that you have developed Fairness Metrics and defined their acceptable thresholds. Step 1: Define end user segments of groups at risk of discrimination. Step 2: Express model output quantitatively (e.g., sentiment analysis for natural language). Step 3: Define acceptable variability between at-risk segments and population average, set as threshold. Step 4: Create such metrics and thresholds for different parameters characterizing model output.",
                checklist_items=[
                    "Define at-risk user segments",
                    "Quantify model outputs",
                    "Define acceptable thresholds",
                    "Create fairness metrics",
                    "Document metric definitions"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=20,
                title="Feature & Model Choice Impact on Metrics",
                description="Evidence the impact of your choice of feature selection and champion model on the fairness metrics. Referencing the fairness metrics defined previously, analyse and document the impact of your choices of features and champion models on the fairness metrics.",
                checklist_items=[
                    "Measure metrics for chosen features",
                    "Measure metrics for champion model",
                    "Compare to alternatives",
                    "Document impact analysis",
                    "Validate metric compliance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            # Mitigation measures (Q61-Q63)
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=21,
                title="Process Measures for Risk Control",
                description="Design and document your process measures to control the risks identified in the preceding fairness and risk tasks. Describe design changes made to mitigate risks. Where risks cannot be removed by design, describe what controls, human oversight and training you have put in place to manage those risks.",
                checklist_items=[
                    "Document design changes",
                    "Describe control measures",
                    "Define human oversight procedures",
                    "Design training programs",
                    "Validate control effectiveness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=22,
                title="Human Oversight Tools & Processes",
                description="Describe the tools and process you have designed to enable human oversight. Describe how humans will have effective oversight of the AI system - what tools will you give the human operator to help them monitor and understand the system's output? How is the human operator empowered to intervene in the event they detect anomalous or risky processing?",
                checklist_items=[
                    "Design monitoring tools",
                    "Define oversight procedures",
                    "Enable intervention mechanisms",
                    "Document operator empowerment",
                    "Validate oversight effectiveness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=23,
                title="Risk Mitigation & Residual Risk Estimation",
                description="Document your risk mitigation steps & estimate the residual risk and justify why you think it is at an acceptable level. For each risk: Step 1) Estimate impact on individual (1-10), Step 2) Estimate users impacted (1-10), Step 3) Calculate risk without mitigation, Step 4) Describe all mitigating measures, Step 5) Recalculate residual risk with mitigation.",
                checklist_items=[
                    "List all mitigation measures",
                    "Estimate individual impact (1-10)",
                    "Estimate users affected (1-10)",
                    "Calculate unmitigated risk",
                    "Calculate residual risk",
                    "Justify acceptability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            # Validation (Q64, Q66)
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=24,
                title="Validate Fairness Metrics",
                description="Validate that the fairness metrics are within the defined thresholds. Based on the AI model validation data set, document your validation process to test whether the fairness metrics are below their thresholds and record the outcome.",
                checklist_items=[
                    "Test metrics against thresholds",
                    "Document validation methodology",
                    "Record test results",
                    "Identify any exceedances",
                    "Document remediation if needed"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

    def _create_phase5_explainability(self, project_id: str) -> NEOMPhase:
        """Phase 5: Explainability Framework (Questions 71-81) - Simplified for length"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Explainability Framework Introduction",
                description="Write an introduction to the Explainability Framework. Summarise what you did and its outcome.",
                checklist_items=[
                    "Summarize explainability approach",
                    "Document key outcomes",
                    "Provide reader guidance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="AI System Logging Operation",
                description="Design and document the AI System's logging operation. Include when logs are produced, how input data is stored for queries/audits, how system configuration can be discovered, and identity logging of persons verifying AI output.",
                checklist_items=[
                    "Design log creation process",
                    "Define log types and triggers",
                    "Document input data storage",
                    "Enable configuration discovery",
                    "Log verification identities"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Traceability & Auditability",
                description="Explain how you will make AI decisions traceable and auditable. Explain and document how the information from logging can demonstrate whether the AI system was working as intended during specific user interactions.",
                checklist_items=[
                    "Design traceability system",
                    "Enable audit trails",
                    "Link logs to decisions",
                    "Document verification process",
                    "Enable issue investigation"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="User Information for AI Interaction",
                description="Document features and processes to inform users when interacting with AI, emotional recognition, bio categorization or manipulative content. How will you inform users who interact with the AI or its output? Document justification that this information enables effective decision-making. For AI-generated content, include fact-checking against external sources where possible.",
                checklist_items=[
                    "Design user notification system",
                    "Inform about AI interaction",
                    "Inform about biometric use",
                    "Inform about generated content",
                    "Enable fact-checking capability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Residual Risk Communication",
                description="Explain how you will inform operators/users of residual risks and limitations. Document how you will ensure users, operators and deploying entities are aware of identified residual risks after mitigation measures.",
                checklist_items=[
                    "Document residual risks",
                    "Design communication plan",
                    "Inform operators",
                    "Inform end users",
                    "Inform deploying entities"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Stakeholder Explanatory Text & Process",
                description="Write stakeholder explanatory text & process for them to get individual decisions explained. Create explanatory text for end users to understand purpose and impact of AI system. Implement and document a process for end users to get decisions explained.",
                checklist_items=[
                    "Create user-friendly explanatory text",
                    "Document system purpose",
                    "Document system impact",
                    "Design explanation request process",
                    "Define explanation delivery method"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="AI Decision Explainability Design",
                description="Design how you will make AI decisions explainable and communicate with stakeholders. Design & document communication channels. What constitutes an explanation? Include: 1) High-level how AI works, 2) Explanation of what led to specific outcome.",
                checklist_items=[
                    "Define explanation components",
                    "Design communication channels",
                    "Explain AI at high level",
                    "Explain specific outcomes",
                    "Tailor to audience"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Complaints Process Design",
                description="Design a complaints process for end users. Design and document processes that end users, operators and deploying entities can use to lodge a complaint and monitor it until resolution.",
                checklist_items=[
                    "Design complaint submission process",
                    "Define complaint handling workflow",
                    "Enable complaint tracking",
                    "Define resolution procedures",
                    "Document escalation paths"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Operator Instructions",
                description="Document operator instructions for the AI system. Instructions should include: 1) AI system's purpose, 2) Accuracy, robustness and cybersecurity levels in ordinary and extreme circumstances, 3) Conditions of foreseeable misuse leading to risks, 4) Performance regarding intended users/groups, 5) Input data specifications when appropriate, 6) Provider identity and contact details.",
                checklist_items=[
                    "Document system purpose",
                    "Document performance characteristics",
                    "Document misuse scenarios",
                    "Document user group performance",
                    "Specify input data requirements",
                    "Provide provider contact info"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Explainability Framework",
            description="Ensure AI system decisions are explainable, traceable and auditable",
            order=5,
            steps=steps
        )

    def _create_phase6_technology(self, project_id: str) -> NEOMPhase:
        """Phase 6: Technology Development & Robustness (Questions 82-114) - Simplified"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Technology Development Dates",
                description="Please give the dates of the design, data preparation, build & validate, launch and recommended retirement date (DD/MM/YYYY)",
                checklist_items=[
                    "Set design phase dates",
                    "Set data preparation dates",
                    "Set build & validate dates",
                    "Set launch date",
                    "Set retirement date"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Extreme Scenario Testing Data",
                description="Describe the data used to test model performance in extreme scenarios. Describe and document how you established expected data ranges for day-to-day operations. Describe how you ensured training and validation datasets contain sufficient extreme data representing outlier events.",
                checklist_items=[
                    "Define normal data ranges",
                    "Identify extreme scenarios",
                    "Obtain extreme scenario data",
                    "Document data sourcing",
                    "Validate coverage"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="Data Backup Regime",
                description="Design and document the data backup regime and back up the data. Describe and document data backup procedures and processes, and record when these have happened.",
                checklist_items=[
                    "Design backup procedures",
                    "Define backup frequency",
                    "Document backup locations",
                    "Test backup restoration",
                    "Record backup executions"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Model Output Validation",
                description="Validate the model outputs via rigorous methodology. Write up your model validation approach, execution and outcome, including demonstrating the model's robustness to outlier data.",
                checklist_items=[
                    "Design validation methodology",
                    "Execute validation tests",
                    "Test with outlier data",
                    "Document outcomes",
                    "Verify robustness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Input Error Resilience",
                description="High risk AI systems should be resilient to errors in their input. Analyse and document likely input errors, and ensure safeguards prevent harmful outputs (e.g., if input defaults to '0000' or '9999', trigger warning).",
                checklist_items=[
                    "Identify likely input errors",
                    "Design error detection",
                    "Implement safeguards",
                    "Test error handling",
                    "Document error responses"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="System Limitations Documentation",
                description="Describe the known limitations of the AI system. This could include scenarios where system won't perform well, environmental factors, operating factors. For example: input data parameter ranges for reliable operation, maximum data input rate.",
                checklist_items=[
                    "Identify performance limitations",
                    "Document environmental constraints",
                    "Define acceptable parameter ranges",
                    "Document rate limits",
                    "Describe failure modes"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Restricted & Unsupported Use Cases",
                description="Document any restricted use cases (subject to legal or policy restrictions) and unsupported use cases (relevant uses for which system was not designed/evaluated or should be avoided).",
                checklist_items=[
                    "List restricted uses",
                    "Document legal restrictions",
                    "List unsupported uses",
                    "Explain why unsupported",
                    "Define boundaries"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Integration Testing",
                description="Undertake rigorous integration testing, including safeguarding mechanisms. Develop and document an integration plan for the AI system, that includes verification that safeguarding mechanisms are working correctly.",
                checklist_items=[
                    "Develop integration plan",
                    "Test system integration",
                    "Verify safeguards",
                    "Document test results",
                    "Confirm readiness"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Decision Data Retention",
                description="Data upon which key decisions were made should be recorded and retained. Define and document your process for archiving required data and show evidence the process is being operated. Decisions requiring data retention include, but are not limited to, decisions cited in the RACI.",
                checklist_items=[
                    "Define retention policy",
                    "Implement archiving process",
                    "Document RACI decisions",
                    "Demonstrate compliance",
                    "Enable auditability"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="Build & Validate Phase Sign-off",
                description="Secure and document the AI Assessor's sign-off after AI system's build and validation - must sign-off before deployment. Undertake 'Pitstop' with DPO to get 'Build & Validate' phase reviewed. Get sign off from DPO and any other accountable individuals in RACI.",
                checklist_items=[
                    "Schedule Pitstop meeting",
                    "Present build & validation work",
                    "Address DPO feedback",
                    "Obtain DPO sign-off",
                    "Obtain RACI sign-offs"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Technology Development & Robustness",
            description="Validate technical implementation and ensure system robustness",
            order=6,
            steps=steps
        )

    def _create_phase7_monitoring(self, project_id: str) -> NEOMPhase:
        """Phase 7: Post-Market Monitoring (Questions 115-128) - Simplified"""

        steps = [
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=1,
                title="Monitoring Framework Introduction",
                description="Write an introduction to the Monitoring Framework. Summarise what you did and its outcome.",
                checklist_items=[
                    "Summarize monitoring approach",
                    "Document key outcomes",
                    "Provide reader guidance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=2,
                title="Periodic Privacy Assessments",
                description="Define & implement process to periodically conduct fresh Privacy Assessments. Define and record frequency of post-market privacy assessments and document governance process to ensure it occurs.",
                checklist_items=[
                    "Define assessment frequency",
                    "Create assessment process",
                    "Assign responsibilities",
                    "Document governance",
                    "Schedule first assessment"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=3,
                title="ROPA & Privacy Notice Updates",
                description="Evidence that you have implemented a process to update, as necessary, your Record of Processing Activities (ROPA) document and your Privacy Notice.",
                checklist_items=[
                    "Create ROPA update process",
                    "Create Privacy Notice update process",
                    "Define update triggers",
                    "Assign ownership",
                    "Document procedures"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=4,
                title="Periodic Security Assessments",
                description="Define governance and processes to ensure post-market security assessments are periodically conducted and documented. Define and record frequency and governance process to ensure it occurs.",
                checklist_items=[
                    "Define assessment frequency",
                    "Create assessment process",
                    "Assign responsibilities",
                    "Document governance",
                    "Schedule first assessment"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=5,
                title="Resource Usage Monitoring",
                description="Document, design and implement scheme to monitor & reduce resource usage post market. Develop process to monitor post-market resource consumption. Process must include periodic analysis to explore how consumption can be lowered.",
                checklist_items=[
                    "Design monitoring scheme",
                    "Define metrics",
                    "Implement tracking",
                    "Schedule periodic analysis",
                    "Define reduction targets"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=6,
                title="Fairness Metrics Monitoring",
                description="Describe your process to monitor the fairness metrics. Process must include RACI, measurement frequency and governance structure. Measurements must be stored in auditable form.",
                checklist_items=[
                    "Define fairness metrics",
                    "Create measurement process",
                    "Define RACI for monitoring",
                    "Set measurement frequency",
                    "Implement auditable storage"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=7,
                title="Fairness Threshold Exceedance Process",
                description="Define a process to resolve the problem of fairness metrics being above permitted thresholds. Develop and document process including escalation and resolution procedures.",
                checklist_items=[
                    "Define threshold levels",
                    "Create escalation process",
                    "Define resolution procedures",
                    "Assign responsibilities",
                    "Document workflows"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=8,
                title="Periodic Sign-offs",
                description="Get the assessments signed-off periodically. Define, document and operate process to periodically submit metric measurements to DPO for verification and sign-off.",
                checklist_items=[
                    "Define sign-off frequency",
                    "Create submission process",
                    "Define required metrics",
                    "Assign responsibilities",
                    "Document governance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=9,
                title="Human Rights Alignment Monitoring",
                description="Periodically analyse and document the alignment of AI system with human rights and cultural values. Define and document frequency and governance process.",
                checklist_items=[
                    "Define analysis frequency",
                    "Create analysis process",
                    "Define assessment criteria",
                    "Assign responsibilities",
                    "Document governance"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=10,
                title="Human Oversight for High-Risk Cases",
                description="Develop processes to ensure AI output is validated by appropriate named humans for EU defined 'High Risk' use cases. Define, document and operate the process.",
                checklist_items=[
                    "Identify high-risk use cases",
                    "Define validation process",
                    "Assign validators",
                    "Document procedures",
                    "Implement tracking"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=11,
                title="Stakeholder Reporting Process",
                description="Ensure metric reporting, system breakdowns, and breaches are shared with stakeholders. Periodic UI testing should be undertaken and recorded. Design unified process for all stakeholder communications.",
                checklist_items=[
                    "Define reporting frequency",
                    "Create reporting templates",
                    "Define stakeholder list",
                    "Implement UI testing schedule",
                    "Document communication process"
                ],
                status=StepStatus.NOT_STARTED
            ),
            ComplianceStep(
                id=str(uuid.uuid4()),
                order=12,
                title="Lifecycle Change Documentation",
                description="Document any changes made to the system through its lifecycle. Record all versions, updates, and modifications throughout the AI system's operational life.",
                checklist_items=[
                    "Create change log system",
                    "Document version control",
                    "Track configuration changes",
                    "Record update history",
                    "Maintain audit trail"
                ],
                status=StepStatus.NOT_STARTED
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Post-Market Monitoring",
            description="Establish ongoing monitoring and governance for deployed AI system",
            order=7,
            steps=steps
        )
