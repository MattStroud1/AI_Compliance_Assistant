"""
NEOM Building AI Pathway - Updated with Full Regulatory Questions
Based on NEOM Trustworthy AI Playbook compliance requirements
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


class NEOMBuildingAIPathway:
    """
    NEOM-compliant pathway for building trustworthy AI systems
    Based on comprehensive regulatory requirements
    """

    def __init__(self):
        self.pathway_name = "NEOM Building AI"
        self.description = "Comprehensive 4-phase journey for building trustworthy AI systems"

    def create_phases(self, project_id: str) -> List[NEOMPhase]:
        """Create all four NEOM phases with regulatory questions"""
        return [
            self._create_phase_1_planning_design(project_id),
            self._create_phase_2_data_preparation(project_id),
            self._create_phase_3_build_validate(project_id),
            self._create_phase_4_deployment_monitoring(project_id),
        ]

    def _create_step(self, project_id: str, phase: PhaseType, order: int,
                     task_id: str, title: str, description: str, checklist: List[str]) -> ComplianceStep:
        """Helper to create a compliance step"""
        return ComplianceStep(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase=phase,
            order=order,
            title=f"Task {task_id}: {title}",
            description=description,
            status=StepStatus.NOT_STARTED,
            checklist_items=checklist,
            resources=[],
            guidance="",
        )

    def _create_phase_1_planning_design(self, project_id: str) -> NEOMPhase:
        """Phase 1: Planning & Design (Tasks 3.1-3.40)"""

        steps = [
            # RACI Creation - First Step
            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 1, "1.1",                "Create Project RACI Matrix",
                "Create a RACI matrix for your AI project to establish clear roles and responsibilities. The RACI matrix defines who is Responsible, Accountable, Consulted, and Informed for each key task. This ensures proper governance and accountability throughout the AI development lifecycle.",
                [
                    "Click 'Go to RACI Matrix' button below to open the RACI page",
                    "Define team members for each of the 7 key roles",
                    "Review the draft RACI matrix showing task assignments",
                    "Ensure each task has exactly one Accountable person",
                    "Verify all team members understand their roles",
                    "Obtain sign-off from all participants",
                    "Return here to mark this step complete"
                ]
            ),

            # Privacy & Data Governance Framework
            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 2, "3.1",                "High Risk Data Processing Assessment",
                "Does your processing of personal data fall into any of the categories in 'LIST 1' on the introduction Tab? Further, are you processing sensitive data or that relating to children or other vulnerable groups? If so, describe the data, how it is processed and explain why this is necessary.",
                [
                    "Review LIST 1 categories for high-risk processing",
                    "Identify if processing sensitive data (health, biometric, genetic, etc.)",
                    "Identify if processing data of children or vulnerable groups",
                    "Describe the specific data being processed",
                    "Explain how the data is processed",
                    "Justify why processing sensitive data is unavoidable",
                    "Document the necessity for this processing given the AI system's objectives"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 3, "3.2",                "Risk Level Decision and Justification",
                "Decide if the data processing is high risk and justify this decision. See the 'introduction tab' for a definition of high risk data processing. Describe the high level risks associated with your data processing and why this does or does not meet the threshold of high-risk processing. Then select the categorization toggle on the 'introduction tab' to present the right questions for you on this worksheet. Please find guidance from the EU here: https://ec.europa.eu/newsroom/just/document.cfm?doc_id=47711",
                [
                    "Review EU definition of high-risk data processing",
                    "Identify and describe high-level risks of your data processing",
                    "Assess if risks meet the high-risk threshold",
                    "Document decision with clear justification",
                    "Select appropriate risk categorization",
                    "Reference EU guidance in justification"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 4, "3.3",                "Legal Basis for Data Processing",
                "Decide the legal basis upon which you will process the data and document the logic of that decision. The legal basis could be legitimate interest, contract, consent or other. Please see the ICO for guidance (https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/) and then consult with the DPO if necessary. Document the logic of your decision to justify your choice of legal basis.",
                [
                    "Review ICO guidance on lawful basis options",
                    "Consider: legitimate interest, contract, consent, legal obligation, vital interests, or public task",
                    "Consult with DPO if necessary",
                    "Document the logic for chosen legal basis",
                    "Justify why this basis is most appropriate",
                    "Ensure chosen basis aligns with data processing activities"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 5, "3.4",                "Features Supporting Legal Basis",
                "Design and describe any features needed to support the chosen legal basis for the data processing. Analyze, define and document what features, such as consent requests, privacy notices, contract clauses, are needed to enact your chosen legal basis.",
                [
                    "Analyze what features are required for chosen legal basis",
                    "Design consent request mechanisms (if using consent)",
                    "Design privacy notices for transparency",
                    "Define contract clauses (if using contractual basis)",
                    "Document all features needed to enact legal basis",
                    "Ensure features comply with regulatory requirements"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 6, "3.5",                "Privacy Risk Analysis",
                "Analyze and document any privacy risks that may result from your data processing activities. This should include both the risks arising in the normal use of your AI system and in foreseeable cases of misuse. Please consider these for each segment of end user. Consider the potential impact on individuals and any harm or damage your processing may cause – whether physical, emotional or material.",
                [
                    "Analyze privacy risks in normal AI system use",
                    "Identify foreseeable misuse scenarios and their privacy risks",
                    "Consider risks for each user segment separately",
                    "Assess inability to exercise privacy rights",
                    "Assess inability to access services or opportunities",
                    "Assess loss of control over personal data use",
                    "Assess discrimination risks",
                    "Assess identity theft or fraud risks",
                    "Assess financial loss potential",
                    "Assess reputational damage risks",
                    "Assess physical harm potential",
                    "Assess loss of confidentiality",
                    "Assess re-identification of pseudonymized data risks",
                    "Document all identified privacy risks comprehensively"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 7, "3.6",                "Dataset Combination Risks",
                "Document any additional risks arising from combining datasets. If datasets are to be combined, describe what risks arise of individuals becoming identifiable and what new insights might become derivable about individuals. Give consideration to how these risks dependent on the complexity of deriving such insights.",
                [
                    "Identify which datasets will be combined",
                    "Analyze re-identification risks from dataset combination",
                    "Assess what new insights become derivable about individuals",
                    "Evaluate complexity of deriving these insights",
                    "Document correlation risks between datasets",
                    "Consider cumulative privacy impact"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 8, "3.7",                "Privacy Enhancing Technologies (PETs) Justification",
                "Explain why you did or did not use PET's in your design. Describe the opportunities you identified to use PETs in your design, what benefits they could bring, and what issues. Conclude by describing what you chose to implement in your design.",
                [
                    "Identify opportunities to use PETs (encryption, anonymization, etc.)",
                    "Describe benefits PETs could bring to your design",
                    "Identify any issues or limitations with implementing PETs",
                    "Document which PETs you chose to implement",
                    "Justify decision not to use certain PETs (if applicable)",
                    "Explain trade-offs considered in PET decisions"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 9, "3.8",                "Privacy by Design Justification",
                "Justify that your design and operational processes embody privacy by design. Justify that you are using the minimum data required to achieve the purpose and that you are employing anonymization and PETs where possible. Explain how you have informed users about the data processing and whether you've given them the appropriate controls. Explain how you will ensure that the data is protected by adequate cyber-security. Justify any default settings. Describe the organizational process which will ensure your business adheres to this approach.",
                [
                    "Justify use of minimum data required for purpose (data minimization)",
                    "Document anonymization techniques employed",
                    "Describe PETs implementation",
                    "Explain user communication about data processing",
                    "Document controls provided to users",
                    "Describe cybersecurity protections for data",
                    "Justify privacy-protective default settings",
                    "Document organizational processes ensuring privacy by design adherence",
                    "Describe third-party processor privacy safeguards",
                    "Reference ICO Privacy by Design guide"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 10, "3.9",                "Residual Privacy Risk Estimation",
                "Describe any other remediation steps you have taken to mitigate the privacy risks identified and estimate the residual risk. Your analysis should proceed through steps: 1) Estimate the impact of each risk on an individual affected, 2) Estimate the number of users potentially impacted, 3) The resulting level of risk without mitigation, 4) Describe all mitigating measures, 5) Repeat steps 2,3,4 to find the residual risk with mitigation.",
                [
                    "Document additional privacy risk mitigation measures not mentioned in 3.6-3.8",
                    "For each risk from 3.5: estimate impact on individual (scale 1-10)",
                    "For each risk: estimate number/percentage of users impacted (scale 1-10)",
                    "Calculate risk level without mitigation (impact × users impacted)",
                    "Describe all mitigating measures taken",
                    "Re-estimate impact and users impacted with mitigations in place",
                    "Calculate residual risk level (with mitigation)",
                    "Document residual risk assessment"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 11, "3.10",                "Risk-Benefit Balance Justification",
                "Justify why the benefits of the proposed data processing outweigh the residual risk. Your answer should take the form of a balance test, weighing the residual risk against the benefits to the end user and other stakeholders - including wider society.",
                [
                    "Document benefits to end users",
                    "Document benefits to deploying organization",
                    "Document benefits to wider society",
                    "Review residual risks from Task 3.9",
                    "Perform balance test: benefits vs. residual risks",
                    "Justify why benefits outweigh risks",
                    "Document balance test conclusion"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 12, "3.11",                "Compliance Officer Sign-off for High-Risk Systems",
                "If AI system is potentially high risk to individuals, then get sign-off from Compliance Officer. This can be done in the PITSTOP with the PDPO at the end of the Plan and Design phase.",
                [
                    "Review if AI system falls into high-risk categories",
                    "Schedule pitstop meeting with PDPO/Compliance Officer",
                    "Present privacy risk analysis and mitigation",
                    "Obtain sign-off from Compliance Officer",
                    "Document approval in project records"
                ]
            ),

            # Security Governance Framework
            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 13, "3.12",                "Security Methodology Documentation",
                "Document your Security methodology to prevent the AI system being hacked and how you will apply it. Document how do you plan to implement an appropriate security standard embodying a methodology which is endorsed by NEOM CISO; for example ISO 27001. Check with CISO that they agree you are following an appropriate standard.",
                [
                    "Select appropriate security standard (e.g., ISO 27001)",
                    "Confirm standard is endorsed by NEOM CISO",
                    "Document how standard will be applied to AI system",
                    "Describe security methodology to prevent hacking",
                    "Obtain CISO agreement on chosen standard",
                    "Document approval"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 14, "3.13",                "Security Design Features",
                "Describe the features of the AI system's design that make it robust to being hacked. Describe your AI system's security features, such as perimeter security measures, network anomaly monitoring etc, and how they interact to create a robust security posture.",
                [
                    "Document perimeter security measures",
                    "Describe network anomaly monitoring capabilities",
                    "Document authentication and authorization mechanisms",
                    "Describe data encryption (in transit and at rest)",
                    "Document access controls and logging",
                    "Explain how security features interact for robust posture",
                    "Describe defense-in-depth approach"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 15, "3.14",                "AI Algorithm Security Analysis",
                "Write up security aspects of your choice of AI algorithm & what security vulnerabilities might arise as a result. Document why you chose your AI approach and algorithm, and the security implications of that choice. What attack vectors does the choice open up?",
                [
                    "Document chosen AI algorithm/approach",
                    "Justify why this algorithm was selected",
                    "Identify security implications of chosen algorithm",
                    "Document attack vectors opened by this choice",
                    "Assess vulnerability to adversarial examples",
                    "Assess vulnerability to model extraction",
                    "Document algorithm-specific security considerations"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 16, "3.15",                "Adversarial Attack Prevention Measures",
                "Describe the measures taken to prevent adversarial attacks and other input manipulation techniques. These can be used to manipulate the functioning and output of the AI system using the input data consumed by the AI system during its operational life. Describe how you used tools to test for adversarial weaknesses and describe what steps you have taken to harden your model and mitigate these risks.",
                [
                    "Identify potential adversarial attack vectors",
                    "Document tools used to test for adversarial examples",
                    "Describe adversarial testing methodology",
                    "Document model hardening techniques implemented",
                    "Describe input validation and sanitization measures",
                    "Assess impact of mitigation measures",
                    "Document residual adversarial risk"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 17, "3.16",                "Data Poisoning Prevention Measures",
                "Describe the measures taken to prevent data poisoning attacks. These can be used to manipulate the functioning and output of the AI system using the input data consumed by the AI system during the training phase of its build. Describe the measures you have put in place to mitigate the risks of such attacks.",
                [
                    "Describe data quality and integrity measures from data creation to custody",
                    "Document data validation during model training",
                    "Describe data integrity checks during validation stages",
                    "Document post-market data integrity monitoring",
                    "Describe robust model architecture resistant to data poisoning",
                    "Justify proportionality of measures to risk level",
                    "Document data poisoning mitigation strategy"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 18, "3.17",                "Model Inversion Attack Prevention",
                "Describe the measures taken to prevent model inversion attacks and other learning transfer attacks. This is where the attacker can build up a picture of the model's training data based on the model outputs. Your response should include how you are controlling the model outputs and how you will monitor model queries.",
                [
                    "Describe how model access to sensitive data is limited",
                    "Document output control mechanisms (e.g., output granularity limits)",
                    "Explain how output controls impede attacker reconnaissance",
                    "Describe model query monitoring for anomalous behavior",
                    "Document query rate limiting measures",
                    "Justify proportionality of measures to risk of compromise",
                    "Assess residual model inversion risk"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 19, "3.18",                "Residual Security Risk Assessment",
                "Given the security measures implemented, what residual risks do you foresee; how have you mitigated them and what is the residual risk. Justify why further risk mitigation steps were not taken. Your answer should include six steps: 1) Identify the risks, 2) estimate their impact on an individual affected, 3) estimate the percentage of users potentially impacted, 4) estimate the resulting level of risk without mitigating measures, 5) describe your mitigating measures, 6) repeat steps 2,3,4 to find the residual risk.",
                [
                    "Identify all security risks",
                    "For each risk: estimate impact on individual (scale 1-10)",
                    "For each risk: estimate percentage of users impacted",
                    "Calculate risk level without mitigation",
                    "Describe all security mitigating measures",
                    "Re-estimate impact and users impacted with mitigations",
                    "Calculate residual security risk",
                    "Justify why residual risk is acceptable",
                    "Justify why further mitigation was not taken"
                ]
            ),

            # Fairness & Risk Mitigation Framework
            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 20, "3.19",                "Human Rights and Cultural Values Alignment",
                "Analyze and document how the AI system will align to human rights and cultural values. Document your analysis of the diversity of user segments and the range of contexts in which they'd use your AI system. Justify why you think that the benefits of the proposed AI system to the users and wider society will outweigh any harm to the users' human rights and society's cultural values.",
                [
                    "Analyze diversity of user segments",
                    "Document range of contexts for AI system use",
                    "Identify alignment with human rights for each segment",
                    "Identify alignment with cultural values",
                    "Document potential harms to human rights",
                    "Document potential harms to cultural values",
                    "Identify user segments/contexts where alignment may be weak",
                    "Justify that benefits outweigh harms overall"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 21, "3.20",                "Societal and Environmental Impact",
                "Describe and document how your design choices impact society and the environment, including explaining how you are minimizing resource usage. Your description should include at least; an estimate the resource impact of your chosen design on the environment. Repeat this estimate for the next best design. If the next best design had less environmental impact, justify why you chose a design with a greater impact.",
                [
                    "Estimate resource impact (electricity, etc.) of chosen design",
                    "Estimate resource impact of next best alternative design",
                    "Compare environmental impacts of design choices",
                    "If chosen design has greater impact, justify why",
                    "Document impact of model outputs on environment",
                    "Conduct similar analysis for societal impact",
                    "Document resource minimization strategies",
                    "Provide high-level estimates with supporting logic"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 22, "3.21",                "Legal and Ethical Data Acquisition",
                "Evidence that any data used or to be used was acquired legally and ethically - including not breaching copyright. The ethical test should include documenting your justification of why you believe a typical end user would feel processing their sensitive data in the planned way would be fair, reasonable and in their best interests.",
                [
                    "Document data sources and acquisition methods",
                    "Verify data was acquired legally",
                    "Verify no copyright breaches",
                    "Conduct ethical assessment of data acquisition",
                    "Document why typical end user would find processing fair",
                    "Document why processing is reasonable",
                    "Document why processing is in users' best interests",
                    "Obtain necessary data acquisition approvals"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 23, "3.22",                "Fairness Issues Identification",
                "Identify and estimate any other fairness issues that may arise in the AI system life cycle and document the analysis. Building on Task 3.19, identify and document any fairness risks in the model's build, validate, deploy and post-market life-cycle phases. Include consideration of whether children or other vulnerable groups may be at risk.",
                [
                    "Build on Task 3.19 analysis",
                    "Identify fairness risks in build phase",
                    "Identify fairness risks in validation phase",
                    "Identify fairness risks in deployment phase",
                    "Identify fairness risks in post-market phase",
                    "Assess risks to children specifically",
                    "Assess risks to other vulnerable groups",
                    "Document all identified fairness issues",
                    "Reference Trustworthy AI Playbook for issue types"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 24, "3.23",                "Fairness Issues from Errors and Misuse",
                "Identify and estimate any fairness issues that may arise in the AI system life cycle from foreseeable errors or misuse. Foreseeable errors might include the input of default data settings such as '999' or '0000'. Whereas foreseeable misuse might include the AI model being used in common contexts for which it is not designed.",
                [
                    "Identify foreseeable input errors (defaults, null values, etc.)",
                    "Analyze fairness impact of error scenarios",
                    "Identify foreseeable misuse scenarios",
                    "Analyze fairness impact of misuse scenarios",
                    "Consider consequences of false positives",
                    "Consider consequences of false negatives",
                    "Document all error/misuse fairness issues",
                    "Estimate severity and likelihood"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 25, "3.24",                "Biased Feedback Loop Risk",
                "Identify and estimate any fairness issues that may arise in the AI system life cycle from biased feedback loops developing and document the analysis. Where AI models continue to learn during their in-life operation, feedback loops may develop because the model's previous predictions shape its future predictions.",
                [
                    "Determine if model continues learning post-deployment",
                    "Identify potential feedback loop mechanisms",
                    "Analyze how past predictions could bias future predictions",
                    "Document specific feedback loop scenarios",
                    "Assess compounding bias risk over time",
                    "Estimate impact on different user segments",
                    "Document feedback loop fairness risks",
                    "Consider examples like self-fulfilling predictions"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 26, "3.25",                "Risk Control Process Design",
                "Design and document your process measures to control the risks identified in the preceding Tasks 3.19-3.24. Describe the changes to the design you have made to mitigate the risks identified. Where risks cannot be removed by design changes, describe what controls, human oversight and training you have put in place to manage those risks.",
                [
                    "Review all risks from Tasks 3.19-3.24",
                    "Document design changes made to mitigate risks",
                    "For risks not removable by design: document control measures",
                    "Describe human oversight mechanisms",
                    "Document training requirements for operators",
                    "Explain how controls manage residual risks",
                    "Create process documentation for risk management"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 27, "3.26",                "Human Oversight Tools and Processes",
                "Describe the tools and process you have designed to enable human oversight. Describe how humans will have effective oversight of the AI system - what tools will you give the human operator to help them monitor and understand the system's output? How is the human operator empowered to intervene in the event they detect anomalous or risky processing?",
                [
                    "Document tools provided to human operators for monitoring",
                    "Describe how tools help understand system output",
                    "Document intervention mechanisms for operators",
                    "Describe process for detecting anomalous processing",
                    "Document escalation procedures",
                    "Describe operator training on oversight tools",
                    "Explain how intervention authority is granted"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 28, "3.27",                "Residual Risk Estimation and Justification",
                "Document your risk mitigation steps & estimate the residual risk and justify why you think it is at an acceptable level. Your analysis should proceed through steps: 1) Estimate the impact of each risk on an individual affected, 2) Estimate the number of users potentially impacted, 3) The resulting level of risk without mitigation, 4) Describe all mitigating measures, 5) Repeat to find the residual risk with mitigation.",
                [
                    "Review all risks from Tasks 3.19-3.24",
                    "For each risk: estimate impact on individual (scale 1-10)",
                    "For each risk: estimate users impacted (scale 1-10)",
                    "Calculate risk level without mitigation",
                    "Document all mitigating features and processes",
                    "Re-estimate impact and users with mitigations",
                    "Calculate residual risk level",
                    "Justify why residual risk is acceptable"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 29, "3.28",                "Fairness Metrics and Thresholds Development",
                "Evidence that you have developed Fairness Metrics and defined their acceptable thresholds. Step 1: Define end user segments at risk of discrimination. Step 2: Express the model output in a quantitative form. Step 3: Define what degree of variability is acceptable between the segments and set this as the acceptable threshold. Step 4: Create metrics and thresholds for different parameters.",
                [
                    "Define user segments/groups at risk of discrimination",
                    "Express model output in quantitative form (e.g., sentiment scores)",
                    "For each output parameter: define acceptable variability threshold",
                    "Set threshold as acceptable variation from population average",
                    "Create fairness metrics for each output parameter",
                    "Document all metrics and their thresholds",
                    "Justify threshold values chosen"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 30, "3.29",                "Automated Decision Harm Prevention",
                "Document mechanisms to prevent harm from automated decisions. Building on Tasks 3.19 to 3.24, identify and document the harms that may arise from automated decisions, and describe the measures that you have put in place to mitigate these risks.",
                [
                    "Review harms identified in Tasks 3.19-3.24",
                    "Identify additional harms from automated decisions",
                    "Document harm prevention mechanisms",
                    "Describe decision review processes",
                    "Document override capabilities",
                    "Describe harm mitigation measures",
                    "Explain monitoring for harmful decisions"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 31, "3.30",                "Human Governance Process Sign-off",
                "Ensure the right human governance processes are in place and get sign-off from the DPO compliance officer and any other accountable individuals in the RACI. Explain and document whether the output of the AI system may lead to decisions or events that are difficult to reverse, or high impact to the safety or wellbeing of individuals.",
                [
                    "Assess if AI output leads to difficult-to-reverse decisions",
                    "Assess if AI output has high impact on safety/wellbeing",
                    "Document governance process for high-impact decisions",
                    "Ensure human review process for critical decisions",
                    "Document training for human reviewers",
                    "Obtain DPO sign-off on governance processes",
                    "Obtain RACI accountable individuals' sign-off"
                ]
            ),

            # Explainability Framework
            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 32, "3.31",                "User Notification for AI Interactions",
                "Document your features and processes designed to inform users when interacting with AI, emotional recognition, bio categorization or manipulative content. When the AI system results in fake or manipulative content, or leverages biometrics or emotional recognition, how will you inform users who interact with the AI system or its output?",
                [
                    "Identify if system uses emotional recognition",
                    "Identify if system uses bio categorization",
                    "Identify if system can generate manipulative content",
                    "Design user notification mechanisms",
                    "Ensure notifications enable informed decision-making",
                    "For AI-generated content: provide fact-checking capability",
                    "Document notification features and processes",
                    "Justify adequacy of user information"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 33, "3.32",                "Residual Risk and Limitations Communication",
                "Explain how you will inform operators/users of residual risks and limitations. In Task 3.27 we identified the residual risks after mitigation measures have been taken. Document how will you ensure users, operators and deploying entities are aware of these risks.",
                [
                    "Review residual risks from Task 3.27",
                    "Design communication materials for end users",
                    "Design communication materials for operators",
                    "Design communication materials for deploying entities",
                    "Document system limitations clearly",
                    "Ensure communications are understandable",
                    "Document distribution method for risk information"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 34, "3.33",                "AI System Logging Design",
                "Design and document the AI system's logging operation. Design and document the AI System's log creation process, including under what circumstances what types of logs are produced. Describe how the input data is stored to aid resolving queries and audits. Describe how these logs enable the system configuration to be discovered.",
                [
                    "Design log creation process",
                    "Document what circumstances trigger logging",
                    "Document types of logs produced",
                    "Describe input data storage for audit purposes",
                    "Ensure logs capture system configuration (H/W, S/W versions, model parameters)",
                    "Document logging of persons verifying AI output",
                    "Design log retention and access policies"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 35, "3.34",                "Traceability and Auditability",
                "Explain how you will make AI decisions traceable and auditable. Explain and document how the information in Task 3.33 can be used to demonstrate whether the AI system was working as intended during its interaction with a specific user.",
                [
                    "Describe how logs from Task 3.33 enable traceability",
                    "Explain process to trace specific user interactions",
                    "Document how to verify system was working as intended",
                    "Describe audit trail reconstruction process",
                    "Explain how to identify system state at time of decision",
                    "Document auditability verification process"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 36, "3.35",                "AI Decision Explainability Design",
                "Design how you will make AI decisions explainable and communicate with stakeholders. Design & document what communication channels will you use with the users, operators and deploying entities? What constitutes an explanation for the AI system's output? This should include two elements: 1) At a high level how does the AI work? and 2) An explanation of what led to a specific outcome.",
                [
                    "Design communication channels for users",
                    "Design communication channels for operators",
                    "Design communication channels for deploying entities",
                    "Define high-level explanation of how AI works",
                    "Design specific outcome explanation mechanism",
                    "Document what factors are included in explanations",
                    "Ensure explanations are understandable to target audience",
                    "Example: explain what led to specific credit score"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 37, "3.36",                "Complaints Process Design",
                "Design a complaints process for end users. Design and document a process that end users, operators and deploying entities (as appropriate for your AI system) can use to lodge a complaint and monitor that complaint until resolution.",
                [
                    "Design complaint submission mechanism for users",
                    "Design complaint submission for operators (if applicable)",
                    "Design complaint submission for deploying entities (if applicable)",
                    "Document complaint tracking system",
                    "Define complaint resolution process",
                    "Establish resolution timeframes",
                    "Design status monitoring capability for complainants",
                    "Document escalation procedures"
                ]
            ),

            # Technology Development Record
            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 38, "3.37",                "Expected Accuracy, Robustness and Security",
                "Describe why you'd expect your choice of algorithm and broader system design to be sufficiently accurate, robust and secure, even with outlier data or foreseeable cases of misuse. Describe and document the levels of accuracy, reliability and security you believe that your algorithm and AI system will need to achieve.",
                [
                    "Define required accuracy levels for AI system",
                    "Define required reliability levels",
                    "Define required security levels",
                    "Explain why chosen algorithm should achieve these levels",
                    "Justify robustness to outlier data",
                    "Justify robustness to foreseeable misuse",
                    "Document expected performance characteristics"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 39, "3.38",                "Validation Methodology Design",
                "Describe the methodology that you will use to validate this belief described in Task 3.37. Describe and document the testing and validation scheme that you will use to demonstrate the accuracy, reliability and security of both the algorithm and the wider AI system.",
                [
                    "Design validation methodology for accuracy",
                    "Design validation methodology for reliability",
                    "Design validation methodology for security",
                    "Document testing scheme for algorithm",
                    "Document testing scheme for wider system",
                    "Define validation metrics and success criteria",
                    "Describe test data requirements"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 40, "3.39",                "Logging Operation Documentation",
                "Design and document the AI system's logging operation. Design and document the AI System's log creation process, including under what circumstances what types of logs are produced. Describe how the input data is stored to aid resolving queries and audits.",
                [
                    "Design comprehensive logging operation",
                    "Document log creation triggers and circumstances",
                    "Specify types of logs produced",
                    "Describe input data storage for queries/audits",
                    "Document how logs capture configuration details",
                    "Design log retention and archival process",
                    "Ensure logs support auditability requirements"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 41, "3.40",                "Design Phase Sign-off",
                "Get the Design Phase documentation signed off by the AI assessor or Compliance Officer, before proceeding. Undertake a 'Pitstop' with the DPO to get the design phase documentation reviewed, and guidance given for the next phase. Get sign off to proceed from DPO and any other accountable individuals in the RACI.",
                [
                    "Compile all design phase documentation",
                    "Schedule pitstop meeting with DPO/AI Compliance Officer",
                    "Present design phase work for review",
                    "Address any concerns or questions raised",
                    "Obtain sign-off from DPO",
                    "Obtain sign-off from RACI accountable individuals",
                    "Document approvals before proceeding to Phase 2"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,
            name="Planning & Design",
            description="Establish governance, define AI system scope, conduct privacy and security risk assessments, and design fairness and explainability measures",
            order=1,
            steps=steps,
            status=StepStatus.NOT_STARTED,
        )

    def _create_phase_2_data_preparation(self, project_id: str) -> NEOMPhase:
        """Phase 2: Data Preparation (Tasks 4.1-4.18)"""

        steps = [
            # Privacy & Data Governance Framework
            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 1, "4.1",
                "Data Anonymization and PII Justification",
                "Where possible anonymize the data, write up how this was done and explain why the anonymization is robust. If personally identifiable data has to be used, justify why. Explain how you have adhered to best-practice anonymization. For guidance please see the ICO Anonymization 'Code of Practice'. If anonymization is not possible your justification of using identifiable data must take the form of a balance test weighing the risks of its use against the benefits.",
                [
                    "Apply anonymization techniques where possible",
                    "Document anonymization methods used",
                    "Explain robustness of anonymization (re-identification resistance)",
                    "Reference ICO Anonymization Code of Practice",
                    "If using PII: conduct balance test (risks vs. benefits)",
                    "Justify why anonymization is not feasible (if applicable)",
                    "Document anonymization validation testing"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 2, "4.2",
                "Sensitive Data and Proxy Removal",
                "What attempts were made to identify and remove sensitive data and its proxies? Describe the use of any sensitive data. Justify why the different types of non-sensitive data used are not acting as proxies for sensitive data types. For example, proxies for sensitive data can be identified using techniques such as identifying association rules in a dataset.",
                [
                    "Identify all sensitive data in dataset",
                    "Document attempts to remove sensitive data",
                    "Analyze potential proxy variables for sensitive attributes",
                    "Use association rule mining to find proxies (if A, then B patterns)",
                    "Justify use of any sensitive data retained",
                    "Document why non-sensitive data is not acting as proxies",
                    "Remove or mitigate proxy variables identified"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 3, "4.3",
                "Dataset Documentation",
                "Document the dataset that you intend to use, including data categorization, labelling, provenance, structure, quality and the data governance process that underpins the integrity of these classifications and attributes. Your response should include a description of the data model, metadata and data governance framework that you have adhered to. You should also describe what steps you have taken to ensure the data set is error free.",
                [
                    "Document data model and structure",
                    "Describe data categorization scheme",
                    "Document data labeling methodology",
                    "Document data provenance (source, collection method)",
                    "Describe data quality assessment",
                    "Document data governance framework",
                    "Describe metadata standards used",
                    "Document error detection and correction steps",
                    "Create comprehensive data documentation"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 4, "4.4",
                "Data Preparation Phase Archive and Sign-off",
                "Document how you have archived the data associated with the data preparation phase. Then ensure that the data preparation phase is signed off by the project owner and the PDPO Compliance Officer assigned to the project. This should be done at the PDPO 'Pitstop' at the end of the 'Data Preparation' phase.",
                [
                    "Archive all data preparation documentation",
                    "Archive prepared datasets",
                    "Document archival location and access procedures",
                    "Schedule pitstop with PDPO",
                    "Present data preparation work for review",
                    "Obtain project owner sign-off",
                    "Obtain PDPO Compliance Officer sign-off"
                ]
            ),

            # Security Governance Framework
            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 5, "4.5",
                "Data Supply Chain Integrity and IAM",
                "Explain how you have ensured your data supply chain integrity to ensure the training data has not been poisoned. While the data was in your possession, this should include how have you implemented IAM & justify if it is appropriately robust. Building on your answer to Task 3.16, explain how you protected the integrity of the data you actually prepared for the model build phase.",
                [
                    "Review Task 3.16 data poisoning prevention plan",
                    "Document data supply chain integrity measures",
                    "Verify data source authenticity",
                    "Document data integrity checks throughout supply chain",
                    "Describe IAM implementation (authentication, authorization)",
                    "Document access controls for data",
                    "Justify IAM robustness given data sensitivity",
                    "Document differences from Task 3.16 plan (if any)"
                ]
            ),

            # Fairness & Risk Mitigation Framework
            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 6, "4.6",
                "Data Quality and Representativeness",
                "Justify that the data credibility, quality & sample size, is representative and sufficient for the intended purpose. Document the following analysis: 1) Validate the data's quality. 2) Justify that the sample size is adequate for the intended purpose. 3) Justify why you think the data set is representative of the intended end users of the AI system.",
                [
                    "Validate data quality (completeness, accuracy, consistency)",
                    "Document quality validation methodology and results",
                    "Assess sample size adequacy for intended purpose",
                    "Justify sample size with statistical analysis",
                    "Analyze representativeness for intended end users",
                    "Document demographic coverage of dataset",
                    "Justify dataset is representative of target population"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 7, "4.7",
                "Data Interpretation and Measurement Errors",
                "Analyze what the data represents, ambiguities in interpretation and errors. Analyze the ways each data attribute can be interpreted and how it could indicate different underlying states of what's being measured. Further, identify the nature and scale of measurement errors. In the light of these factors, document any ambiguity in how you interpret what the data represents.",
                [
                    "For each key attribute: analyze possible interpretations",
                    "Document what underlying states each attribute could indicate",
                    "Example: temperature reading could indicate weather, fire, or sensor error",
                    "Identify measurement error types and scale",
                    "Document ambiguities in data interpretation",
                    "Assess impact of ambiguities on model",
                    "Document interpretation decisions made"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 8, "4.8",
                "Selection Bias Analysis",
                "Identify and document sources of selection bias. Selection bias - your data isn't representative of the population due to sampling issues from the pool of all measurements available. Justify why you think your data sample is representative of the total population of measurements, and if it isn't, explain what impact on the model this bias will have.",
                [
                    "Analyze sampling methodology for selection bias",
                    "Compare sample demographics to population demographics",
                    "Identify any systematic exclusions in sampling",
                    "Justify sample representativeness or acknowledge bias",
                    "If biased: estimate impact on model performance",
                    "If biased: document which populations may be underserved",
                    "Document selection bias analysis"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 9, "4.9",
                "Historical Bias Analysis",
                "Identify and document sources of historical bias. Historical bias - the population has changed since the data was sampled. Justify why you think your sample is representative of the current population, and if it isn't, explain what impact on the model this bias will have.",
                [
                    "Identify when data was collected",
                    "Analyze how population has changed since collection",
                    "Compare sample to current population",
                    "Justify sample is still representative or acknowledge bias",
                    "If biased: estimate impact on current model performance",
                    "Document temporal validity of data",
                    "Document historical bias analysis"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 10, "4.10",
                "Survivor Bias Analysis",
                "Identify and document sources of Survivor bias. The data sample differs from the population because some members survive longer and so are more likely to be sampled. Justify why you think your sample is not subject to survivor bias, and if it is, explain what impact on the model this bias will have.",
                [
                    "Analyze if sampling methodology favors 'survivors'",
                    "Identify if certain population members are systematically missing",
                    "Assess differential survival/persistence in data",
                    "Justify sample is not subject to survivor bias or acknowledge it",
                    "If biased: estimate impact on model",
                    "Document which groups may be underrepresented",
                    "Document survivor bias analysis"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 11, "4.11",
                "Availability Bias Analysis",
                "Identify and document sources of Availability bias. The data available does not statistically reflect the population being modeled. Task 4.8 asks you to consider whether your sample of data is representative of the population of measurements. This task asks you to consider and document whether data is available that truly reflects the population that you are trying to model.",
                [
                    "Assess if available data truly reflects target population",
                    "Identify geographic coverage limitations",
                    "Example: model for all Saudi Arabia, but data only from one province",
                    "Document data availability constraints",
                    "Identify populations for which data is unavailable",
                    "Justify coverage or acknowledge limitations",
                    "If biased: estimate impact on model generalizability",
                    "Document availability bias analysis"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 12, "4.12",
                "Outlier Bias Analysis",
                "Identify and document sources of Outlier bias. The population has regions dominated by outliers, which region averages fail to capture and leads to inaccuracies. Justify and document why you think your sample is not subject to outlier bias, and if it is, explain what impact on the model this bias will have.",
                [
                    "Identify outliers in dataset",
                    "Analyze if outliers represent real population segments",
                    "Assess if population regions are outlier-dominated",
                    "Determine if averages obscure important variations",
                    "Justify sample is not subject to outlier bias or acknowledge it",
                    "If biased: estimate impact on model for outlier regions",
                    "Document outlier bias analysis and handling"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 13, "4.13",
                "Evaluation Bias Analysis",
                "Identify and document sources of Evaluation bias. The target evaluation dataset is not appropriate for the population. Example: image recognition AI trained to recognize white faces and applied to a mixed ethnicity population. Justify and document why you think your sample is not subject to evaluation bias, and if it is, explain what impact on the model this bias will have.",
                [
                    "Assess if evaluation dataset matches deployment population",
                    "Compare evaluation dataset demographics to target population",
                    "Identify any systematic mismatches",
                    "Justify evaluation dataset is appropriate or acknowledge bias",
                    "If biased: estimate differential performance across groups",
                    "Document which groups may experience lower accuracy",
                    "Document evaluation bias analysis"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 14, "4.15",
                "Bias and Weakness Correction",
                "Explain how you have corrected for the sources of weakness and bias in the dataset. For example: Document any additional data you have acquired to mitigate the issues identified and/or new approaches to sampling the population etc.",
                [
                    "Review biases identified in Tasks 4.8-4.13",
                    "Document additional data acquired to address gaps",
                    "Describe re-sampling or re-weighting techniques used",
                    "Document bias correction algorithms applied",
                    "Explain augmentation techniques used",
                    "Justify correction methods chosen",
                    "Assess effectiveness of bias corrections"
                ]
            ),

            # Technology Development Record
            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 15, "4.16",
                "Extreme Scenario Testing Data",
                "Describe the data used to test model performance in extreme scenarios. Describe and document how you have established the data ranges that you expect your AI model to be input in day to day operations. Further, describe and document how you've ensured that both your training and validation datasets contain sufficient more extreme data representing outlier events.",
                [
                    "Define expected data ranges for day-to-day operations",
                    "Document normal operating parameter ranges",
                    "Identify extreme scenarios relevant to AI system",
                    "Ensure training dataset includes outlier/extreme examples",
                    "Ensure validation dataset includes outlier/extreme examples",
                    "Document proportion of extreme cases in datasets",
                    "Justify adequacy of extreme scenario coverage"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 16, "4.17",
                "Data Backup Regime",
                "Design and document the data backup regime and back up the data. Describe and document your data back up procedures and processes, and record when these have happened.",
                [
                    "Design data backup procedures",
                    "Define backup frequency",
                    "Define backup retention policy",
                    "Document backup storage location(s)",
                    "Document backup verification process",
                    "Perform initial data backup",
                    "Record backup completion date and verification",
                    "Document backup restoration testing"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 17, "4.18",
                "Data Preparation Phase Sign-off",
                "Get the data preparation phase signed off by the AI Compliance Officer. Undertake a 'Pitstop' with the PDPO to get the 'Data Preparation' phase documentation reviewed, and guidance given for the next phase. Get sign off to proceed from PDPO and any other accountable individuals in the RACI.",
                [
                    "Compile all data preparation documentation",
                    "Schedule pitstop meeting with PDPO",
                    "Present data preparation work for review",
                    "Address any concerns raised",
                    "Obtain PDPO sign-off",
                    "Obtain RACI accountable individuals' sign-off",
                    "Document approvals before proceeding to Phase 3"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Data Preparation",
            description="Ensure data quality, identify and mitigate biases, apply privacy-enhancing technologies, and validate data representativeness",
            order=2,
            steps=steps,
            status=StepStatus.NOT_STARTED,
        )

    def _create_phase_3_build_validate(self, project_id: str) -> NEOMPhase:
        """Phase 3: Build & Validate (Tasks 5.1-5.25)"""

        steps = [
            # Technology Development Record
            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 1, "5.1",
                "Training, Validation, and Operational Data Cards",
                "Document the training, validation and operational data with data cards. Ensure that the operational data (expected in-life input) is representative of the training data. Where the operational data is not representative (domain shift) then explain the nature and extent of that domain shift and how you've mitigated the risks of the consequent drop in model performance.",
                [
                    "Create data card for training dataset (purpose, size, characteristics)",
                    "Create data card for validation dataset",
                    "Create data card for expected operational data",
                    "Compare operational data to training data distributions",
                    "Identify any domain shifts between training and operational data",
                    "Document nature and extent of domain shifts",
                    "Describe mitigation measures for domain shift risks",
                    "Assess expected impact on model performance"
                ]
            ),

            # Security Governance Framework
            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 2, "5.2",
                "Hacking Resistance Validation",
                "Validate that your AI system is sufficiently robust to being hacked. Use a reliable service to conduct penetration testing and report this test result. Describe how the pen test was run, the test report results and the mitigations undertaken in the light of those results. Report the residual risk.",
                [
                    "Engage reliable penetration testing service",
                    "Document penetration testing methodology",
                    "Conduct pen testing of AI system",
                    "Document test results and vulnerabilities found",
                    "Implement mitigations for identified vulnerabilities",
                    "Re-test to verify mitigation effectiveness",
                    "Assess and document residual security risk",
                    "Archive penetration test reports"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 3, "5.3",
                "Adversarial Attack Resistance Validation",
                "Validate that your AI system is sufficiently robust to adversarial attacks. Test your trained model against adversarial attack techniques. Describe what mitigation you have implemented to harden the model to adversarial attacks. Report on your testing and evidence the residual risk.",
                [
                    "Select adversarial attack testing tools/frameworks",
                    "Generate adversarial examples for model",
                    "Test model against adversarial attacks",
                    "Document attack success rates and vulnerabilities",
                    "Implement model hardening techniques",
                    "Re-test with hardened model",
                    "Document mitigation effectiveness",
                    "Assess and report residual adversarial risk"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 4, "5.4",
                "Data Poisoning Resistance Validation",
                "Validate that your AI system is sufficiently robust to data poisoning attacks. Test your trained model against poisoned data. Describe what mitigation you have implemented to harden the model to data poisoning. Report on your testing and evidence the residual risk.",
                [
                    "Design data poisoning attack scenarios",
                    "Inject poisoned data into training process",
                    "Test model performance with poisoned data",
                    "Document vulnerability to data poisoning",
                    "Implement data validation and filtering measures",
                    "Implement model architecture hardening",
                    "Re-test with mitigations in place",
                    "Assess and report residual data poisoning risk"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 5, "5.5",
                "Model Inversion Resistance Validation",
                "Validate that your AI system is sufficiently robust to model inversion attacks. Test the ability to extract training data from model outputs. Describe what mitigation you have implemented. Report on your testing and evidence the residual risk.",
                [
                    "Design model inversion attack scenarios",
                    "Attempt to reconstruct training data from outputs",
                    "Document reconstruction success and privacy leakage",
                    "Implement output perturbation or differential privacy",
                    "Implement query monitoring and rate limiting",
                    "Re-test inversion attacks with mitigations",
                    "Document mitigation effectiveness",
                    "Assess and report residual inversion risk"
                ]
            ),

            # Fairness & Risk Mitigation Framework
            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 6, "5.6",
                "Fairness Analysis and Testing Against Metrics",
                "Analyze and test the model for fairness against the metrics defined in Task 3.28. For each metric defined in Task 3.28, measure the performance of the model for each of the demographic groups and compare the results to the acceptable thresholds to test whether the AI system meets the fairness requirements. Report the results.",
                [
                    "Review fairness metrics and thresholds from Task 3.28",
                    "For each demographic group: measure model performance",
                    "For each fairness metric: calculate actual values",
                    "Compare actual metrics to acceptable thresholds",
                    "Document whether AI system meets fairness requirements",
                    "Identify any metrics that fail to meet thresholds",
                    "Report comprehensive fairness testing results"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 7, "5.7",
                "Corrective Actions for Fairness Violations",
                "Where the model violates the fairness metrics, explain what corrective actions you took. For those fairness metrics that were not satisfied in Task 5.6, describe what corrective actions you have taken to improve the model's fairness. Confirm whether those actions were successful and report the resulting fairness metrics.",
                [
                    "Review fairness violations from Task 5.6",
                    "Design corrective actions for each violation",
                    "Implement data rebalancing (if applicable)",
                    "Implement algorithm adjustments (if applicable)",
                    "Implement post-processing bias mitigation",
                    "Re-test fairness metrics after corrections",
                    "Document whether corrections were successful",
                    "Report final fairness metric values"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 8, "5.8",
                "Justification for Residual Fairness Issues",
                "Where significant fairness issues persist, justify why. If fairness metrics still fail to meet thresholds after corrective actions, explain why these residual issues persist and justify why the AI system should still be deployed despite these fairness limitations.",
                [
                    "Identify persisting fairness issues after Task 5.7",
                    "For each persisting issue: explain root cause",
                    "Document technical limitations preventing full correction",
                    "Perform balance test: fairness limitations vs. benefits",
                    "Justify deployment despite fairness limitations",
                    "Document compensating controls or human oversight",
                    "Obtain stakeholder approval for residual fairness risk"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 9, "5.9",
                "AI System Accuracy, Reliability, and Resilience Validation",
                "Validate that your AI system meets the accuracy, reliability and resilience expected and required. Building on the validation methodology described in Task 3.38, test your model and AI system to confirm it is sufficiently accurate, reliable and resilient. Report the test results.",
                [
                    "Review validation methodology from Task 3.38",
                    "Execute accuracy testing with validation dataset",
                    "Document accuracy metrics (precision, recall, F1, etc.)",
                    "Execute reliability testing (consistent results)",
                    "Execute resilience testing (performance with noisy/corrupted input)",
                    "Compare results to required thresholds from Task 3.37",
                    "Document whether AI system meets requirements",
                    "Report comprehensive validation test results"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 10, "5.10",
                "Accuracy, Reliability, Resilience Improvement Actions",
                "Where the model didn't meet thresholds, explain what you did to improve it. For any performance areas where the model failed to meet thresholds in Task 5.9, describe the corrective actions taken (model architecture changes, hyperparameter tuning, additional training data, etc.). Confirm whether those actions were successful.",
                [
                    "Review performance gaps from Task 5.9",
                    "Design improvement actions for each gap",
                    "Implement model architecture changes (if needed)",
                    "Perform hyperparameter tuning",
                    "Acquire additional training data (if needed)",
                    "Re-train model with improvements",
                    "Re-test performance against thresholds",
                    "Document whether improvements were successful"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 11, "5.11",
                "Justification for Residual Performance Limitations",
                "Where significant performance limitations persist, justify why. If performance metrics still fail to meet thresholds after improvement actions, explain why these residual limitations persist and justify why the AI system should still be deployed.",
                [
                    "Identify persisting performance limitations after Task 5.10",
                    "For each limitation: explain root cause",
                    "Document inherent technical constraints",
                    "Perform balance test: limitations vs. benefits",
                    "Justify deployment despite performance limitations",
                    "Document compensating controls (human-in-the-loop, etc.)",
                    "Obtain stakeholder approval for residual performance risk"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 12, "5.12",
                "Build and Validate Phase Sign-off",
                "Get the Build & Validate phase signed off by the AI Compliance Officer. Undertake a 'Pitstop' with the PDPO to get the 'Build & Validate' phase documentation reviewed, and guidance given for the next phase. Get sign off to proceed from PDPO and any other accountable individuals in the RACI.",
                [
                    "Compile all Build & Validate documentation",
                    "Schedule pitstop meeting with PDPO",
                    "Present model performance, fairness, and security results",
                    "Address any concerns raised",
                    "Obtain PDPO sign-off",
                    "Obtain RACI accountable individuals' sign-off",
                    "Document approvals before proceeding to Phase 4"
                ]
            ),

            # Explainability Framework
            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 13, "5.13",
                "Stakeholder Explanations for AI Output",
                "Explain how you will describe the AI system's logic and the explanation for AI outputs to stakeholders. Building on the explainability design from Task 3.35, document the actual explanations you will provide to different stakeholder groups (users, operators, deploying entities) about: 1) How the AI system works at a high level, and 2) What led to specific outputs.",
                [
                    "Review explainability design from Task 3.35",
                    "Create high-level explanation of AI system logic",
                    "Create specific output explanation templates",
                    "Tailor explanations for end users (non-technical language)",
                    "Tailor explanations for operators (operational details)",
                    "Tailor explanations for deploying entities (business/risk context)",
                    "Test explanations with representative stakeholders",
                    "Refine explanations based on feedback"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 14, "5.14",
                "Operator Instructions and Training Materials",
                "Create operator instructions and training materials. Develop comprehensive documentation and training materials for AI system operators covering: how to use the system, how to interpret outputs, when to intervene, escalation procedures, and how to use oversight tools designed in Task 3.26.",
                [
                    "Create operator user manual",
                    "Document step-by-step operating procedures",
                    "Create output interpretation guide",
                    "Document intervention triggers and procedures",
                    "Document escalation procedures",
                    "Create training materials for oversight tools (from Task 3.26)",
                    "Develop hands-on training scenarios",
                    "Create assessment materials to verify operator competency"
                ]
            ),

            # Technology Development Record
            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 15, "5.15",
                "Model Card Documentation",
                "Develop a model card to document the model. Create a comprehensive model card documenting: model architecture, intended use, training data, performance metrics, fairness metrics, limitations, ethical considerations, and recommended use cases.",
                [
                    "Document model architecture and algorithm type",
                    "Document intended use and target users",
                    "Describe training data characteristics",
                    "Report performance metrics from Task 5.9",
                    "Report fairness metrics from Task 5.6",
                    "Document known limitations",
                    "Document ethical considerations",
                    "Define recommended and not-recommended use cases",
                    "Create accessible model card format"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 16, "5.16",
                "Integration Testing",
                "Conduct integration testing of the AI system. Test the AI system integrated with surrounding systems and processes to ensure it functions correctly in the operational environment. Document test scenarios, results, and any issues discovered.",
                [
                    "Define integration test scenarios",
                    "Test AI system with upstream data sources",
                    "Test AI system with downstream consuming systems",
                    "Test end-to-end workflows",
                    "Test error handling and edge cases",
                    "Document integration test results",
                    "Resolve integration issues discovered",
                    "Conduct regression testing after fixes"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 17, "5.17",
                "RACI Matrix Completion and Approval",
                "Complete and obtain approval for the RACI matrix. Finalize the RACI matrix identifying who is Responsible, Accountable, Consulted, and Informed for each key task in AI system operation, monitoring, and governance. Obtain approval from all accountable parties.",
                [
                    "Review and update RACI matrix from planning phase",
                    "Ensure all operational tasks have RACI assignments",
                    "Ensure all monitoring tasks have RACI assignments",
                    "Ensure all governance tasks have RACI assignments",
                    "Verify all individuals accept their assigned roles",
                    "Obtain formal approval from accountable parties",
                    "Document approved RACI matrix",
                    "Communicate RACI assignments to all parties"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 18, "5.18",
                "Data Retention Policy",
                "Define and document the data retention policy. Specify how long different types of data will be retained (training data, operational input, logs, outputs) and justify retention periods based on regulatory, business, and privacy requirements. Document secure deletion procedures.",
                [
                    "Define retention period for training data",
                    "Define retention period for validation data",
                    "Define retention period for operational input data",
                    "Define retention period for AI system outputs",
                    "Define retention period for logs and audit trails",
                    "Justify retention periods (regulatory, business, privacy needs)",
                    "Document secure data deletion procedures",
                    "Implement automated retention enforcement"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 19, "5.19",
                "Incident Response Plan",
                "Develop an incident response plan for AI system failures or issues. Document procedures for detecting, reporting, assessing, responding to, and learning from AI system incidents including: performance degradation, security breaches, fairness violations, and privacy incidents.",
                [
                    "Define incident types and severity levels",
                    "Document incident detection procedures",
                    "Document incident reporting channels",
                    "Define incident assessment procedures",
                    "Document response procedures for each incident type",
                    "Define escalation paths",
                    "Document incident communication procedures",
                    "Define post-incident review and learning process"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 20, "5.20",
                "User Acceptance Testing",
                "Conduct user acceptance testing with representative users. Test the AI system with actual end users or operators in realistic scenarios. Gather feedback on usability, usefulness, trust, and concerns. Document feedback and implement necessary improvements.",
                [
                    "Recruit representative users for testing",
                    "Design realistic test scenarios",
                    "Conduct user acceptance testing sessions",
                    "Gather feedback on usability",
                    "Gather feedback on usefulness and value",
                    "Assess user trust in AI system",
                    "Document user concerns and suggestions",
                    "Implement improvements based on feedback"
                ]
            ),

            # Procurement and Restrictions
            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 21, "5.21",
                "Third-Party Component Documentation",
                "Document all third-party AI components, libraries, and services. If using third-party AI models, APIs, or libraries, document: provider, version, purpose, data sharing, privacy implications, security implications, and licensing. Ensure third parties meet NEOM compliance standards.",
                [
                    "Identify all third-party AI components used",
                    "Document provider and version for each component",
                    "Document purpose and functionality of each component",
                    "Document data sharing with third parties",
                    "Assess privacy implications of third-party components",
                    "Assess security implications of third-party components",
                    "Review licensing agreements",
                    "Verify third-party compliance with NEOM standards"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 22, "5.22",
                "AI System Limitations Documentation",
                "Comprehensively document AI system limitations. Based on all testing and validation, create comprehensive documentation of: what the AI system cannot do, contexts where it should not be used, known failure modes, and situations requiring human intervention.",
                [
                    "Document functional limitations (what AI cannot do)",
                    "Document contexts and use cases where AI should not be used",
                    "Document known failure modes and error patterns",
                    "Document situations requiring mandatory human intervention",
                    "Document accuracy/performance limitations by context",
                    "Document fairness limitations for specific demographics",
                    "Create clear limitation warnings for operators",
                    "Create limitation disclosures for end users"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 23, "5.23",
                "Use Restrictions and Prohibited Contexts",
                "Define and document use restrictions and prohibited contexts. Based on risk assessments and limitations, explicitly define contexts, purposes, or user groups where the AI system must not be used. Implement technical or procedural controls to prevent misuse.",
                [
                    "Review all risk assessments from previous phases",
                    "Define prohibited use contexts explicitly",
                    "Define prohibited purposes",
                    "Identify user groups for whom system is inappropriate",
                    "Document rationale for each restriction",
                    "Design technical controls to enforce restrictions (if possible)",
                    "Design procedural controls and training on restrictions",
                    "Create clear restriction warnings and labels"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 24, "5.24",
                "Environmental Impact Assessment",
                "Assess and document the environmental impact of AI system operation. Calculate or estimate: energy consumption for inference, carbon footprint, resource usage for ongoing operations. Compare to alternatives and justify that environmental impact is minimized.",
                [
                    "Estimate energy consumption per inference",
                    "Calculate total estimated operational energy usage",
                    "Estimate carbon footprint of AI system operation",
                    "Assess resource usage (compute, storage, network)",
                    "Compare environmental impact to alternative solutions",
                    "Justify that impact is minimized given system requirements",
                    "Document energy efficiency optimizations implemented",
                    "Plan for carbon offset (if applicable)"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 25, "5.25",
                "Pre-Deployment Review and Final Approval",
                "Conduct comprehensive pre-deployment review and obtain final approval. Review all documentation, test results, and compliance evidence. Conduct final review meeting with all accountable stakeholders. Obtain final approval to deploy from: project owner, DPO, CISO, and any other RACI accountable individuals.",
                [
                    "Compile complete AI system documentation package",
                    "Review all compliance evidence and sign-offs",
                    "Verify all regulatory requirements are met",
                    "Schedule final pre-deployment review meeting",
                    "Present comprehensive review to stakeholders",
                    "Address any final concerns or conditions",
                    "Obtain project owner final approval",
                    "Obtain DPO final approval",
                    "Obtain CISO final approval",
                    "Obtain all RACI accountable individuals' approval",
                    "Document final approvals with dates and signatures"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Build & Validate",
            description="Train model, validate fairness metrics, implement security measures, and conduct comprehensive testing",
            order=3,
            steps=steps,
            status=StepStatus.NOT_STARTED,
        )

    def _create_phase_4_deployment_monitoring(self, project_id: str) -> NEOMPhase:
        """Phase 4: Deployment & Monitoring (Tasks 6.1-6.33)"""

        steps = [
            # Post-Market Monitoring
            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 1, "6.1",
                "Post-Market Monitoring System Design",
                "Design and document the post-market monitoring system. Describe the processes and tools for continuous monitoring of AI system performance, fairness, security, and privacy in production. Include metrics, thresholds, alerting mechanisms, and review frequency.",
                [
                    "Define key performance indicators (KPIs) to monitor",
                    "Define fairness metrics to monitor continuously",
                    "Define security metrics and anomaly detection",
                    "Define privacy compliance indicators",
                    "Set alert thresholds for each metric",
                    "Document monitoring tool infrastructure",
                    "Define monitoring review frequency",
                    "Establish monitoring dashboard requirements"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 2, "6.2",
                "Performance Degradation Detection",
                "Implement and document performance degradation detection. Describe how you will detect when AI system accuracy, precision, or other performance metrics degrade over time. Define thresholds that trigger investigation and potential model retraining.",
                [
                    "Define baseline performance metrics from validation",
                    "Implement continuous performance measurement",
                    "Set degradation alert thresholds",
                    "Define statistical tests for performance drift",
                    "Document investigation procedures when thresholds breached",
                    "Define criteria triggering model retraining",
                    "Establish performance review schedule",
                    "Document performance degradation response plan"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 3, "6.3",
                "Data Drift Detection",
                "Implement and document data drift detection. Describe how you will detect when operational input data distribution shifts from training data distribution. Define thresholds and response procedures for significant data drift.",
                [
                    "Define baseline data distribution from training",
                    "Implement continuous input data monitoring",
                    "Select data drift detection methods (KL divergence, PSI, etc.)",
                    "Set data drift alert thresholds",
                    "Document investigation procedures for drift detection",
                    "Define criteria for model retraining due to drift",
                    "Establish data distribution review schedule",
                    "Document data drift response plan"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 4, "6.4",
                "Fairness Monitoring and Bias Detection",
                "Implement continuous fairness monitoring. Describe how you will continuously monitor for fairness violations and emerging bias in production. Define procedures for investigating and correcting fairness issues discovered post-deployment.",
                [
                    "Review fairness metrics from Task 3.28 and 5.6",
                    "Implement continuous fairness metric calculation",
                    "Monitor fairness across demographic groups",
                    "Set fairness violation alert thresholds",
                    "Document investigation procedures for fairness alerts",
                    "Define corrective action procedures",
                    "Establish fairness review meeting schedule",
                    "Document fairness incident response plan"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 5, "6.5",
                "Security Monitoring and Incident Response",
                "Implement security monitoring and incident response. Describe continuous monitoring for security threats including: unauthorized access attempts, adversarial attacks, data poisoning attempts, and anomalous queries. Document security incident response procedures.",
                [
                    "Implement access attempt monitoring and logging",
                    "Implement adversarial input detection",
                    "Monitor for data poisoning attempts",
                    "Implement query pattern anomaly detection",
                    "Set security alert thresholds",
                    "Document security incident classification",
                    "Document incident response procedures by severity",
                    "Define escalation paths for security incidents"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 6, "6.6",
                "Privacy Compliance Monitoring",
                "Implement privacy compliance monitoring. Describe continuous monitoring of privacy controls including: data access logging, consent compliance, data retention compliance, and privacy incident detection. Document privacy incident response.",
                [
                    "Implement data access logging and monitoring",
                    "Monitor consent withdrawal requests and compliance",
                    "Monitor data retention policy compliance",
                    "Detect potential privacy incidents or leakage",
                    "Set privacy compliance alert thresholds",
                    "Document privacy incident classification",
                    "Document privacy incident response procedures",
                    "Establish privacy compliance review schedule"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 7, "6.7",
                "User Feedback and Complaint Tracking",
                "Implement user feedback and complaint tracking system. Building on the complaints process from Task 3.36, implement systems to collect, track, analyze, and respond to user feedback and complaints. Define procedures for addressing systemic issues identified through feedback.",
                [
                    "Implement feedback collection mechanisms",
                    "Implement complaint tracking system from Task 3.36",
                    "Define feedback categorization taxonomy",
                    "Establish feedback analysis procedures",
                    "Define response timeframes by complaint severity",
                    "Document procedures for identifying systemic issues",
                    "Establish feedback review meeting schedule",
                    "Document feedback-driven improvement process"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 8, "6.8",
                "Audit Trail and Logging Review",
                "Implement audit trail review processes. Describe procedures for regular review of AI system logs and audit trails. Define what is reviewed, review frequency, who conducts reviews, and procedures for investigating anomalies.",
                [
                    "Define audit log review scope",
                    "Establish log review frequency",
                    "Assign log review responsibilities (RACI)",
                    "Define procedures for anomaly investigation",
                    "Document log retention and archival",
                    "Establish log review reporting procedures",
                    "Define escalation procedures for serious findings",
                    "Document audit trail review documentation"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 9, "6.9",
                "Model Retraining and Update Process",
                "Define and document the model retraining and update process. Describe criteria triggering retraining, retraining procedures, validation requirements for updated models, and deployment process for model updates. Ensure updates maintain compliance.",
                [
                    "Define criteria triggering model retraining",
                    "Document data collection for retraining",
                    "Document retraining validation requirements",
                    "Require fairness re-validation for updated models",
                    "Require security re-validation for updated models",
                    "Define A/B testing or shadow deployment for updates",
                    "Document rollback procedures if issues arise",
                    "Require compliance review before deploying updates"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 10, "6.10",
                "Periodic Compliance Reviews",
                "Establish periodic comprehensive compliance review process. Define schedule and procedures for comprehensive reviews of all compliance aspects: privacy, security, fairness, explainability, documentation. Document review participants, outputs, and follow-up procedures.",
                [
                    "Define comprehensive compliance review schedule (quarterly/annual)",
                    "Identify review participants (DPO, CISO, project owner, etc.)",
                    "Define review scope: privacy, security, fairness, explainability",
                    "Document review procedures and checklists",
                    "Define review outputs and documentation requirements",
                    "Establish follow-up procedures for findings",
                    "Document corrective action tracking",
                    "Require sign-off from DPO and CISO"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 11, "6.11",
                "Continuous Improvement Process",
                "Establish continuous improvement process for AI system. Document how monitoring results, feedback, incidents, and reviews drive continuous improvements to the AI system, processes, and documentation. Define improvement prioritization and implementation procedures.",
                [
                    "Define sources of improvement opportunities",
                    "Establish improvement proposal process",
                    "Define improvement prioritization criteria",
                    "Document improvement evaluation process",
                    "Define improvement implementation procedures",
                    "Require compliance review for significant changes",
                    "Document improvement tracking and reporting",
                    "Establish lessons learned documentation"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 12, "6.12",
                "Regulatory Change Monitoring",
                "Implement regulatory and standards change monitoring. Describe how you will monitor for changes in relevant regulations (EU AI Act, GDPR, NEOM requirements, etc.) and standards. Define procedures for assessing impact and implementing necessary updates.",
                [
                    "Identify relevant regulations and standards to monitor",
                    "Assign responsibility for regulatory monitoring",
                    "Define monitoring frequency and sources",
                    "Document procedures for impact assessment",
                    "Define procedures for implementing regulatory changes",
                    "Establish regulatory compliance review schedule",
                    "Document regulatory change communication process",
                    "Maintain regulatory compliance register"
                ]
            ),

            # EU AI Act Technical Documentation
            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 13, "6.13",
                "General Description of AI System",
                "Provide a general description of the AI system. Document: intended purpose, business context, deployment environment, user segments, geographic scope, and how the system fits into broader organizational processes.",
                [
                    "Document AI system intended purpose clearly",
                    "Describe business context and objectives",
                    "Document deployment environment (cloud, edge, on-premise)",
                    "Define and describe all user segments",
                    "Document geographic scope of deployment",
                    "Describe integration with organizational processes",
                    "Document system boundaries and interfaces",
                    "Create high-level system architecture diagram"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 14, "6.14",
                "Detailed Description of System Elements",
                "Provide detailed description of AI system elements and components. Document: all software components, hardware requirements, data sources, external APIs/services, and how components interact. Include version information.",
                [
                    "Document all software components and libraries",
                    "Document component versions",
                    "Document hardware requirements and specifications",
                    "Document data sources and interfaces",
                    "Document external APIs and services used",
                    "Document inter-component communication",
                    "Create detailed architecture diagrams",
                    "Document dependencies and requirements"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 15, "6.15",
                "Design Specifications and Training Methodology",
                "Document design specifications and training methodology. Describe: model architecture choices, training algorithm, hyperparameters, training procedure, validation methodology, and rationale for design decisions.",
                [
                    "Document model architecture in detail",
                    "Document training algorithm and methodology",
                    "Document hyperparameters and tuning process",
                    "Document training procedure step-by-step",
                    "Document validation methodology",
                    "Justify key design decisions",
                    "Document computational requirements",
                    "Reference design rationale from Task 3.37"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 16, "6.16",
                "Data Requirements and Characteristics",
                "Document comprehensive data requirements and characteristics. Describe: required input data format, data quality requirements, data preprocessing, expected data ranges, handling of out-of-range data, and data validation.",
                [
                    "Document required input data format and schema",
                    "Document data quality requirements",
                    "Document data preprocessing steps",
                    "Document expected data ranges (from Task 4.16)",
                    "Document handling of out-of-range data",
                    "Document data validation procedures",
                    "Document data dependencies",
                    "Reference data cards from Task 5.1"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 17, "6.17",
                "Training Data Description",
                "Comprehensively document training data. Describe: data sources, data collection methodology, data size and characteristics, data labeling process, data quality, representativeness assessment, and bias analysis.",
                [
                    "Reference data cards from Task 5.1",
                    "Document training data sources",
                    "Document data collection methodology",
                    "Document dataset size and characteristics",
                    "Document data labeling process and quality",
                    "Reference representativeness analysis from Task 4.6",
                    "Reference bias analysis from Tasks 4.8-4.13",
                    "Document data quality validation"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 18, "6.18",
                "Validation and Testing Data Description",
                "Document validation and testing data. Describe: validation dataset characteristics, test dataset characteristics, how datasets differ from training data, extreme scenario test data, and rationale for dataset composition.",
                [
                    "Reference data cards from Task 5.1",
                    "Document validation dataset characteristics",
                    "Document test dataset characteristics",
                    "Document how validation/test differ from training",
                    "Reference extreme scenario data from Task 4.16",
                    "Document dataset composition rationale",
                    "Document dataset quality assurance",
                    "Ensure datasets are representative per Task 4.6"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 19, "6.19",
                "Performance Metrics and Evaluation Results",
                "Document performance metrics and evaluation results. Report: accuracy, precision, recall, F1, AUC, and other relevant metrics. Include performance across different user segments and contexts. Reference validation testing from Task 5.9.",
                [
                    "Reference validation results from Task 5.9",
                    "Document all accuracy metrics (precision, recall, F1, etc.)",
                    "Document performance across user segments",
                    "Document performance in different contexts",
                    "Document reliability metrics",
                    "Document resilience metrics",
                    "Compare performance to required thresholds from Task 3.37",
                    "Document any performance limitations"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 20, "6.20",
                "Fairness Metrics and Evaluation Results",
                "Document fairness metrics and evaluation results. Report fairness metrics defined in Task 3.28, results from testing in Task 5.6, and any corrective actions from Task 5.7. Document residual fairness limitations.",
                [
                    "Reference fairness metrics from Task 3.28",
                    "Reference fairness testing results from Task 5.6",
                    "Document fairness across demographic groups",
                    "Document corrective actions from Task 5.7",
                    "Document residual fairness limitations from Task 5.8",
                    "Justify deployment despite limitations (if applicable)",
                    "Document ongoing fairness monitoring from Task 6.4",
                    "Reference fairness in model card from Task 5.15"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 21, "6.21",
                "Cybersecurity Measures Documentation",
                "Comprehensively document cybersecurity measures. Describe all security controls including: access controls, encryption, network security, monitoring, penetration testing results, and security risk assessment. Reference security validation from Phase 3.",
                [
                    "Reference security methodology from Task 3.12",
                    "Document all security controls implemented",
                    "Reference security design from Task 3.13",
                    "Reference penetration testing from Task 5.2",
                    "Reference adversarial testing from Task 5.3",
                    "Reference data poisoning testing from Task 5.4",
                    "Reference model inversion testing from Task 5.5",
                    "Document residual security risks from Task 3.18"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 22, "6.22",
                "Privacy Measures and DPIA Summary",
                "Document privacy measures and Data Protection Impact Assessment (DPIA) summary. Describe all privacy controls, reference privacy risk analysis, document legal basis, and summarize DPIA outcomes. Reference privacy work from Phase 1 and 2.",
                [
                    "Reference legal basis from Task 3.3",
                    "Reference privacy risk analysis from Task 3.5-3.10",
                    "Document all privacy-enhancing technologies from Task 3.7",
                    "Reference privacy by design from Task 3.8",
                    "Reference anonymization from Task 4.1",
                    "Document data minimization measures",
                    "Summarize DPIA outcomes and approvals",
                    "Document privacy incident response from Task 6.6"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 23, "6.23",
                "Risk Assessment Summary",
                "Provide comprehensive risk assessment summary. Consolidate all risk assessments from privacy, security, fairness, and performance. Document residual risks and justifications. Reference risk analysis throughout all phases.",
                [
                    "Consolidate privacy risks from Tasks 3.5-3.10",
                    "Consolidate security risks from Tasks 3.12-3.18",
                    "Consolidate fairness risks from Tasks 3.19-3.30",
                    "Consolidate performance risks from Tasks 3.37, 5.9-5.11",
                    "Document all residual risks with justifications",
                    "Document risk mitigation measures",
                    "Create comprehensive risk register",
                    "Document risk acceptance sign-offs"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 24, "6.24",
                "Human Oversight Measures Documentation",
                "Document all human oversight measures. Describe oversight tools, processes, training, intervention capabilities, and escalation procedures. Reference human oversight design from Tasks 3.26 and 3.30.",
                [
                    "Reference oversight tools from Task 3.26",
                    "Reference governance processes from Task 3.30",
                    "Document operator training from Task 5.14",
                    "Document intervention triggers and procedures",
                    "Document escalation paths",
                    "Document oversight monitoring and reporting",
                    "Document high-impact decision review process",
                    "Document human-in-the-loop procedures"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 25, "6.25",
                "Accuracy and Robustness Specifications",
                "Document accuracy and robustness specifications. Define expected accuracy levels, robustness to outliers, handling of edge cases, and performance under adversarial conditions. Reference performance validation from Phase 3.",
                [
                    "Reference accuracy requirements from Task 3.37",
                    "Reference validation results from Task 5.9",
                    "Document expected accuracy specifications",
                    "Document robustness to outliers from Task 4.16",
                    "Document edge case handling",
                    "Reference adversarial robustness from Task 5.3",
                    "Document performance degradation detection from Task 6.2",
                    "Define minimum acceptable performance levels"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 26, "6.26",
                "Explainability and Transparency Documentation",
                "Document explainability and transparency measures. Describe how AI decisions are explained to different stakeholders, what information is provided, and how transparency is maintained. Reference explainability work from Tasks 3.31-3.36 and 5.13.",
                [
                    "Reference user notifications from Task 3.31",
                    "Reference risk communication from Task 3.32",
                    "Reference logging from Task 3.33",
                    "Reference traceability from Task 3.34",
                    "Reference decision explanations from Task 3.35",
                    "Reference stakeholder explanations from Task 5.13",
                    "Document explanation methodology",
                    "Document transparency measures for operators and users"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 27, "6.27",
                "Instructions for Use Documentation",
                "Create comprehensive instructions for use. Provide detailed instructions for: deployment, operation, monitoring, maintenance, troubleshooting, and decommissioning. Target different audiences: deploying entities, operators, and end users.",
                [
                    "Create deployment instructions",
                    "Create operation instructions (reference Task 5.14)",
                    "Create monitoring instructions (reference Task 6.1)",
                    "Create maintenance procedures",
                    "Create troubleshooting guide",
                    "Create decommissioning procedures",
                    "Tailor instructions for deploying entities",
                    "Tailor instructions for operators",
                    "Tailor instructions for end users"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 28, "6.28",
                "System Limitations and Restrictions",
                "Comprehensively document system limitations and restrictions. Consolidate limitations from Task 5.22, restrictions from Task 5.23, and any other constraints. Ensure limitations are clearly communicated in all documentation.",
                [
                    "Reference limitations from Task 5.22",
                    "Reference restrictions from Task 5.23",
                    "Document functional limitations clearly",
                    "Document context-specific limitations",
                    "Document prohibited use cases",
                    "Document user segment restrictions",
                    "Ensure limitations in instructions for use",
                    "Ensure limitations in model card"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 29, "6.29",
                "Change Management Process Documentation",
                "Document change management process for AI system. Define procedures for: proposing changes, assessing change impact, compliance review for changes, testing requirements, approval process, and change documentation.",
                [
                    "Define change proposal process",
                    "Define change impact assessment procedures",
                    "Define compliance review requirements for changes",
                    "Define testing requirements for changes",
                    "Define change approval process and authorities",
                    "Document change implementation procedures",
                    "Define rollback procedures",
                    "Define change documentation requirements"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 30, "6.30",
                "Incident Management and Reporting",
                "Document incident management and reporting procedures. Consolidate incident procedures from Task 5.19 and monitoring tasks. Define incident classification, reporting obligations, investigation procedures, and corrective actions.",
                [
                    "Reference incident response plan from Task 5.19",
                    "Document incident classification taxonomy",
                    "Define regulatory reporting obligations",
                    "Define internal reporting procedures",
                    "Document incident investigation procedures",
                    "Define corrective action procedures",
                    "Document incident documentation requirements",
                    "Define post-incident review process"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 31, "6.31",
                "Record Keeping and Documentation Maintenance",
                "Establish record keeping and documentation maintenance procedures. Define what records must be kept, retention periods, access controls, update procedures, and archival processes. Ensure compliance with regulatory requirements.",
                [
                    "Define records to be maintained",
                    "Reference data retention policy from Task 5.18",
                    "Define documentation retention periods",
                    "Define access controls for records",
                    "Define documentation update procedures",
                    "Define version control procedures",
                    "Define archival and retrieval procedures",
                    "Ensure compliance with regulatory record-keeping requirements"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 32, "6.32",
                "Conformity Assessment and CE Marking (if applicable)",
                "Conduct conformity assessment for EU AI Act compliance (if applicable). Assess conformity with EU AI Act requirements, compile technical documentation, conduct or commission conformity assessment, and obtain CE marking if required.",
                [
                    "Determine if AI system requires CE marking under EU AI Act",
                    "Compile complete technical documentation package",
                    "Review all regulatory requirements for conformity",
                    "Conduct self-assessment or engage notified body",
                    "Document conformity assessment process",
                    "Address any non-conformities identified",
                    "Obtain CE marking (if required)",
                    "Maintain conformity documentation"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 33, "6.33",
                "Final Documentation Package and Ongoing Compliance",
                "Compile final comprehensive documentation package and establish ongoing compliance. Ensure all documentation is complete, up-to-date, accessible, and maintained. Obtain final sign-offs from all stakeholders. Establish ongoing compliance maintenance.",
                [
                    "Compile complete documentation package",
                    "Verify all compliance requirements are documented",
                    "Verify all sign-offs are obtained",
                    "Ensure documentation is accessible to required parties",
                    "Establish documentation maintenance procedures",
                    "Assign documentation ownership responsibilities",
                    "Schedule periodic documentation reviews",
                    "Obtain final deployment approval from project owner, DPO, and CISO",
                    "Document deployment date and configuration",
                    "Establish ongoing compliance reporting"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Deployment & Monitoring",
            description="Deploy AI system with monitoring, ensure ongoing compliance, and maintain documentation",
            order=4,
            steps=steps,
            status=StepStatus.NOT_STARTED,
        )
