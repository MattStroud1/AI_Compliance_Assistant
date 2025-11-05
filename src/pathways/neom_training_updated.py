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
                """**Learning Objectives:**
- Understand what 'privacy by design' means and why it matters
- Learn the three critical data governance roles and their responsibilities
- Master how to establish and maintain a RACI matrix
- Understand why specificity in RACI assignments prevents costly gaps
- Learn Data Governance Framework requirements
- Understand version control for RACI matrices

---

**Why Data Governance is Your AI Project's Foundation**

Picture this: You've built a brilliant AI system that predicts customer preferences with uncanny accuracy. But six months after launch, you discover it's been using personal data without proper consent. The regulators come knocking, your reputation takes a hit, and suddenly you're facing fines that could sink the project. This nightmare scenario is entirely preventable with proper data governance from day one.

Data governance isn't just bureaucracy—it's the scaffolding that allows your AI system to stand tall and withstand scrutiny. At its heart is a principle called "privacy by design," which means building privacy protections into your AI system from the ground up, rather than bolting them on as an afterthought when problems emerge.

**The RACI Matrix: Your Project's North Star**

Think of a RACI matrix as your project's organizational chart on steroids. RACI stands for Responsible (who does the work), Accountable (who owns the outcome), Consulted (who provides input), and Informed (who needs to know). Without clear RACI definitions, you'll find team members stepping on each other's toes, critical decisions falling through cracks, and when something goes wrong, everyone pointing fingers.

Here's what makes a good RACI matrix: specificity. Don't just write "Data Team" as responsible—name actual people with their email addresses. Don't say someone is "accountable for data quality"—specify they're accountable for ensuring training data accuracy meets the 95% threshold before model training begins. This level of detail transforms your RACI from a vague organizational chart into an operational playbook.

Critically, your RACI must include three specialized data governance roles:

**The Data Owner** is your data's executive sponsor. They have authority over data assets and make strategic decisions about access and usage. Think of them as the data's guardian—they're ultimately responsible if something goes wrong with how data is collected, used, or shared. In practice, this is often a senior business leader who understands both the value and risks of the data.

**The Data Steward** is your hands-on data manager. They handle day-to-day operations, implementing policies and ensuring data is properly documented. If the Data Owner is the architect, the Data Steward is the general contractor making sure everything is built to spec. They're the ones who catch quality issues early, maintain metadata, and ensure teams follow established procedures.

**The Data Custodian** is your technical guardian. They're responsible for the physical storage, security, and access controls. They implement encryption, manage backups, set up access permissions, and ensure data residency requirements are met. If there's a data breach or loss, the Data Custodian is first in the hot seat.

**Making It Operational**

The best RACI matrices are living documents, not dusty PDFs filed away and forgotten. Version control is essential—when roles change or new tasks emerge, create a new version, archive the old one, and get signatures on the update. This creates an audit trail showing you had proper governance at each stage.

Start your project with a RACI kick-off meeting. Walk through each row of the matrix with the entire team. Make sure everyone understands not just their own role, but how they interact with others. Where are the handoff points? What are the escalation paths? Who has authority to override whom? These conversations surface misunderstandings before they become conflicts.

Your Data Governance Framework should document all of this: roles, responsibilities, decision rights, escalation procedures, and data handling standards. It's tempting to over-engineer this, creating hundreds of pages nobody reads. Resist that urge. A concise, clear framework that people actually reference beats a comprehensive tome that gathers dust.

**The Hidden Benefits**

When data governance is done right, you'll notice something remarkable: projects move faster, not slower. Decisions get made quickly because everyone knows who has authority. Mistakes get caught early because responsibilities are clear. Compliance becomes straightforward because you can show auditors exactly who did what and when.

Moreover, good governance builds trust. When data subjects know there's a named, accountable person responsible for protecting their information, they're more comfortable sharing it. When business leaders know there are proper controls, they're more willing to greenlight innovative uses of data.

The RACI matrix and governance framework you establish now will serve as the blueprint for every AI project that follows. Invest the time to get it right, and you'll reap the benefits for years to come.""",
                []  # Learning objectives moved to content
            ),
            self._create_step(
                project_id, 2, 3,
                "Data & Privacy - Sensitive Data and Legal Basis",
                """**Learning Objectives:**
- Identify what constitutes sensitive data under PDPL and GDPR
- Understand children's data age thresholds (13 for PDPL, 16 for GDPR)
- Learn the three common legal bases for processing personal data
- Master the Legitimate Interest Assessment (LIA) three-question test
- Understand why sensitive data requires special legal basis considerations
- Learn how to design features to support your chosen legal basis

---

**The Sensitive Data Minefield: Why Some Data Demands Extra Care**

Not all data is created equal. While your name and email address are personal data requiring protection, they don't carry the same risks as your medical records or political affiliations. This is why regulations draw a sharp line between regular personal data and what they call "sensitive" or "special category" data.

Sensitive data is information that, if mishandled, could lead to discrimination, persecution, or significant harm to individuals. Think about it: if an AI system learns you enjoy Italian food, the worst that happens is targeted pasta ads. But if it reveals your HIV status, religious beliefs, or sexual orientation to the wrong parties? That could destroy lives.

Both the Saudi Personal Data Protection Law (PDPL) and the European GDPR treat sensitive data with heightened scrutiny. The PDPL list includes ethnic or tribal origin, religious and political beliefs, civil association memberships, security and criminal data, biometric identifiers, genetic and health information, location and financial data, and information about parentage. The GDPR adds trade union membership and data about sexual orientation or sex life.

**The Children's Data Special Case**

Children's data gets similar special treatment, but the age threshold varies. Under PDPL, children are those under 13 years old. GDPR sets the bar higher at 16 (though member states can lower it to 13). Why the difference? It reflects different cultural views on when young people can meaningfully consent to data processing.

Here's the practical implication: if your AI system might interact with children, you need robust age verification and parental consent mechanisms. You can't just ask "Are you over 13?" and take their word for it. You need actual verification—which is why many social platforms simply ban users under 13 rather than deal with the compliance headache.

**Choosing Your Legal Basis: The Foundation of Lawful Processing**

Before you collect a single byte of personal data, you must answer a fundamental question: "On what legal grounds are we processing this data?" In privacy law, this is called your "legal basis," and choosing wrong can invalidate your entire data processing operation.

For private sector AI projects, three legal bases dominate: Legitimate Interest, Contract, and Consent. Each comes with different requirements and constraints.

**Legitimate Interest** is popular because it's flexible—you can process data for purposes that benefit your business, as long as those benefits aren't outweighed by privacy risks to individuals. But there's a catch: you must conduct a Legitimate Interest Assessment (LIA) answering three questions:

1. Is there a legitimate interest behind the processing? (Your business need must be real and specific)
2. Is the processing necessary for that purpose? (Could you achieve your goal another way?)
3. Do individuals' rights override your interest? (Would they reasonably expect this use? Could it harm them?)

Only if you answer yes to the first two and no to the third can you proceed. And here's the critical constraint: **you absolutely cannot use Legitimate Interest as the legal basis for processing sensitive data**. The law considers sensitive data too risky for this flexible approach.

**Contract** as a legal basis means the data processing is necessary to fulfill a contractual obligation with the data subject. For instance, if someone buys your AI-powered service, you can process their payment information because it's necessary to deliver what they purchased. The key word is "necessary"—you can't claim contract as your basis for optional marketing activities.

**Consent** seems straightforward but is actually the most demanding legal basis. It must be freely given, specific, informed, and unambiguous. You can't bury consent in pages of terms and conditions. You can't make consent a condition for service when it's not necessary for that service. Pre-ticked boxes don't count. The user must take clear affirmative action.

**Designing for Your Legal Basis**

Your choice of legal basis isn't just a legal checkbox—it shapes your entire AI system design. If you're relying on consent, you need interfaces that clearly explain what data you're collecting and why, with prominent opt-in mechanisms. You need systems to track who consented to what and when. You need easy ways for users to withdraw consent, and automated processes to delete their data when they do.

If you're using a contract basis, your agreements need specific clauses explaining the data processing. If you're claiming legitimate interest, you need documentation of your LIA, updated whenever your processing changes.

Many teams make the mistake of picking their legal basis as an afterthought, then trying to retrofit their system to match. Do it the other way around: choose your legal basis early, document your reasoning, and build your data flows to support it from day one. This approach not only ensures compliance but also builds user trust, as your data practices will feel coherent and transparent rather than cobbled together.""",
                []  # Learning objectives moved to content
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
                """**Learning Objectives:**
- Understand why AI systems need security beyond traditional software security
- Learn about new attack surfaces in machine learning systems
- Identify key security considerations for AI systems
- Understand the importance of CISO and DPO sign-offs
- Learn how to establish security governance for AI projects

---

**AI Security: A New Frontier in Cybersecurity**

Imagine you're securing a traditional web application. You implement firewalls, encryption, access controls, and regular security audits. Your CISO signs off, confident the system is protected. But what if that application contains an AI model that makes critical decisions? Suddenly, your traditional security arsenal isn't enough.

**The AI Security Paradox**

Here's the challenge: AI systems are simultaneously more powerful and more vulnerable than traditional software. A conventional application follows explicit programming logic—if you secure the code and the infrastructure, you've largely secured the system. But an AI model is different. It's learned its behavior from data, making it susceptible to entirely new classes of attacks that target its learning process, its training data, and even its decision-making patterns.

Consider this real-world scenario: A healthcare organization deploys an AI diagnostic tool that's passed all traditional security audits. The servers are secure, the network is encrypted, access is controlled. Yet an adversary discovers they can manipulate the model's diagnoses by subtly altering medical images in ways invisible to the human eye. Traditional security measures never anticipated this attack vector.

**Understanding AI-Specific Attack Surfaces**

AI systems introduce three fundamental attack surfaces that don't exist in traditional software:

**1. The Training Data Attack Surface**

Your AI model is only as trustworthy as the data it learned from. Unlike conventional software where the code is explicitly written and reviewed, AI models absorb patterns from potentially millions of data points. If an adversary can poison this training data—even a small percentage of it—they can influence the model's behavior in dangerous ways.

Think of it like teaching a child. If someone occasionally whispers false information during their education, those misconceptions become embedded in their worldview. Similarly, poisoned training data creates biases and backdoors that persist throughout the model's lifetime.

**2. The Model Itself as Intellectual Property**

AI models represent enormous investments—months or years of data collection, computational resources, and expert tuning. Unlike traditional software, where reverse-engineering requires considerable effort, AI models can sometimes be stolen simply by querying them repeatedly and observing their outputs. This "model extraction" attack can allow competitors or adversaries to replicate your AI system without the original investment.

In 2020, researchers demonstrated they could extract a commercial image classification model with 98% accuracy using only API queries. The model represented millions in investment, yet it was vulnerable to theft through its normal operation.

**3. The Inference-Time Attack Surface**

Even after deployment, AI models face unique threats during their operation. Adversarial examples—inputs deliberately crafted to fool the model—can cause catastrophic failures. A stop sign with carefully placed stickers might be classified as a "speed limit 45" sign by an autonomous vehicle's vision system. To humans, the stop sign looks normal. To the AI, it's something entirely different.

These attacks exploit how neural networks process information—through high-dimensional mathematical transformations that don't align with human perception. What seems like imperceptible noise to us can completely alter an AI's decision.

**Why Traditional Security Isn't Enough**

Your CISO's standard playbook addresses network security, access control, and data protection—all crucial elements. But it likely doesn't cover:

- **Data provenance and integrity verification** throughout the ML pipeline
- **Model versioning and governance** to track changes and prevent unauthorized modifications
- **Adversarial robustness testing** to ensure the model resists manipulation attempts
- **Privacy-preserving techniques** like differential privacy to prevent information leakage
- **Supply chain security** for third-party models, datasets, and ML frameworks

This is why SDAIA AI Principles and the EU AI Act mandate additional security requirements specifically for AI systems. They recognize that machine learning introduces fundamental new risks that traditional cybersecurity doesn't address.

**Establishing AI Security Governance**

Effective AI security requires collaboration between multiple stakeholders:

**The CISO** brings expertise in traditional security controls, threat modeling, and security operations. They ensure the infrastructure, networks, and systems supporting the AI are hardened against conventional attacks.

**The DPO (Data Protection Officer)** ensures that security measures protect personal data throughout the AI lifecycle. They're particularly concerned with training data privacy, model inversion risks, and ensuring security controls align with data protection regulations.

**The AI Development Team** understands the model architecture, training process, and inference pipeline. They implement technical defenses like adversarial training, input validation, and model monitoring.

**The Risk Management Office** assesses the business and operational risks posed by AI-specific security threats. They help prioritize security investments based on threat likelihood and impact.

Your RACI matrix must include appropriate AI security roles with clear sign-offs from both the CISO and DPO. This dual approval ensures both traditional and AI-specific security concerns are addressed. Neither can be skipped—you need both perspectives to secure modern AI systems effectively.

**Key Takeaways**

AI security isn't just an extension of traditional cybersecurity—it's a distinct discipline addressing unique attack vectors. Training data can be poisoned, models can be stolen or manipulated, and adversaries can craft inputs that fool AI systems in ways imperceptible to humans.

To build trustworthy AI, you must layer AI-specific security measures on top of your existing security program. This requires governance structures that bring together CISO expertise, DPO oversight, and AI technical knowledge. Only then can you address both traditional and AI-specific threats comprehensively.

In the following sections, we'll explore specific AI security threats in detail and learn practical countermeasures to defend against them. Understanding these risks is the first step toward building AI systems that are not just intelligent, but also secure and resilient.""",
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
                """**Learning Objectives:**
- Understand training data leak risks and their cascading consequences
- Learn about development-time model theft and intellectual property protection
- Understand supply chain model poisoning attacks through third-party components
- Learn about training data poisoning techniques and backdoor insertion
- Understand how poisoned data induces model drift and performance degradation
- Learn practical countermeasures for each threat type

---

**The Hidden Vulnerabilities: Attacks Before Deployment**

Most people think about AI security as something that happens after deployment—protecting a running system from external attacks. But some of the most dangerous threats to AI systems occur much earlier, during the development phase when training data is being collected and models are being built. Let's explore these critical pre-deployment threats.

**Training Data Leaks: The Foundation Cracks**

Imagine building a house on a foundation you believe is solid, only to discover years later that detailed blueprints of every structural weakness were posted online. That's essentially what happens with training data leaks.

Your training data reveals everything about how your AI model makes decisions. It shows patterns, edge cases, biases, and blind spots. When this data leaks—whether through misconfigured cloud storage, insider threats, or data breaches—adversaries gain a blueprint for attacking your model.

Consider a fraud detection model trained on historical transaction data. If this training data leaks, fraudsters can study exactly which patterns trigger alerts and which slip through undetected. They can reverse-engineer the model's decision boundaries without ever directly accessing the model itself. It's like giving a burglar the complete specifications of your alarm system before they attempt a break-in.

**Real-world Impact:**

In 2017, a major ride-sharing company experienced a data breach exposing 57 million user records. While the immediate privacy concerns made headlines, few considered the AI security implications: their driver background-check AI and surge-pricing algorithms were now vulnerable to adversaries who could study the training data patterns.

**Countermeasures:**

Protecting training data requires treating it as the crown jewel it truly is:

- **Data access controls:** Implement strict role-based access. Only team members who absolutely need training data should have access, and every access should be logged and monitored.
- **Encryption at rest and in transit:** Training data should never exist in unencrypted form outside of secure computing environments.
- **Data anonymization and synthetic data:** Where possible, use differentially private or synthetic datasets that preserve statistical properties without exposing real individuals' information.
- **Regular security audits:** Engage your CISO to conduct penetration tests specifically targeting training data repositories.

**Development-Time Model Theft: Stealing Months of Work in Minutes**

Training sophisticated AI models requires enormous resources—specialized hardware, massive datasets, and expert talent working for months or years. But once trained, a model is ultimately just a file containing numerical parameters. If an adversary steals this file, they've instantly obtained all that investment without any of the cost.

Model theft during development is particularly insidious because it often goes undetected. Unlike a deployed model where unusual query patterns might raise flags, development environments may have looser monitoring. A malicious insider, a compromised development machine, or vulnerable cloud storage can provide the opening an adversary needs.

**A Cautionary Tale:**

In 2020, researchers demonstrated they could steal machine learning models from major cloud providers by exploiting side-channel vulnerabilities in shared hardware. The stolen models represented millions in investment, yet the theft left no obvious trace.

**Countermeasures:**

- **Secure development environments:** Isolate model training in hardened environments with strict network segmentation
- **Model encryption:** Store model parameters encrypted, with decryption keys managed through hardware security modules (HSMs)
- **Version control and access logging:** Track every change to model files and monitor who accesses them
- **Code review for ML pipelines:** Just as you review application code, review ML training scripts for security vulnerabilities
- **Physical security:** For highly sensitive models, consider air-gapped training environments with no internet connectivity

**Supply Chain Model Poisoning: The Trojan Horse Attack**

Modern AI development relies heavily on pre-trained models, open-source frameworks, and third-party datasets. This creates a vast supply chain that adversaries can exploit. It's AI's equivalent of the classic Trojan Horse—the threat comes disguised as something helpful.

Imagine downloading a pre-trained language model from a popular repository to fine-tune for your specific application. Unbeknownst to you, an adversary has poisoned this model with backdoors that activate when specific trigger phrases appear in the input. Your fine-tuning preserves these backdoors, and you've now deployed a compromised system that appears to work perfectly—until the adversary activates their trigger.

**The Growing Threat:**

As the AI ecosystem matures, supply chain attacks are becoming more sophisticated. In 2021, researchers demonstrated a "BadNets" attack where poisoned pre-trained models maintained backdoors even after significant retraining. The backdoors were remarkably resilient—surviving the very process that organizations use to customize models for their needs.

**Countermeasures:**

- **Vendor vetting:** Thoroughly evaluate the provenance and security practices of third-party model and dataset providers
- **Model scanning:** Use automated tools to scan pre-trained models for anomalous behavior patterns
- **Trusted repositories only:** Restrict downloads to vetted, official sources with strong security practices
- **Model validation:** Test pre-trained models extensively before fine-tuning, looking for unexpected behaviors
- **Backdoor detection:** Implement specialized testing to detect potential backdoor triggers before deployment

**Training Data Poisoning: Corrupting the Learning Process**

Perhaps the most subtle and dangerous attack is training data poisoning—the strategic injection of malicious examples into your training dataset. Unlike other attacks that target existing models or data, poisoning attacks corrupt the learning process itself.

Data poisoning can take several forms:

**Bias Injection:** Adversaries inject examples that create systematic biases. A hiring AI trained on poisoned data might learn to discriminate against certain demographics. The model appears to work normally but makes consistently biased decisions that favor the adversary's goals.

**Backdoor Insertion:** Poisoned examples teach the model to behave normally under most conditions but respond incorrectly when a specific "trigger" appears. Imagine a spam filter that works perfectly but always allows through emails containing a secret keyword. The model passes all normal tests because the backdoor only activates on the specific trigger the adversary controls.

**Performance Degradation:** Sometimes the goal isn't a specific backdoor but simply degrading model quality over time. Gradually injecting examples that contradict the model's training induces "data drift," causing performance to slowly degrade without obvious cause.

**The Insidious Nature:**

What makes poisoning particularly dangerous is its scale. Research has shown that poisoning just 3% of training data can significantly alter model behavior. For models trained on millions of examples scraped from the internet, verifying the integrity of every single training example is impractical.

**Countermeasures:**

- **Data provenance tracking:** Maintain detailed records of where each training example originated
- **Statistical outlier detection:** Use automated systems to flag suspicious data points that don't match expected distributions
- **Data sanitization:** Implement preprocessing pipelines that filter potentially corrupted examples
- **Diverse data sources:** Don't rely on single data sources; diversity makes poisoning attacks harder to execute at scale
- **Adversarial training:** Include known attack examples in training to build resilience
- **Continuous monitoring:** Even after deployment, monitor for signs of poisoned data affecting model behavior—unexpected drift, performance anomalies, or behavioral inconsistencies

**Building Resilient AI Systems**

These pre-deployment threats share a common theme: they target the AI development process itself rather than the deployed system. This means traditional perimeter security isn't sufficient. You must secure the entire ML pipeline—from data collection through model training to artifact storage.

The good news is that awareness and proper security hygiene can dramatically reduce these risks. Work closely with your CISO to implement defense-in-depth strategies that protect data, models, and development environments. Treat training data and model artifacts with the same security rigor as production databases and application code. And remember: in AI security, prevention is far more effective than cure. A poisoned model or leaked training dataset can compromise your system in ways that may never be fully remediated.""",
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
                """**Learning Objectives:**
- Understand adversarial examples and evasion attacks at a technical level
- Learn about the transferability phenomenon that makes adversarial attacks scalable
- Understand model inversion attacks and how they extract training data information
- Learn about membership inference risks and privacy implications
- Understand adversarial training as a primary defense mechanism
- Learn about differential privacy techniques for protecting model outputs
- Understand input validation mechanisms and monitoring strategies

---

**When AI Eyes Deceive: Runtime Attacks on Deployed Models**

You've secured your training data, protected your models during development, and validated your supply chain. Your AI system passes all tests and gets deployed to production. The security job is done, right? Unfortunately, that's when an entirely new category of threats emerges—attacks against the running model itself.

**Adversarial Examples: Fooling AI in Plain Sight**

In 2018, researchers at MIT demonstrated something remarkable and terrifying: they created a 3D-printed turtle that AI image classifiers consistently identified as a "rifle." To human eyes, it was clearly a turtle. But from every angle, every lighting condition, state-of-the-art AI vision systems saw a weapon.

This is the essence of adversarial examples—inputs deliberately crafted to exploit how neural networks process information. These attacks reveal a fundamental disconnect between human and machine perception.

**How Adversarial Examples Work:**

Neural networks make decisions by processing inputs through layers of mathematical transformations. Each layer extracts increasingly abstract features—edges become shapes, shapes become objects. But this process operates in high-dimensional space where human intuition breaks down.

Adversaries can calculate exactly which tiny changes to an input will flip the model's decision. These perturbations might be imperceptible noise added to an image, subtle changes to audio waveforms, or carefully crafted typos in text. To humans, the input looks normal. To the AI, it's something completely different.

**Real-World Consequences:**

The implications go far beyond academic curiosity:

**Autonomous Vehicles:** Researchers demonstrated that strategically placed stickers on a stop sign could cause it to be classified as a "speed limit 45" sign. The stickers looked like random graffiti to humans, but to the vehicle's AI, they completely changed the sign's meaning. A car running a stop sign at highway speed could be catastrophic.

**Face Recognition Systems:** Specially designed glasses or subtle makeup patterns can fool facial recognition systems, allowing unauthorized individuals to bypass security checkpoints while looking perfectly normal to human guards.

**Malware Detection:** Adversarial perturbations can make malicious code appear benign to AI-powered security tools. The malware functions normally but evades detection systems that would catch conventional threats.

**The Transferability Problem:**

What makes adversarial attacks particularly dangerous is a phenomenon called transferability. Adversarial examples crafted for one model often fool other similar models—even models with different architectures trained on different data.

This means an adversary doesn't need direct access to your specific model. They can create adversarial examples using their own model and those same examples will likely fool yours. This dramatically lowers the bar for attacks—no insider access required, no model theft necessary.

**Defending Against Adversarial Attacks:**

**1. Adversarial Training:** The most effective defense is teaching your model to recognize and resist adversarial perturbations. During training, augment your dataset with adversarial examples and teach the model to correctly classify them. This is like inoculation—exposing the model to attacks during training builds immunity for deployment.

However, adversarial training has costs: it requires more computational resources, can reduce accuracy on normal examples, and provides imperfect protection. It's an arms race—new attack methods can sometimes bypass adversarial training defenses.

**2. Input Validation and Sanitization:** Implement preprocessing pipelines that detect and remove adversarial perturbations. This might include denoising filters, input transformation that destroys carefully crafted perturbations, or ensemble methods that combine multiple models to increase attack difficulty.

**3. Certified Defenses:** Recent research has developed "certified robust" models that provide mathematical guarantees of resilience within specific bounds. These models can prove that no perturbation smaller than a threshold can cause misclassification.

**4. Monitoring and Anomaly Detection:** Deploy runtime monitoring that flags unusual input patterns or confidence distributions. Adversarial examples often produce anomalous activation patterns in hidden layers—patterns invisible in the output but detectable with proper instrumentation.

**Model Inversion: Extracting Secrets from Black Boxes**

Imagine an AI model that predicts health risks based on genetic and medical data. It's deployed as a service—you submit your information, it returns a risk score. Seems safe enough; you're not exposing the training data, just using a model trained on it.

But researchers have shown that careful querying of such models can actually reconstruct training data. This is model inversion—using the model's outputs to infer information about the data it was trained on.

**The Attack Mechanism:**

By systematically querying a model with carefully chosen inputs and observing the confidence of predictions, attackers can essentially work backwards through the model's mathematical transformations. They might not reconstruct exact training examples, but they can extract statistical properties and sometimes remarkably detailed approximations.

**Privacy Implications:**

Model inversion attacks can reveal:
- Medical diagnoses from healthcare AI models
- Financial information from credit scoring models
- Biometric features from face recognition systems
- Personal attributes from recommendation systems

This is particularly concerning because organizations often assume that deploying a trained model is safer than exposing raw training data. Model inversion attacks prove this assumption wrong—the model itself can leak information about its training data.

**Defenses:**

**Differential Privacy:** Add carefully calibrated noise to training data and model outputs. This noise masks individual contributions while preserving overall statistical properties. It's like blurring a photograph just enough that you can't recognize individuals but can still understand the scene.

**Output Rounding and Thresholding:** Reduce the precision of model outputs to prevent attackers from extracting fine-grained information through confidence scores.

**Query Limitations:** Limit how many queries each user can make, making systematic model inversion impractical. However, this must be balanced against legitimate use cases.

**Adversarial Training (Again):** Models trained to resist adversarial examples often show increased resilience to inversion attacks as well.

**Membership Inference: The "Were You in My Training Set?" Attack**

A more subtle but equally concerning attack is membership inference—determining whether a specific individual's data was used to train the model. This might sound harmless, but it has serious privacy implications.

**Why This Matters:**

Consider a model trained on medical records of patients with a stigmatized disease. If an adversary can determine that your record was in the training set, they've potentially learned about your medical condition—even though the model never explicitly outputs diagnoses.

Or imagine a model trained on employee data from companies with layoffs. Confirming that someone's data was in the training set might reveal that they were employed at a specific time, information they wanted to keep private.

**The Attack:**

Membership inference exploits overfitting. Models tend to be more confident about examples they've seen during training compared to new examples. By carefully analyzing confidence scores, attackers can detect this difference and infer membership in the training set.

**Defenses:**

**Regularization:** Strong regularization during training reduces overfitting, making the model's behavior more uniform across training and non-training examples.

**Differential Privacy:** Again, differential privacy provides formal guarantees against membership inference by ensuring individual data points don't significantly influence model outputs.

**Data Augmentation:** Training on augmented versions of data makes it harder to distinguish "saw during training" from "similar to training examples."

**Model Ensembles:** Averaging predictions from multiple models trained on different subsets of data can mask the telltale signs of membership.

**Bringing It All Together**

Runtime attacks on deployed AI systems represent a unique security challenge. Unlike traditional software vulnerabilities that can be patched, many adversarial attacks exploit fundamental properties of how neural networks learn and generalize. There's no perfect patch—only defense-in-depth.

Your security strategy must include:

- **Proactive defenses** during development (adversarial training, differential privacy)
- **Input validation** and sanitization at runtime
- **Monitoring and anomaly detection** to catch attacks in progress
- **Incident response plans** for when adversarial attacks are detected
- **Regular red team exercises** to test model resilience

Work with your CISO to integrate AI-specific threat scenarios into your security operations. Traditional penetration testing won't catch adversarial example vulnerabilities—you need specialized expertise and tools.

Remember: AI security isn't a checkbox on a compliance form. It's an ongoing discipline requiring constant vigilance, updated defenses, and collaboration between AI developers, security professionals, and privacy officers. The threats are real, sophisticated, and evolving. But with proper awareness and defenses, you can build AI systems that are not just powerful but also secure and privacy-preserving.""",
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
                """**Learning Objectives:**
- Document the purpose and use cases of the AI system comprehensively
- Identify who will operate and be impacted by the system, including indirect stakeholders
- Assess impact on children and vulnerable groups with specific risk scenarios
- Analyze impact on Human Rights and Cultural Values across all three categories
- Evaluate social and environmental impact with concrete examples
- Identify foreseeable errors and misuse scenarios through threat modeling
- Document high-level framework for managing risk and fairness

---

**The Foundation of Trustworthy AI: Context, Risk, and Fairness**

Building a trustworthy AI system begins not with algorithms or architectures, but with fundamental questions about purpose, people, and potential harms. Before writing a single line of code, you must deeply understand the context in which your AI will operate and the risks and fairness challenges it may create.

This isn't a box-checking exercise—it's a critical thinking process that can reveal showstopping issues early, when they're still manageable. Getting this foundation right can mean the difference between an AI system that genuinely serves people and one that perpetuates harm at scale.

**Two Interwoven Threads: Risk and Fairness**

Think of risk and fairness as two threads woven together throughout your AI system's lifecycle. They're distinct but deeply connected concerns that must be addressed in parallel.

**The Risk Thread** asks: "What could go wrong?" This encompasses both intended use cases and foreseeable misuse. Who will use the AI? For what purpose? Who will be affected by its decisions? What happens if someone deliberately misuses it? What if they accidentally provide bad inputs?

**The Fairness Thread** asks: "Could this system treat people unfairly?" This focuses on biases in data and algorithmic decision-making that might lead to discriminatory outcomes. Even well-intentioned AI systems can perpetuate and amplify societal biases if we don't actively identify and mitigate them.

These threads intertwine constantly. A risk might be that your hiring AI is used in ways that violate employment law. The fairness issue might be that it systematically discriminates against certain demographics. They're two perspectives on the same fundamental challenge: ensuring your AI serves all people equitably and safely.

**Establishing Context: The Critical Questions**

Before assessing risks and fairness issues, you must thoroughly understand your AI system's context. This requires honest, detailed answers to fundamental questions:

**What is the purpose of your AI system?**

Be specific. "Improve healthcare" is too vague. "Predict 30-day hospital readmission risk for heart failure patients to enable targeted follow-up interventions" is better—it defines the specific task, the population, and the intended intervention.

**What are the use cases?**

Document not just the primary use case but edge cases and boundary conditions. Will doctors use your diagnostic AI as a second opinion tool? Or will it autonomously make decisions? Will it handle pediatric patients? Elderly patients with comorbidities? These distinctions matter enormously for risk assessment.

**Who will operate the system?**

Are they medical professionals with years of training? Customer service representatives with minimal technical background? Teenagers using a consumer app? Operator expertise fundamentally shapes risk—experts can catch obvious errors; novices might blindly trust AI outputs.

**Who will the system impact?**

Consider direct and indirect impacts. A loan approval AI directly impacts applicants. It indirectly impacts their families, the neighborhoods where businesses can't get funding, and entire communities facing systemic disadvantage. Cast a wide net—hidden stakeholders often face the greatest harms.

**Will it affect children or other vulnerable groups?**

This is critical. Children, elderly individuals, people with disabilities, refugees, and other vulnerable populations require special protections. Their data may need extra safeguards. The AI's decisions may have amplified impacts on their lives. EU AI Act and SDAIA principles specifically call out protection of vulnerable groups.

**In what languages and geographies will it be deployed?**

Cultural context shapes everything. An AI system designed for Saudi Arabia must respect Islamic values and Arabic language nuances. Deploying that same system in Sweden without adaptation could cause serious issues. Language models perform differently across languages—especially for lower-resource languages.

**Identifying Risk and Fairness Issues**

With context established, systematically identify potential issues across three broad categories:

**1. Human Rights and Cultural Values Impact**

AI systems can affect fundamental human rights in ways traditional software rarely does. Consider:

**Civil and Political Rights:** Does your system affect liberty, free expression, privacy, or protection from discrimination? A content moderation AI that disproportionately removes posts from political minorities affects free expression. A surveillance system that enables tracking without warrants affects liberty and privacy.

**Economic, Social, and Cultural Rights:** Does it affect access to fair wages, education, or healthcare? A hiring AI that screens out qualified candidates affects economic rights. An educational AI that provides lower-quality tutoring to disadvantaged students perpetuates educational inequality.

**Collective Rights:** Does it affect minority groups, genders, or indigenous peoples? An AI trained primarily on Western medical data may perform poorly for other populations. A language AI that lacks cultural context may misunderstand indigenous communication styles.

**Real-World Example:** In 2019, researchers found that commercial facial recognition systems had error rates up to 34% higher for darker-skinned women compared to lighter-skinned men. This disparity affected access to services and raised fundamental fairness concerns about deploying such systems in security or authentication contexts.

**2. Social and Environmental Impact**

Look beyond individual users to broader societal effects:

**Social Impact:** Consider second-order effects. Social media recommendation algorithms don't just show content—they shape what people believe, who they interact with, and how societies polarize. Cambridge Analytica demonstrated how micro-targeted advertising could potentially affect elections. Your AI's social impact might extend far beyond its immediate function.

**Environmental Impact:** Large AI models consume enormous energy. Training GPT-3 reportedly emitted as much carbon as five cars over their lifetimes. If your application requires training massive models or running inference at scale, the environmental cost becomes a fairness issue—future generations bear the environmental cost of today's AI convenience.

**3. Foreseeable Errors and Misuse**

Think like an adversary or a careless user:

**Input Errors:** What happens if someone enters "9999" or "0000" as defaults? What if units are wrong—pounds instead of kilograms for medical dosing? What if dates are in the wrong format? Real systems encounter real garbage inputs. Your AI should handle them gracefully.

**Misuse Scenarios:** Could your AI be weaponized? A deepfake generator intended for entertainment could be used for fraud or harassment. A powerful language model could generate sophisticated phishing emails. Document foreseeable misuse—not to avoid building useful systems, but to implement appropriate safeguards.

**Building Your Framework**

Document all of this in a comprehensive Risk and Fairness Framework document. This becomes your north star throughout development. It should include:

- Detailed context analysis
- Identified risks categorized by type and severity
- Identified fairness concerns with affected groups
- Mitigation strategies for each identified issue
- Metrics for monitoring risks and fairness post-deployment
- Escalation procedures when issues are detected

This document is living—update it as you learn more. But starting with this foundation ensures you're building an AI system with eyes wide open to its potential impacts.

**The Bottom Line**

Understanding context and identifying risks and fairness issues isn't about being pessimistic—it's about being responsible. Every powerful technology can be used well or poorly, can help some while harming others. By systematically thinking through these issues before they become concrete problems, you dramatically increase the likelihood of building AI that genuinely serves everyone fairly and safely.

In the following sections, we'll explore specific types of bias, technical fairness metrics, and practical mitigation strategies. But none of that matters if you haven't first established this fundamental understanding of what you're building, who it affects, and what could go wrong.""",
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
                """**Learning Objectives:**
- Understand how biased feedback loops develop and self-reinforce
- Learn the five-step process of bias escalation in AI systems
- Identify design measures to prevent bias at the architectural level
- Understand process measures for ongoing bias detection and correction
- Learn operator training requirements to prevent misuse
- Understand human oversight requirements (in-the-loop vs out-of-the-loop)
- Learn about automation bias and strategies to prevent over-reliance on AI

---

**The Vicious Cycle: When AI Bias Feeds on Itself**

Perhaps the most insidious challenge in AI fairness is the biased feedback loop—a phenomenon where an AI system's decisions create the very data that reinforces and amplifies its biases. It's a vicious cycle that can turn minor biases into systemic discrimination over time.

**The Anatomy of a Feedback Loop**

Consider a police predictive policing AI system. Here's how bias can spiral:

**Step 1: Biased Input Data** - Historical crime data shows more arrests in predominantly minority neighborhoods. But this reflects policing practices (more police presence in these areas) as much as actual crime rates.

**Step 2: AI Decision Making** - The AI learns that these neighborhoods are "high crime" areas and recommends concentrating police resources there.

**Step 3: Feedback Loop** - More police in these neighborhoods leads to more arrests, more stops, more data showing "high crime."

**Step 4: Reinforcement** - This new data further trains the model that these neighborhoods require heavy policing.

**Step 5: Escalation** - Over years, the disparity grows. Neighborhoods get labeled "high crime" not because of actual crime rates but because of self-fulfilling police deployment patterns driven by biased AI.

This isn't hypothetical—multiple cities have grappled with exactly this pattern in predictive policing systems.

**The Credit Scoring Catastrophe**

Another real-world example: Consumer credit risk models in the US historically used ZIP codes as risk proxies. Because of racist housing policies like redlining, predominantly Black neighborhoods had lower credit availability and higher debt burdens—not because residents were less creditworthy, but because of systematic discrimination.

AI credit models learned this pattern. They denied loans to people in these ZIP codes. This made it harder for residents to build credit history. Lack of credit history further reinforced the model's assessment that these areas were "risky." The feedback loop perpetuated and amplified decades-old discrimination through seemingly neutral algorithmic decision-making.

**Breaking the Cycle: Four Mitigation Categories**

Addressing feedback loops requires a multi-layered defense strategy across design, processes, training, and oversight:

**1. Design Measures: Building Resilience into the System**

Smart system design can prevent feedback loops before they start:

**Input Validation:** Code your model to produce error messages for out-of-range inputs. If someone enters "9999" or defaults, the system should flag this rather than learning from garbage data.

**Bias-Aware Architecture:** Design models that explicitly monitor for demographic disparities in predictions. If the hiring AI starts showing different acceptance rates across groups, this should trigger automatic alerts.

**Proxy Variable Elimination:** Carefully audit which features the model uses. Is ZIP code really predictive, or is it a proxy for race? Remove or carefully control variables that might be proxies for protected attributes.

**Cautionary Tale:** Google's 2015 photo labeling AI infamously tagged photos of Black people as "gorillas." They attempted to "fix" this by removing "gorilla" as a label entirely rather than addressing the underlying bias in training data. That's not bias correction—it's hiding the problem.

**2. Process Measures: Continuous Monitoring and Correction**

Bias detection must be ongoing, not a one-time check:

**Regular Fairness Audits:** Test your model quarterly (or more frequently for high-risk systems) against fairness metrics. Are disparities growing? Document trends over time.

**A/B Testing for Fairness:** When updating models, run them in parallel to compare not just accuracy but fairness metrics. Sometimes accuracy improves while fairness degrades—you need to catch this.

**Feedback Data Auditing:** Regularly examine the data being fed back into your system. Is it representative? Are certain groups overrepresented or underrepresented? Rebalance before retraining.

**Corrective Protocols:** Document exactly what happens when bias is detected. Who is notified? What are the thresholds for pausing the system? How quickly must fixes be implemented? Having these protocols defined before a crisis ensures swift response.

**3. Operator Training: Empowering People to Question AI**

Technology alone won't prevent bias—people must understand how to use AI responsibly:

**Fairness Risk Training:** Operators must understand not just how to use the system but what can go wrong. What are the potential biases? What are the signs something is malfunctioning?

**Risk Pathway Education:** Help operators understand causal pathways leading to risks. If they grasp that the hiring AI might penalize candidates from certain universities because of biased historical hiring, they'll know to scrutinize those recommendations.

**Appropriate Use Definitions:** Clearly define when operators should NOT use the AI. A medical diagnostic AI trained on adults shouldn't be used for pediatric patients. A loan approval AI trained on one market shouldn't be applied to others. Make these boundaries explicit and enforce them.

**4. Human Oversight: Keeping Humans in the Loop**

AI should augment human judgment, not replace it:

**In-the-Loop (HITL):** For high-stakes decisions, require human approval. The AI recommends; humans decide. This is crucial for hiring, lending, medical diagnoses, and other decisions with major life impacts.

**Out-of-the-Loop (OOTL):** For lower-stakes or high-volume decisions, humans review samples after decisions are made. This allows efficiency while maintaining oversight.

**Interpretability Tools:** Give operators tools to understand WHY the AI made a recommendation. Feature importance scores, counterfactual explanations, and similar-case comparisons help humans spot when AI reasoning is flawed.

**Override Mechanisms:** Operators must be able to override AI decisions without excessive friction. If the override process is too burdensome, operators will rubber-stamp AI recommendations even when they suspect problems.

**Combating Automation Bias**

Perhaps the biggest human factors challenge is automation bias—the tendency to over-trust AI recommendations. Studies show that even when humans are told AI might be wrong, they often defer to it anyway.

**Countermeasures:**

- **Devil's advocate protocols:** For critical decisions, assign someone to argue against the AI's recommendation
- **Confidence calibration:** Show operators historical AI error rates to calibrate trust appropriately
- **Decision provenance:** Require operators to document their reasoning, forcing active engagement rather than passive acceptance
- **Periodic blind reviews:** Occasionally give operators recommendations from both AI and random/baseline systems without labeling which is which. This keeps critical thinking skills sharp.

**The Bottom Line**

Biased feedback loops represent AI's potential to perpetuate injustice at unprecedented scale. But they're not inevitable. Through thoughtful design, rigorous monitoring, comprehensive training, and meaningful human oversight, you can break these cycles before they spiral.

The key is recognizing that bias mitigation isn't a one-time task—it's an ongoing commitment built into every stage of your AI system's lifecycle.""",
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
                """**Learning Objectives:**
- Identify measurement bias in your data collection and instrumentation
- Understand the three types of sampling bias and their real-world impacts
- Recognize survivorship bias in historical data analysis
- Learn about recency bias and its effects on temporal patterns
- Understand data processing biases introduced during cleaning and preparation
- Identify cultural bias in AI systems deployed across diverse populations
- Learn about exclusion and confirmation bias in feature selection

---

**The Taxonomy of Bias: Know Your Enemy**

Data is like a map—and biases are the ways that map distorts the landscape it's supposed to represent. Just as a map might exaggerate some features and minimize others, your training data inevitably contains distortions. The question isn't whether bias exists—it does—but whether you can identify and correct it.

Let's explore the major types of bias that plague AI systems, with practical examples to help you spot them in your own projects.

**1. Measurement Bias: Faulty Instruments, Faulty Data**

This occurs when your measurement process systematically skews results. Think of a bathroom scale that's 5 pounds off—every measurement is consistently wrong.

**Real-world examples:**
- **Medical AI:** Blood pressure cuffs sized for average adults give inaccurate readings for very large or very small patients. An AI trained on this data learns incorrect risk profiles for these populations.
- **Sentiment analysis:** Asking people to rate happiness on a 1-10 scale is subjective. Different cultures interpret scales differently—some avoid extremes, others use the full range. The AI learns cultural response patterns, not actual sentiment.

**Detection:** Look for systematic differences in measurement quality across subgroups. Are certain populations measured with different tools or processes?

**2. Sampling Bias: The Wrong Map for the Territory**

This is perhaps the most common and dangerous bias type—when your training data doesn't represent the population you'll deploy to.

**Non-Response Bias:** Your survey uses QR codes. Tech-savvy people respond; others don't. Your sample skews young and affluent, missing perspectives of elderly or less digitally connected populations.

**Under-Coverage Bias:** Facial recognition systems trained predominantly on lighter-skinned faces perform poorly on darker skin tones. The training set under-covers the actual diversity of faces the system will encounter.

**Availability Bias:** Medical AI trained on hospital records has far more data about sick people than healthy people. It may learn to detect illness well but struggle to recognize wellness, potentially overdiagnosing conditions.

**Detection:** Compare demographic distributions in your training data to your intended deployment population. Gaps reveal under-coverage.

**3. Survivorship Bias: The Silent Evidence**

You only see the survivors—literally or metaphorically—missing crucial information about what didn't survive to be measured.

**Classic example:** WWII bombers that returned from missions showed damage in certain areas. Analysts initially recommended reinforcing those areas—until someone realized they were only seeing planes that survived despite that damage. The fatal hits were in areas with no damage on returning planes, because planes hit there didn't return. They needed to reinforce where returning planes *weren't* damaged.

**AI applications:** Training a loan default predictor only on people who got loans. You're missing everyone who was denied—potentially creditworthy people who would have repaid. Survey data about living with a disease underrepresents those who died from it, biasing severity assessments.

**Detection:** Ask "Who or what is missing from this dataset by design?" Document exclusion criteria explicitly.

**4. Recency Bias: Forgetting the Past**

Recent data gets disproportionate weight, missing long-term trends.

**Example:** A weather prediction AI trained primarily on recent years might miss climate change patterns visible in longer historical data. Similarly, a market prediction AI trained mostly on post-2008 financial data might not recognize patterns that preceded the crash.

**Detection:** Plot your data's temporal distribution. Are recent years over-represented? Does performance degrade on older test data?

**5. Data Processing Bias: The Cleanup That Corrupts**

Introduced during the cleaning and preparation phase, often with good intentions that backfire.

**Outlier Bias:** Averaging or binning data can mask important diversity. If you bin ages into decades, you lose the distinction between 51 and 59—potentially crucial for certain applications. When variance within bins is high, averages are misleading.

**Algorithmic Bias:** The aggregation or normalization algorithm itself might favor certain outcomes. For example, using mean instead of median for skewed distributions systematically distorts representation.

**Detection:** Compare raw and processed data distributions. What information was lost in processing?

**6. Cultural Bias: One Size Doesn't Fit All**

Models trained in one cultural context often fail in others.

**Examples:**
- **Gesture recognition AI** trained in Western contexts might misinterpret gestures that have different meanings elsewhere (thumbs up is offensive in some cultures)
- **Language AI** trained primarily on formal English text struggles with dialects, code-switching, or non-Western names
- **Recommendation systems** assuming nuclear family structures fail for cultures with different family configurations

**Detection:** Test your AI across cultural contexts. Involve diverse stakeholders in design and validation.

**7. Exclusion Bias: What You Don't Collect**

You systematically exclude certain data types, often unconsciously based on preconceptions about what's "relevant."

**Example:** A hiring AI trained only on successful employees' resumes. You've excluded rejected candidates who might have succeeded if given a chance—especially if historical hiring was biased. Your AI learns to perpetuate past bias by only seeing one side of the decision.

**Detection:** Explicitly document what data you're excluding and why. Question each exclusion—is it truly irrelevant, or might it contain important signal?

**8. Confirmation Bias: Seeing What You Expect**

Humans interpret data to support pre-existing beliefs, affecting what features we choose and how we frame problems.

**Example:** Believing that certain neighborhoods are "high risk," you might include ZIP code as a feature and interpret its strong predictive power as validation rather than recognizing it as a proxy for historical discrimination.

**Detection:** Use diverse teams. People with different backgrounds and beliefs are less likely to share the same blind spots. Document feature selection rationale before seeing results.

**Putting It Together**

Bias comes from everywhere—measurement instruments, sampling strategies, what survives to be measured, what's recent, how you process, cultural assumptions, what you exclude, and what you expect to find. No dataset is perfect.

The goal isn't perfection—it's awareness and mitigation. Systematically audit your data for each bias type. Document what you find. Take corrective action where possible, and for biases you can't eliminate, ensure your model's users understand the limitations.""",
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
                """**Learning Objectives:**
- Understand the difference between group and individual fairness metrics
- Learn when to use each fairness metric based on your application context
- Understand how to calculate Disparate Impact and interpret results
- Learn about Equal Opportunity vs Equalized Odds tradeoffs
- Understand the Theil Index for measuring benefit distribution inequality
- Learn how to set appropriate fairness thresholds for your use case
- Understand the 80% rule and its regulatory applications
- Document fairness metric selection and justification

---

**From Philosophy to Numbers: Measuring Fairness**

"Fairness" sounds simple until you try to define it precisely. Does fairness mean everyone gets the same outcome? The same treatment? The same opportunity? Remarkably, these intuitions can be mathematically incompatible—optimizing for one definition of fairness may worsen another.

This is why we need formal fairness metrics: quantitative measures that let us detect, monitor, and mitigate discrimination in AI systems. Let's explore the key metrics and when to use each.

**Group Fairness: Comparing Outcomes Across Demographics**

These metrics compare how an AI system treats different demographic groups:

**1. Disparate Impact (DI):** The ratio of positive outcomes for a protected group versus a non-protected group.

**Formula:** DI = (Positive rate for Group A) / (Positive rate for Group B)

**Example:** A hiring AI accepts 60% of male candidates and 45% of female candidates. DI = 45%/60% = 0.75 (or 75%).

**Interpretation:** Values close to 1.0 indicate parity. The "80% rule" (from US employment law) states that DI should be at least 0.80—if it's lower, there may be discrimination. In this example, the 75% DI suggests potential bias.

**2. Demographic Parity (DP):** Stricter than DI—requires that predictions be statistically independent of sensitive attributes. Every demographic group should receive positive outcomes at the same rate.

**When to use:** Consumer applications where everyone should have equal access regardless of demographics. Credit approval, housing, employment screening.

**Limitation:** Sometimes groups have legitimately different base rates. Enforcing demographic parity can reduce accuracy if there are true differences in outcomes.

**3. Equal Opportunity (EO):** Requires that the True Positive Rate (recall) be similar across groups. Among qualified individuals, everyone should have equal chance of being identified as qualified.

**Formula:** TPR = (True Positives) / (True Positives + False Negatives)

**Example:** A medical diagnostic AI should have similar sensitivity for all demographic groups—if it catches 90% of disease cases in one group, it should catch ~90% in others.

**When to use:** When false negatives are particularly harmful. Medical diagnosis, fraud detection (missing real fraud), safety-critical applications.

**4. Equalized Odds (EOdds):** More stringent than EO—requires both True Positive Rates AND False Positive Rates to be balanced across groups.

**When to use:** When both false positives and false negatives have significant consequences. Criminal justice risk assessment, loan approvals, hiring decisions.

**The Tradeoff:** Equalized Odds is harder to achieve than Equal Opportunity but provides more comprehensive fairness protection.

**5. Treatment Equality (TE):** Groups with similar risk profiles should receive similar treatment and outcomes. Focuses on the ratio of errors—false positives to false negatives should be similar across groups.

**When to use:** Resource allocation contexts where different error types have different costs.

**Individual Fairness: Similar People, Similar Treatment**

Group fairness metrics can miss individual-level discrimination. Individual fairness metrics address this:

**6. Individual Fairness:** "Similar individuals should receive similar predictions regardless of protected attributes."

**Challenge:** Defining "similar" is subjective and domain-dependent. Two job candidates might be similar in skills but different in experience—is that fair or unfair differentiation?

**Implementation:** Use distance metrics to measure similarity, then require that prediction differences are bounded by similarity differences.

**7. Theil Index:** Measures inequality in benefit allocation. Borrowed from economics, it quantifies how unequally benefits (or harms) are distributed.

**Scale:** 0 = perfect equality (everyone receives equal benefits); higher values indicate greater inequality.

**When to use:** Resource distribution scenarios—who gets access to services, credit, opportunities.

**8. Consistency:** Measures whether k-nearest neighbors receive similar predictions. A consistency score of 1.0 means each instance has the same prediction as its k nearest neighbors.

**When to use:** As a check against arbitrary predictions. Low consistency may indicate the model is making inconsistent decisions for similar cases.

**Setting Thresholds: Where to Draw the Line**

Fairness metrics give you numbers, but what threshold defines "fair enough"?

**The 80% Rule:** Derived from US Equal Employment Opportunity Commission guidelines, this states that a selection rate for any group should be at least 80% of the rate for the highest-selected group. If your best-performing demographic has a 70% acceptance rate, others should be at least 56% (0.80 × 70%).

**Regulatory Context:** Many jurisdictions and sectors have specific fairness requirements:
- **EU AI Act:** High-risk systems must implement bias detection and correction
- **US Fair Lending:** Specific thresholds for credit decisions
- **Employment law:** Varies by jurisdiction but often references the 80% rule

**Context Matters:** A medical diagnostic AI should have near-perfect parity (close to 1.0) because lives are at stake. A music recommendation system might tolerate more variance because consequences are minimal.

**Bidirectional vs Unidirectional:**
- **Unidirectional:** Only concerned if one specific group is disadvantaged (e.g., protected group must have at least 80% of majority group's rate)
- **Bidirectional:** Concerned about disparity in either direction (both groups must be within 80-120% of each other)

**Document Your Decisions:** Whatever thresholds you choose, document:
- Which metrics you're using and why
- What thresholds you've set
- The rationale (regulatory requirements, ethical considerations, stakeholder input)
- How you'll monitor and respond to violations
- Any tradeoffs you're making (e.g., accepting slight demographic parity violations to achieve better equal opportunity)

**The Impossibility of Perfect Fairness**

Here's the uncomfortable truth: in many real-world scenarios, you cannot simultaneously satisfy all fairness definitions. Optimizing for demographic parity might worsen equalized odds. Achieving individual fairness might violate group fairness constraints.

This doesn't mean fairness is impossible—it means fairness requires choices. You must decide which fairness definitions matter most for your application, set appropriate thresholds, monitor continuously, and transparently communicate your decisions and their limitations.

**Practical Implementation:**

1. **Select 2-3 key metrics** aligned with your application's ethical priorities
2. **Set thresholds** based on regulatory requirements and stakeholder input
3. **Automate monitoring** to track metrics on ongoing predictions
4. **Create alerts** when thresholds are violated
5. **Regular audits** (quarterly minimum for high-risk systems)
6. **Transparency reports** documenting fairness performance over time

Fairness isn't a destination—it's an ongoing commitment to measurement, monitoring, and improvement.""",
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
