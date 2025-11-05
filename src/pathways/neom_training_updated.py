"""
NEOM Training on AI Pathway - Interactive Learning Course
Based on the Trustworthy AI Playbook and compliance requirements
Organized by 7 topic-based chapters (not phases)
"""

from typing import List
from datetime import datetime
import uuid

from ..models import (
    ComplianceStep,
    StepStatus,
    NEOMPhase,
    PhaseType,
)


class TrainingChapter:
    """Represents a training chapter with learning objectives and assessments"""

    def __init__(self, chapter_id: int, title: str, description: str):
        self.chapter_id = chapter_id
        self.title = title
        self.description = description


class NEOMTrainingPathway:
    """
    NEOM-compliant pathway for learning about trustworthy AI
    Based on comprehensive Trustworthy AI Playbook
    Organized by 7 topic-based chapters
    """

    def __init__(self):
        self.pathway_name = "NEOM Training on AI"
        self.description = "Comprehensive 7-chapter course for learning trustworthy AI principles and compliance"

    def create_chapters(self, project_id: str) -> List[NEOMPhase]:
        """Create all seven training chapters as NEOMPhase objects"""
        chapters = []

        # Chapter 1
        chapter1_steps = self._create_chapter_1_introduction(project_id)
        chapters.append(NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,  # Use planning for chapter 1
            name="Chapter 1: Introduction & Overview",
            description="Why Trustworthy AI Matters",
            order=1,
            steps=chapter1_steps
        ))

        # Chapter 2
        chapter2_steps = self._create_chapter_2_data_privacy(project_id)
        chapters.append(NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,
            name="Chapter 2: Data & Privacy",
            description="Implementing privacy by design and good data governance",
            order=2,
            steps=chapter2_steps
        ))

        # Chapter 3
        chapter3_steps = self._create_chapter_3_security(project_id)
        chapters.append(NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Chapter 3: Security",
            description="AI-specific security threats and countermeasures",
            order=3,
            steps=chapter3_steps
        ))

        # Chapter 4
        chapter4_steps = self._create_chapter_4_risk_fairness(project_id)
        chapters.append(NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Chapter 4: Risk & Fairness",
            description="Identifying biases and implementing fairness metrics",
            order=4,
            steps=chapter4_steps
        ))

        # Chapter 5
        chapter5_steps = self._create_chapter_5_explainability(project_id)
        chapters.append(NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Chapter 5: Explainability",
            description="Making AI decisions transparent and understandable",
            order=5,
            steps=chapter5_steps
        ))

        # Chapter 6
        chapter6_steps = self._create_chapter_6_tech_development_record(project_id)
        chapters.append(NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Chapter 6: Technology Development Record",
            description="Comprehensive documentation requirements",
            order=6,
            steps=chapter6_steps
        ))

        # Chapter 7
        chapter7_steps = self._create_chapter_7_post_market_monitoring(project_id)
        chapters.append(NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Chapter 7: Post Market Monitoring",
            description="Continuous monitoring and compliance assessments",
            order=7,
            steps=chapter7_steps
        ))

        return chapters

    def _create_step(self, project_id: str, chapter_num: int, order: int,
                     title: str, description: str, checklist: List[str]) -> ComplianceStep:
        """Helper to create a training step"""
        return ComplianceStep(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase=None,  # Training uses chapters, not phases
            order=order,
            title=f"Chapter {chapter_num}: {title}",
            description=description,
            status=StepStatus.NOT_STARTED,
            checklist_items=checklist,
            resources=[],
            guidance="",
        )

    def _create_chapter_1_introduction(self, project_id: str) -> List[ComplianceStep]:
        """Chapter 1: Introduction & Overview"""

        return [
            self._create_step(
                project_id, 1, 1,
                "Introduction & Overview - Why Trustworthy AI Matters",
                """**The Challenge of "Working" AI**

Imagine that you've just developed a new AI model powering some fantastic service. Your AI model is churning out predictions, and everything is working brilliantly. But what do we mean by "working"?

Is a credit risk algorithm which uses postcode as a feature and so is implicitly influenced by race, working? What about Facebook's algorithm which drives user engagement, while polarizing society, is that working? Would you want to buy a bulletproof vest that's 80% effective... or only protects some types of people?

For an AI system to be described as "working", it needs to do more than produce the right outcome some of the time, for some people, without knowing when or for whom. **If we fail to do that, the system is not really working at all.**

**The Business Case for Trustworthy AI:**
- 72% of consumers say that "knowing a company's AI policies before making a purchase is important"
- Companies focused on data protection and AI Ethics grow on average **1.6x faster**
- Ethical AI practices result in AI that **truly works**

**The Compliance Stick:**
- The EU AI Act: 123 pages of processes, documents, and controls
- Saudi Arabia's SDAIA: 46 pages of AI Ethics Principles
- Failure to comply can result in significant penalties""",
                [
                    "Understand what it means for an AI system to truly 'work'",
                    "Learn why 72% of consumers care about AI policies",
                    "Understand the 1.6x growth advantage of ethical AI companies",
                    "Review the EU AI Act's 123 pages of requirements",
                    "Review SDAIA's 46 pages of AI Ethics Principles",
                    "Understand NEOM's three-document framework (Playbook, Compliance Tool, Toolbox)",
                    "Learn about the pitstop meeting process",
                    "Complete Chapter 1 quiz"
                ]
            ),
        ]

    def _create_chapter_2_data_privacy(self, project_id: str) -> List[ComplianceStep]:
        """Chapter 2: Data & Privacy"""

        return [
            self._create_step(
                project_id, 2, 2,
                "Data & Privacy - RACI and Governance",
                """**Implementing Privacy by Design and Good Data Governance**

This section focuses on ensuring and evidencing good data governance and the implementation of "privacy by design". This starts with establishing clear governance structures, determining legal basis for processing, and implementing features to support privacy.

**RACI Matrix:**
At the start of the project, establish a RACI (Responsible, Accountable, Consulted, Informed) matrix and get buy-in from those named on it. Make the RACI specific, including what decisions and sign-offs each person is responsible for. Do not leave gaps or ambiguity.

**Critical Data Governance Roles:**
1. **Data Owner** - Authority over data assets, makes decisions about data access and usage
2. **Data Steward** - Manages day-to-day data operations and implements data policies
3. **Data Custodian** - Responsible for technical storage, security, and access controls

Each role should operate within a clear and well-documented Data Governance Framework. The RACI must be kept up to date throughout the project.""",
                [
                    "Understand what 'privacy by design' means",
                    "Learn the three critical data governance roles",
                    "Understand how to establish a RACI matrix",
                    "Learn why specificity in RACI assignments prevents gaps",
                    "Understand the Data Governance Framework requirements",
                    "Learn about version control for RACI matrices"
                ]
            ),
            self._create_step(
                project_id, 2, 3,
                "Data & Privacy - Sensitive Data and Legal Basis",
                """**Understanding Sensitive Data**

An early step in the design process is to determine whether your data includes sensitive data or data of children.

**Sensitive data relates to (PDPL & GDPR):**
- Ethnic or tribal origin
- Religious, intellectual, or political beliefs
- Civil association membership
- Security and criminal data
- Biometric data for identification
- Genetic data and health data
- Location data and financial data
- Trade union membership (GDPR)
- Sexual orientation or sex life (GDPR)

**Children's Data:** Under 13 years (PDPL) or 16 years (GDPR)

**Legal Basis for Processing:**
The three most common legal bases are:
1. **Legitimate Interest** - Requires a Legitimate Interest Assessment (LIA)
2. **Contract** - Appropriate clauses in contracts
3. **Consent** - Requires mechanisms to capture consent

**Note:** You cannot process sensitive data on the legal basis of legitimate interest.""",
                [
                    "Identify what constitutes sensitive data under PDPL",
                    "Identify additional sensitive data categories under GDPR",
                    "Understand children's data age thresholds (13 for PDPL, 16 for GDPR)",
                    "Learn the three common legal bases for processing",
                    "Understand the Legitimate Interest Assessment (LIA) three-question test",
                    "Learn why sensitive data cannot use Legitimate Interest as legal basis",
                    "Understand how to design features to support chosen legal basis"
                ]
            ),
            self._create_step(
                project_id, 2, 4,
                "Data & Privacy - Privacy Impact Assessments (PIA)",
                """**When Privacy Impact Assessments Are Required**

You must determine whether your proposed data processing represents "high-risk" processing. This risk is high when, considering the nature, scope, context and purposes of the processing, it is likely to result in a high risk to the rights and freedoms of natural persons.

**Types of processing likely to be high risk:**
- Systematic and extensive profiling with significant effects
- Large-scale use of sensitive data
- Public monitoring
- Evaluation or scoring with legal/significant effects
- Automated decision-making with legal/significant effects
- Systematic monitoring
- Data concerning vulnerable data subjects
- Matching or combining datasets
- Innovative use of new technologies
- Preventing data subjects from exercising rights

**Five Parts of a PIA:**
1. Description of the intended data processing
2. Assessment of risks to privacy, rights and freedoms
3. Measures to address those risks
4. Safeguards, security measures and mechanisms
5. Justification for processing given the risks""",
                [
                    "Understand what constitutes 'high-risk' data processing",
                    "Learn the types of processing activities that trigger PIA requirements",
                    "Understand how to assess risk using severity and likelihood",
                    "Learn the five parts of a Privacy Impact Assessment",
                    "Understand when to conduct a PIA even if not required",
                    "Learn about pitstop review requirements with DPO"
                ]
            ),
            self._create_step(
                project_id, 2, 5,
                "Data & Privacy - Anonymization and Privacy Enhancing Technologies (PETs)",
                """**Data Anonymization and PETs**

**Anonymization:**
The simplest form is to remove Personally Identifiable Information (PII) from the dataset. However, the risk of re-identification remains where the remaining data could be matched to another dataset containing PII.

**Privacy-Enhancing Technologies (PETs)** enable insights from personal data while protecting privacy:

**PETs That Disguise The Data:**
- **Synthetic Data** - New data with same trends/statistical properties but different from original
- **Differential Privacy** - Manipulates data so it no longer reflects identifiable individuals
- **Homomorphic Encryption** - Encrypts data while preserving statistical properties

**PETs That Enable Insights Without Sharing All Data:**
- **Secure Multi-Party Computation** - Share parts of data to enable conclusions about all data
- **Private Set Intersection** - Identify common people in two datasets without sharing the datasets
- **Federated Learning** - Build AI model on distributed data without centralizing it

The expectation is that service developers will implement PETs where practicable.""",
                [
                    "Understand the difference between PII removal and full anonymization",
                    "Learn about re-identification risks",
                    "Understand Synthetic Data and its use cases",
                    "Learn about Differential Privacy techniques",
                    "Understand Homomorphic Encryption",
                    "Learn about Secure Multi-Party Computation",
                    "Understand Federated Learning",
                    "Learn how to justify PET selection decisions",
                    "Complete Chapter 2 quiz"
                ]
            ),
        ]

    def _create_chapter_3_security(self, project_id: str) -> List[ComplianceStep]:
        """Chapter 3: Security"""

        return [
            self._create_step(
                project_id, 3, 6,
                "Security - Introduction to AI Security Threats",
                """**AI-Specific Security Considerations**

This section describes the security tasks identified in the SDAIA AI Principles and the EU AI Act. These requirements are additional to any CISO security compliance processes.

AI systems face unique security threats beyond traditional software vulnerabilities. The machine learning components introduce new attack surfaces that adversaries can exploit to:
- Manipulate model behavior
- Steal intellectual property
- Compromise data privacy

**Key Security Considerations:**
- Securing training data from leaks and poisoning
- Protecting models from theft during development and deployment
- Defending against adversarial attacks during inference
- Implementing proper access controls and monitoring

**Governance:**
The RACI must include appropriate AI security roles with sign-offs from both CISO and the DPO.""",
                [
                    "Understand why AI systems need security beyond traditional software security",
                    "Learn about new attack surfaces in machine learning systems",
                    "Identify key security considerations for AI systems",
                    "Understand the importance of CISO and DPO sign-offs",
                    "Learn how to establish security governance for AI projects"
                ]
            ),
            self._create_step(
                project_id, 3, 7,
                "Security - Training Data and Model Threats",
                """**Training Data Leak**
Adversaries can use leaked training data to identify vulnerabilities in AI models, discover weaknesses or biases that can be exploited.

**Countermeasures:** Implement robust security standards per CISO guidance.

**Development-Time Model Theft**
Attackers steal the AI model during its development phase.

**Countermeasures:** Implement robust security standards per CISO guidance.

**Supply Chain Model Poisoning**
If the AI model relies on third-party components or libraries, attackers may compromise security through the supply chain by injecting malicious code.

**Countermeasures:** Robust vendor vetting and strict access controls to ensure model integrity.

**Training Data Poisoning**
Attackers manipulate training data to:
- Inject biased or misleading data to bias predictions
- Insert backdoor triggers that activate under specific conditions
- Induce data drift leading to degraded performance over time

**Countermeasures:** Robust data validation and preprocessing, careful vetting of data sources, adversarial training strategies, ongoing monitoring and auditing.""",
                [
                    "Understand training data leak risks",
                    "Learn about development-time model theft",
                    "Understand supply chain model poisoning attacks",
                    "Learn about training data poisoning techniques",
                    "Understand backdoor attacks",
                    "Learn about data drift from poisoned training data",
                    "Understand countermeasures for each threat type"
                ]
            ),
            self._create_step(
                project_id, 3, 8,
                "Security - Adversarial Attacks and Inference Threats",
                """**Evasion or Adversarial Examples**
Attackers craft inputs that are intentionally designed to be misclassified by the AI model. These adversarial examples contain imperceptible perturbations that deceive the model.

**Risks:**
- Bypass security mechanisms (facial recognition, malware detection)
- Transferability - adversarial examples for one model often work on other similar models

**Countermeasures:**
- Adversarial training (augmenting training data with adversarial examples)
- Prompt/Input validation mechanisms
- Enhanced interpretability of model outputs
- Ongoing monitoring and testing

**Model Inversion**
Attackers attempt to infer sensitive information about training data by analyzing the model's outputs through querying and observing responses.

**Countermeasures:**
- Training data perturbation (noise injection)
- Output noise (differential privacy techniques)
- Adversarial training
- Secure deployment environments

**Membership Inference**
Attackers determine whether a specific data point was part of the training dataset, potentially revealing sensitive information.

**Countermeasures:**
- Output noise (differential privacy)
- Data augmentation
- Regularization techniques
- Query access limitations""",
                [
                    "Understand adversarial examples and evasion attacks",
                    "Learn about transferability of adversarial examples",
                    "Understand model inversion attacks",
                    "Learn about membership inference risks",
                    "Understand adversarial training as a defense",
                    "Learn about differential privacy techniques",
                    "Understand input validation mechanisms",
                    "Complete Chapter 3 quiz"
                ]
            ),
        ]

    def _create_chapter_4_risk_fairness(self, project_id: str) -> List[ComplianceStep]:
        """Chapter 4: Risk & Fairness"""

        return [
            self._create_step(
                project_id, 4, 9,
                "Risk & Fairness - Establishing Context and Identifying Issues",
                """**Two Interwoven Threads: Risk and Fairness**

**Risk Thread:** Think about who will use the AI, for what purpose, and who will be impacted. This includes foreseeable but unintended scenarios where the AI system is misused or given erroneous inputs.

**Fairness Thread:** Focus on biases that may be present in input data which would lead to discriminatory operation. These must be tested for, identified, and mitigated using Fairness Metrics.

**Establishing the Context - Key Questions:**
- What is the purpose of your AI system?
- What are the use cases?
- Who will operate the system?
- Who will the system impact?
- Will it affect children or other vulnerable groups?
- In what languages and geographies will it be deployed?

**Risk & Fairness Issues to Identify:**

**1. Human Rights and Cultural Values Impact:**
- Civil and Political Rights (liberty, free expression, privacy, freedom from discrimination)
- Economic, Social, and Cultural Rights (fair wages, education, healthcare)
- Collective Rights (minorities, genders, indigenous peoples)

**2. Social & Environmental Impact:**
- Broader societal impacts (e.g., targeted advertising affecting elections)
- Environmental damage from AI energy consumption

**3. Foreseeable Errors and Misuse:**
- Input errors (defaults to "0000" or "9999", wrong units)
- Unethical but profitable uses""",
                [
                    "Document the purpose and use cases of the AI system",
                    "Identify who will operate and be impacted by the system",
                    "Assess impact on children and vulnerable groups",
                    "Analyze impact on Human Rights and Cultural Values",
                    "Evaluate social and environmental impact",
                    "Identify foreseeable errors and misuse scenarios",
                    "Document high-level framework for managing risk and fairness"
                ]
            ),
            self._create_step(
                project_id, 4, 10,
                "Risk & Fairness - Biased Feedback Loops and Mitigation",
                """**Biased Feedback Loops**

AI systems using reinforcement learning or adapting based on post-market inputs may develop biases if exposed to non-representative data.

**How Biased Feedback Loops Develop:**
1. **Biased Input Data** - Training data contains historical prejudices or unequal representation
2. **AI Decision Making** - System makes decisions based on biased data (e.g., hiring AI prefers certain demographics)
3. **Feedback Loop** - Decisions affect real world and generate new data
4. **Reinforcement of Bias** - New data reflects biased decisions, further training reinforces bias
5. **Escalation** - Bias becomes more pronounced over time

**Example:** Consumer credit risk models in the US discriminated against people in predominantly black neighborhoods using "postcode" as a risk proxy.

**Mitigating Risk & Fairness Issues - Four Categories:**

**1. Design Measures:**
- Code the model to produce error messages for out-of-range inputs
- Carefully implement bias corrections (avoid Google image AI mistakes)

**2. Process Measures:**
- Regular testing for emerging biases
- Corrective steps when biases are detected

**3. Operator Training Measures:**
- Train operators about fairness risks
- Explain pathways leading to risks
- Define circumstances where AI should not be used

**4. Human Oversight Measures:**
- In-the-loop: Human involvement in decision-making
- Out-of-the-loop: Humans review decisions after they're made
- Provide tools to interpret, spot anomalies, and override decisions
- Guard against "automation bias" (unreasonable trust in machines)""",
                [
                    "Understand how biased feedback loops develop",
                    "Learn the five-step process of bias escalation",
                    "Identify design measures to mitigate risks",
                    "Understand process measures for ongoing bias detection",
                    "Learn operator training requirements",
                    "Understand human oversight requirements (in-the-loop vs out-of-the-loop)",
                    "Learn about automation bias and how to prevent it"
                ]
            ),
            self._create_step(
                project_id, 4, 11,
                "Risk & Fairness - Types of Bias",
                """**Understanding Different Types of Bias**

Data is like a map - biases are the degree to which the map doesn't accurately represent the landscape.

**1. Measurement Bias:**
Occurs when measurement methods skew data (faulty equipment, data entry errors, inconsistent subjective measures).

**2. Sampling Bias:**
Data used to train the model is not representative of the intended population.
- *Non-response Bias:* People who respond differ from those who don't (e.g., QR code surveys favor tech-savvy)
- *Under-coverage Bias:* Some population members inadequately represented (e.g., facial recognition trained mostly on one ethnicity)
- *Availability Bias:* Available data isn't representative (e.g., more medical info on sick people than healthy)

**3. Survivorship Bias:**
Analysis only considers 'survivors' or successes, ignoring failures (e.g., illness surveys underrepresent fatal illnesses).

**4. Recency Bias:**
Recent data gets disproportionate weight over older data, missing long-term patterns (e.g., short-term weather data missing global warming trend).

**5. Data Processing Bias:**
Introduced during data cleaning and preparation.
- *Outlier bias:* Averaging masks diversity when variance within bins is large
- *Algorithmic Bias:* Algorithm inherently favors certain outcomes

**6. Cultural Bias:**
Model doesn't adequately account for cultural differences.

**7. Exclusion Bias:**
Certain data systematically excluded (often due to preconceived notions).

**8. Confirmation Bias:**
Data interpreted to support pre-existing beliefs (affects feature selection).""",
                [
                    "Identify measurement bias in your data",
                    "Understand the three types of sampling bias",
                    "Recognize survivorship bias",
                    "Learn about recency bias and its effects",
                    "Understand data processing biases",
                    "Identify cultural bias in AI systems",
                    "Learn about exclusion and confirmation bias"
                ]
            ),
            self._create_step(
                project_id, 4, 12,
                "Risk & Fairness - Fairness Metrics and Thresholds",
                """**Fairness Metrics**

Fairness metrics quantify and monitor the fairness of ML models to ensure they don't discriminate.

**Group Fairness Metrics:**

**1. Disparate Impact (DI):**
Ratio of positive outcomes for protected group to non-protected group.

**2. Demographic Parity (DP):**
Predictions statistically independent of sensitive attributes; equal representation across groups.

**3. Conditional Demographic Disparity (CDD):**
Disparity in prediction performance between groups after adjusting for other factors.

**4. Equal Opportunity (EO):**
True positive rate (TPR) similar across different groups.

**5. Equalized Odds (EOdds):**
Both false positive rate (FPR) and TPR balanced across groups.

**6. Treatment Equality (TE):**
Groups with similar risk profiles receive similar treatment/outcomes.

**Individual Fairness Metrics:**

**7. Individual Fairness:**
Similar individuals receive similar predictions regardless of protected attributes.

**8. Theil Index:**
Measures inequality in benefit allocation; 0 = perfect fairness; lower scores better.

**9. Consistency:**
Measures similarity of predictions for similar instances using k-nearest neighbors; 1 = ideal.

**Setting Fairness Thresholds:**
- Often set in sector-specific regulations
- 80% rule commonly employed
- Must consider implications in your specific use case
- Document logic and conclusions
- Thresholds can be unidirectional or bidirectional""",
                [
                    "Understand the difference between group and individual fairness metrics",
                    "Learn when to use each fairness metric",
                    "Understand how to calculate Disparate Impact",
                    "Learn about Equal Opportunity vs Equalized Odds",
                    "Understand the Theil Index",
                    "Learn how to set appropriate fairness thresholds",
                    "Understand the 80% rule",
                    "Document fairness metric selection and justification",
                    "Complete Chapter 4 quiz"
                ]
            ),
        ]

    def _create_chapter_5_explainability(self, project_id: str) -> List[ComplianceStep]:
        """Chapter 5: Explainability"""

        return [
            self._create_step(
                project_id, 5, 13,
                "Explainability - Foundations and Techniques",
                """**Why AI Model Explainability Matters**

AI model explainability focuses on making AI system decisions understandable to humans. This is important because it:
- Fosters trust and understanding among users
- Enables identification and correction of biases
- Ensures decisions align with ethical standards and regulatory requirements
- Facilitates model improvements
- Allows stakeholders to confidently rely on judgments in high-stakes domains

**Explainability Foundations:**

**Data Provenance and Quality:**
Document and explain the provenance, quality, labeling, and interpretation of data the model was built on, including the governance structure.

**Main Approaches to AI Model Explainability:**

**1. Transparent Models (Inherently Interpretable):**
Linear regression, decision trees, simple rule-based systems - naturally interpretable.

**2. Post-Hoc Interpretability:**
- *Local Explanations:* LIME (Local Interpretable Model-agnostic Explanations), SHAP (SHapley Additive exPlanations) - explain individual predictions
- *Global Explanations:* Feature importance, decision boundary visualization - understand overall behavior

**3. Model Simplification:**
Simplify complex model into interpretable one while retaining performance.

**4. Visualization Techniques:**
Saliency maps, activation maps, layer-wise relevance propagation - visualize what the model focuses on.

**5. Example-Based Methods:**
Counterfactual explanations, prototype analysis - use specific instances to explain behavior.

**6. Feature Relevance Estimation:**
Understand importance of different input features.

**7. Rule Extraction:**
Extract rules or decision paths from complex models.

**8. Interactive Tools:**
Allow users to query and explore the model interactively.""",
                [
                    "Understand why explainability is essential for AI systems",
                    "Learn about transparent vs black-box models",
                    "Understand LIME and SHAP for local explanations",
                    "Learn about global explanation techniques",
                    "Understand visualization techniques for deep learning",
                    "Learn about counterfactual explanations",
                    "Understand when to use each explainability approach",
                    "Learn about logging requirements for auditability"
                ]
            ),
            self._create_step(
                project_id, 5, 14,
                "Explainability - Communicating with End Users",
                """**User Communication Requirements**

Content to inform users about AI decision-making must include two elements:

**1. How the AI System Operates:**
The internal logic and processes that enable it to reach a decision, expressed at a level comprehensible to the user.

**2. Why the AI Made a Specific Decision:**
Explanation focused on why the AI came to the decision about them or a specific context.

**Communication Channels:**
- Training manuals
- Boiler plate text shown to users
- Dedicated section of the AI platform
- Pop-up screens within the user journey

**Additional User Information Requirements:**

Users must also be informed about:
- Whether they're viewing AI-generated content that may be a deep fake
- Whether the AI uses emotional recognition
- Whether the AI performs biometric categorization
- What residual risks are associated with the AI system
- How to access the complaints process
- How to obtain explanations of AI decisions

**Validation:**
Communication channels designed to explain the AI system's work must be validated with users BEFORE placing the AI system on the market to ensure effectiveness.

**Post-Market Requirements:**
- Periodically revalidate user interfaces
- Ensure explainability remains effective as user base changes
- Define and implement processes to report breaches and emerging risks to stakeholders""",
                [
                    "Design explanations of how the AI system operates",
                    "Create process for users to obtain decision explanations",
                    "Implement user notification about deep fake content",
                    "Inform users about emotional recognition usage",
                    "Communicate biometric categorization usage",
                    "Explain residual risks to users",
                    "Design and communicate complaints process",
                    "Validate user interfaces with actual users",
                    "Establish post-market revalidation schedule",
                    "Complete Chapter 5 quiz"
                ]
            ),
        ]

    def _create_chapter_6_tech_development_record(self, project_id: str) -> List[ComplianceStep]:
        """Chapter 6: Technology Development Record"""

        return [
            self._create_step(
                project_id, 6, 15,
                "Technology Development Record - Planning and Design Phase",
                """**The Technology Development Record**

Mandated in the EU AI Act, this is a centralized record of the AI system's technology development. Different parts are built up in different phases, with emphasis on the Build and Validate phase.

**Planning and Design Phase Requirements:**

**1. Design Description:**
Describe your proposed design for the AI system. Reference design documents and attach all supporting documents (must be a single document, no external links).

**2. Define Success Criteria:**
Clearly define required levels of:
- Accuracy
- Reliability
- Security

**3. Justify Design:**
Explain why your design will achieve the objectives.

**4. Define Validation Methodology:**
Document methodology to validate whether your model achieved desired levels of accuracy, reliability, and security.

**Note:** Define this NOW before building the model to ensure clear objectives and resist reverse-engineering easier goals once model capabilities are known.

**5. Design Logging and Record Keeping:**
Define processes for:
- When event logs are generated
- How and how long input data is stored
- How logs show hardware/software versions used
- What model parameters were used
- How records and logs can be searched
- Privacy protections for records

**6. Obtain Sign-Offs:**
Get sign-offs from roles named in RACI (including DPO) for all design work.""",
                [
                    "Create comprehensive design description with supporting documents",
                    "Define accuracy requirements and justify them",
                    "Define reliability requirements and justify them",
                    "Define security requirements and justify them",
                    "Document validation methodology before building model",
                    "Design event logging system",
                    "Design input data storage and retention policies",
                    "Design version tracking for hardware/software",
                    "Design model parameter recording",
                    "Design record search and privacy protection mechanisms",
                    "Obtain all required sign-offs from RACI roles"
                ]
            ),
            self._create_step(
                project_id, 6, 16,
                "Technology Development Record - Data Preparation and Build Phases",
                """**Data Preparation Phase:**

**1. Define Input Data Range:**
Define the range of input data you expect your AI model to encounter, including foreseeable outliers.

**2. Ensure Dataset Coverage:**
Ensure training and validation datasets adequately cover the expected range of input data and outliers.

**3. Create Data Cards:**
Record data cards for each dataset and archive them.

**4. Design Data Backup Procedures:**
- Design backup procedures
- Record when backups occur
- Create governance process to ensure backups happen

**5. Obtain Sign-Offs:**
Get sign-offs from RACI roles (including DPO).

**Build and Validate Phase:**

**Central Activity - Model Creation:**
Record each step in sufficient detail that an expert could recreate them:
- What datasets were used?
- How were they partitioned?
- What hardware and software was used?
- How were hyper-parameters set in each iteration?

**Validation Documentation:**
Record enough detail that an expert can recreate validation steps, including:
- Testing model robustness to outlier input data
- Demonstrating accuracy, reliability, and security
- For high-risk AI: demonstrating robustness to input errors

**System Integration Testing:**
Once integrated into the final AI system, test and document:
- Does the model function as intended in context?
- Do usage guardrails work?
- Are user communication channels operating and effective?

**Decision Documentation:**
Record and store data underpinning key decisions (training datasets, prompts, outcomes) with proper indexing for retrieval.

**Known Limitations:**
Record known limitations of the AI system.

**Use Case Restrictions:**
Document any restricted or unsupported use cases.""",
                [
                    "Define and document expected input data range",
                    "Identify foreseeable outlier data",
                    "Create data cards for all datasets",
                    "Design and implement backup procedures",
                    "Document model building steps in reproducible detail",
                    "Document validation methodology and results",
                    "Test and document system integration",
                    "Record key decision data with proper indexing",
                    "Document known limitations",
                    "Document restricted and unsupported use cases",
                    "Obtain all required sign-offs",
                    "Complete Chapter 6 quiz"
                ]
            ),
        ]

    def _create_chapter_7_post_market_monitoring(self, project_id: str) -> List[ComplianceStep]:
        """Chapter 7: Post Market Monitoring"""

        return [
            self._create_step(
                project_id, 7, 17,
                "Post Market Monitoring - Governance and Continuous Monitoring",
                """**Why Post-Market Monitoring Is Essential**

Even if an AI system functions perfectly at launch, over time this may change because:
- The nature of the user base changes
- Feedback loops emerge causing model drift
- Changes are made to how the AI system is implemented
- Security breaches occur

**Post-Market Monitoring System Components:**
1. Continuous monitoring
2. Periodic assessments

**Post-Market Monitoring Governance:**

**Develop a Post-Market Monitoring Plan:**
- What metrics will be continuously monitored?
- What triggers will provoke investigations?
- Frequency of periodic AI Impact Assessments
- Frequency of Security assessments
- RACI for post-market monitoring
- Sign-off from appropriate stakeholders

**Continuous Monitoring - Three Key Themes:**

**1. Resource Usage (Environmental Impact):**
Example calculation:
- Identify power consumption of hardware
- Calculate % attributable to your AI if shared
- Monthly energy consumption
- Type of power generation
- CO2 per MWh from that energy source
- Total tonnes of CO2 per month

**2. Fairness Metrics:**
- Define monitoring frequency
- Compare values with predefined thresholds
- Sign-off by authority defined in RACI
- Document metric values and analysis

**3. Security Metrics:**
- Develop with CISO
- Create metrics to detect AI-specific attacks
- Nature depends on type of AI system""",
                [
                    "Understand why AI systems require ongoing monitoring",
                    "Develop comprehensive post-market monitoring plan",
                    "Define continuous monitoring metrics",
                    "Set up investigation triggers",
                    "Establish monitoring frequency",
                    "Design resource usage monitoring",
                    "Implement fairness metrics monitoring",
                    "Implement security metrics monitoring with CISO",
                    "Establish governance and RACI for monitoring",
                    "Obtain stakeholder sign-offs"
                ]
            ),
            self._create_step(
                project_id, 7, 18,
                "Post Market Monitoring - Assessments and Technology Development Record Updates",
                """**AI Impact Assessments**

**Full AI Impact Assessment:**
- Conduct before launch
- Questions depend on AI risk level (toggle in Compliance Tool)
- Must be reviewed and approved by DPO before launch or market placement

**Periodic Assessment:**
- Simplified version of full assessment
- Focused on issues arising during operational lifespan
- Includes continued alignment with human rights and cultural values
- Stipulate frequency in post-market monitoring plan
- Define triggers for additional assessments
- Must be reviewed by DPO and other RACI authorities

**AI Security Assessments:**
- Full assessment before launch
- Periodic assessments during operational life
- Defined and signed off by CISO

**User Interface Monitoring:**

Post-market monitoring must periodically assess effectiveness of user interfaces:
- Effectiveness at communicating required information
- User understanding of residual risks
- Accessibility of decision explanations
- Accessibility of complaints procedure
- Define metrics characterizing UI effectiveness
- Set acceptable thresholds
- Define assessment frequency

**Technology Development Record - Post-Market Updates:**

The TDR is an active document requiring ongoing updates:

**Descriptive Information (keep current):**
- Who is responsible for the AI system
- Purpose of the AI system
- Date and version
- Intended lifespan
- Hardware (intended and actual)
- Forms the AI has been placed on market
- External systems it interacts with
- Diagrams of how AI fits into broader product
- Record of all changes made through lifecycle
- List of standards followed

**Documentation (keep current):**
- Instructions for users
- Integration guide for deployers
- EU Conformity Certification applications""",
                [
                    "Understand difference between full and periodic AI Impact Assessments",
                    "Conduct full AI Impact Assessment before launch",
                    "Establish schedule for periodic assessments",
                    "Define triggers for additional assessments",
                    "Coordinate with CISO on security assessments",
                    "Design UI effectiveness metrics",
                    "Establish UI assessment schedule",
                    "Keep Technology Development Record current",
                    "Update user instructions as system evolves",
                    "Maintain integration guide for deployers",
                    "Document all system changes throughout lifecycle",
                    "Complete Chapter 7 and Final Exam"
                ]
            ),
        ]
