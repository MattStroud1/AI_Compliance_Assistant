"""
ROPA (Record of Processing Activities) Pathway
Based on UK GDPR Article 30 compliance requirements
A step-by-step guide for creating and maintaining a comprehensive ROPA
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


class ROPAPathway:
    """
    ROPA pathway for creating and maintaining Records of Processing Activities
    Based on UK GDPR Article 30 requirements
    """

    def __init__(self):
        self.pathway_name = "ROPA (Record of Processing Activities)"
        self.description = "9-step journey for creating and maintaining UK GDPR Article 30 compliant records"

    def create_phases(self, project_id: str) -> List[NEOMPhase]:
        """Create ROPA phases: Planning, Data Collection, Documentation, Maintenance"""
        return [
            self._create_phase_1_planning(project_id),
            self._create_phase_2_data_collection(project_id),
            self._create_phase_3_documentation(project_id),
            self._create_phase_4_maintenance(project_id),
        ]

    def _create_step(self, project_id: str, phase: PhaseType, order: int,
                     task_id: str, title: str, description: str, checklist: List[str]) -> ComplianceStep:
        """Helper to create a compliance step"""
        return ComplianceStep(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase=phase,
            order=order,
            title=f"Step {task_id}: {title}",
            description=description,
            status=StepStatus.NOT_STARTED,
            checklist_items=checklist,
            resources=[],
            guidance="",
        )

    def _create_phase_1_planning(self, project_id: str) -> NEOMPhase:
        """Phase 1: Planning & Scoping (Steps 1-2)"""

        steps = [
            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 1, "1",
                "Determine Your ROPA Obligations and Scope",
                """**Why this matters:** Understanding whether your organisation is required to maintain a Record of Processing Activities is the foundation. Under UK GDPR Article 30, most organisations must keep records of their personal data processing activities as a core part of the accountability principle (Article 5(2)). Even smaller organisations (fewer than 250 employees) should assess if they need a ROPA, because exemptions are limited. Article 30(5) provides a derogation for SMEs with under 250 staff, but only if the processing is occasional, low-risk to individuals, and doesn't involve special-category or criminal-offence data. In practice, regular business activities (employee records, customer data, etc.) or any sensitive data mean you must keep a ROPA despite the SME threshold.

**What to do:** Identify whether your organisation acts as a data controller, data processor, or both, because Article 30 sets different documentation requirements for each role. Controllers make decisions about why and how personal data is processed, whereas processors handle data on behalf of a controller. Determine if you meet the SME exemption criteria. If you have 250+ employees, a ROPA is mandatory for all processing activities. If under 250, list out any processing that is not strictly occasional, that might pose risks to rights/freedoms (e.g. profiling, large-scale use), or that includes special categories (health, race, biometrics, etc.) or criminal data.

**How to proceed:** If you conclude that few of your processes fall entirely outside Article 30's scope, plan to document all processing for completeness. This avoids accidental omissions and is aligned with GDPR's demonstration of compliance mandate (Recital 82). Make senior management aware of the legal duty to produce these records on request to the ICO, and the potential fines for non-compliance (up to £8.7 million or 2% of global turnover).""",
                [
                    "Identify roles: Are we acting as a controller, a processor, or both for different activities?",
                    "Employee threshold: Do we have 250+ employees (then full ROPA required) or fewer?",
                    "Exemption conditions: If <250 employees, list any processing that is regular (not one-off), higher-risk, or involves special/criminal data",
                    "Management buy-in: Inform leadership of the legal requirement (Article 30) and consequences",
                    "Decision: Conclude that a ROPA will be created and note any truly out-of-scope one-off activities",
                    "Document which role(s) your organisation plays: controller, processor, or both"
                ]
            ),

            self._create_step(
                project_id, PhaseType.PLANNING_DESIGN, 2, "2",
                "Assign Responsibility and Resources",
                """**Why this matters:** Creating a ROPA is a cross-organisational project that needs clear ownership. UK GDPR doesn't explicitly say who must compile the ROPA, but under the accountability principle the controller is responsible for compliance. In practice, designating a responsible person or team (often the Data Protection Officer if you have one, per Article 37) ensures that the task is managed effectively and that knowledge from across the business is gathered. The DPO or privacy officer usually has the expertise to interpret GDPR requirements and coordinate input, making them well-suited to lead this effort. Having a defined owner and sufficient resources is crucial for staying on schedule and producing an accurate ROPA.

**What to do:** Form a small project team for the ROPA. This typically includes the DPO or privacy lead, plus representatives from key departments (IT, HR, Marketing, Finance, etc.) who understand the data processed in their functions. Each department can nominate a point of contact to work with the ROPA lead. Secure management support for this initiative – for example, get executive sponsorship to underscore its importance and to allocate time and tools needed. Also determine who will maintain the record going forward (often the DPO or an information governance team) to keep it up to date.

**How to carry it out:** Kick off with an internal meeting or memo explaining the ROPA project and roles. Clearly outline the information that will be needed from each business area. Set a realistic timeline with milestones. Provide training or guidance to team members if they are unfamiliar with terms like "processing purpose" or "special category data," so that inputs are accurate. You might use a shared spreadsheet or a collaborative tool to collect information, so ensure everyone has access. Regular check-ins can help track progress.""",
                [
                    "Designate a ROPA project lead (typically DPO or privacy officer)",
                    "Form a project team with representatives from key departments (IT, HR, Marketing, Finance, etc.)",
                    "Nominate a point of contact in each department to provide data processing information",
                    "Secure executive sponsorship and management support for the initiative",
                    "Allocate budget for any tools or software needed (privacy management platforms, templates, etc.)",
                    "Determine who will maintain the ROPA going forward",
                    "Set up a collaborative tool or shared system for collecting information",
                    "Create a project timeline with clear milestones",
                    "Schedule regular check-in meetings (weekly or biweekly) to track progress",
                    "Provide training to team members on GDPR terminology and requirements"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.PLANNING_DESIGN,
            name="Phase 1: Planning & Scoping",
            description="Establish ROPA obligations, assign responsibilities, and set up the project framework",
            order=1,
            steps=steps
        )

    def _create_phase_2_data_collection(self, project_id: str) -> NEOMPhase:
        """Phase 2: Data Collection & Mapping (Steps 3-5)"""

        steps = [
            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 3, "3",
                "Identify and Map All Personal Data Processing Activities",
                """**Why this matters:** You can't document what you don't know about. The cornerstone of a good ROPA is a complete inventory of your processing activities – essentially all instances where personal data is collected, used, shared, stored, or deleted. This mapping fulfills the GDPR's expectation that controllers know their data flows (a prerequisite for transparency and security obligations). It also directly ties to Article 30's requirement to document each "processing activity under its responsibility". Taking time to systematically identify these activities prevents omissions that could lead to non-compliance.

**What to do:** Conduct an information audit or data-mapping exercise across the organisation. Start high-level: list your organisation's main functions or departments, as each will handle personal data in different contexts (e.g. HR, customer service, marketing, IT, sales, etc.). For each area, brainstorm or use questionnaires to capture the specific processing activities. A processing activity can be thought of as a distinct business process involving personal data. Don't forget internal processes (IT logging, building access logs) and support functions (legal, finance) if they handle personal data.

**How to carry it out:** Use a consistent set of scoping questions to ensure you cover all relevant aspects. The ICO suggests starting with basic questions for each business function: "Why do you use personal data? Who do you hold information about? What information do you hold? Who do you share it with? How long do you keep it? How do you keep it safe?" These questions, posed to each department, will tease out the different processing activities and their purposes.""",
                [
                    "List all main departments and business functions in your organisation",
                    "For each department, identify distinct processing activities (e.g., HR: recruitment, payroll, performance reviews)",
                    "Use scoping questions: Why use personal data? Who is the data about? What data do you hold?",
                    "Ask: Who do you share data with? How long is it kept? How is it secured?",
                    "Include customer/client-facing processes (sales, marketing, customer service)",
                    "Include internal processes (IT logging, access logs, employee monitoring)",
                    "Include support functions (legal, finance, facilities)",
                    "Cover all data subject groups: customers, employees, contractors, partners, vendors",
                    "Create a master list of all processing activities identified",
                    "Assign a tentative name and description to each processing activity"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 4, "4",
                "Define the Information You Need to Record (ROPA Content Requirements)",
                """**Why this matters:** Article 30 UK GDPR explicitly lists what information must be included in your ROPA for each processing activity. Ensuring you know these requirements up front is vital so you can gather the right details and structure your record correctly. Controllers have a more extensive list to document than processors, reflecting their greater responsibility for determining the "why and how" of processing. By defining all required data points (and some extra recommended ones), you create a template that meets legal obligations and is useful for compliance management.

**What to do:** Set up a ROPA template or table listing all the fields you need to fill in for each processing activity. At minimum, include every element mandated by Article 30.

**UK GDPR Article 30 required content for Controllers:**
- Name and contact details of the controller (and any joint controllers)
- Contact details of the Data Protection Officer (if designated)
- Purpose of the processing
- Categories of data subjects (whose data is being processed)
- Categories of personal data (types of data being processed)
- Categories of recipients (who the data is disclosed to)
- International transfers (details of any data transferred outside UK, including safeguards)
- Retention schedule (how long data is kept)
- General description of technical and organisational security measures
- Representative's details (if applicable)

**Additional recommended fields:**
- Lawful basis for processing (e.g., Contract, Consent, Legitimate Interests)
- Source of data (especially if not obtained directly from individuals)
- Use of processors or sub-processors
- Related documents (DPIA, privacy notice, data sharing agreements)
- Special category/criminal data conditions (if applicable)
- Automated decision-making or profiling flags
- Data storage location
- Date of last review or update""",
                [
                    "Create a ROPA template with all Article 30 required fields",
                    "Add columns for: Controller name/contact, DPO contact, Purpose",
                    "Add columns for: Data subjects, Personal data categories, Recipients",
                    "Add columns for: International transfers & safeguards, Retention period",
                    "Add column for: Security measures description",
                    "Include optional but recommended fields: Lawful basis, Data source",
                    "Include fields for: Processors used, Related DPIAs, Privacy notice references",
                    "For special category data: Add fields for legal condition and Appropriate Policy Document",
                    "Add fields for: Automated decision-making, Profiling, Data storage location",
                    "Add administrative fields: Process owner, Last updated date, Version number",
                    "Create separate templates for Controller vs Processor roles if needed",
                    "Ensure template is in an editable format (spreadsheet, document, or privacy management system)"
                ]
            ),

            self._create_step(
                project_id, PhaseType.DATA_PREPARATION, 5, "5",
                "Collect Detailed Information for Each Processing Activity",
                """**Why this matters:** With your list of processing activities (from Step 3) and a template of required details (from Step 4), you now need to gather accurate information to fill in each section of the ROPA. This step is critical because the quality of your ROPA depends on how precise and complete this information is. Gathering input is often the most time-consuming part, as it involves coordination across the organisation. It's also where you validate that your understanding of processes is correct. Diligent data collection supports the accuracy principle (Article 5(1)(d)) – your records must be accurate and up-to-date to truly demonstrate compliance.

**What to do:** For each processing activity identified, collect the information needed to populate every field of your ROPA template. Engage with the people who know the process best: process owners, IT staff, legal/compliance staff, records management, security officers, and the DPO.

**How to carry it out:** Create a data-gathering questionnaire for each processing activity. This could be an online form or a document that asks for each field's information. Distribute questionnaires and follow up with meetings to clarify answers. Ensure completeness – if a respondent leaves a field blank, you need to investigate. Cross-check with existing resources like privacy notices or past DPIAs. If discrepancies arise, resolve them to improve overall compliance.""",
                [
                    "Create a data-gathering questionnaire covering all ROPA template fields",
                    "Distribute questionnaire to process owners in each department",
                    "For each activity, collect: Purpose, Data subjects, Personal data types",
                    "Collect: Lawful basis, Recipients, International transfers (if any)",
                    "Collect: Retention period, Security measures, Data source",
                    "Engage IT staff for: Systems used, Storage locations, Technical security measures",
                    "Engage Legal/Compliance for: Legal bases, Retention periods, Contracts/agreements",
                    "Engage Security/CISO for: Security measures (encryption, access controls, etc.)",
                    "Consult DPO for: Lawful bases, DPIA requirements, Overall compliance validation",
                    "Collect copies of supporting documents: Policies, contracts, privacy notices, DPIAs",
                    "Follow up on any blank or unclear responses",
                    "Cross-check information with existing privacy notices and DPIAs",
                    "Identify any processing activities that may require a DPIA (if not already done)",
                    "Track missing information and assign action items to obtain it"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DATA_PREPARATION,
            name="Phase 2: Data Collection & Mapping",
            description="Identify all processing activities, define ROPA requirements, and collect detailed information",
            order=2,
            steps=steps
        )

    def _create_phase_3_documentation(self, project_id: str) -> NEOMPhase:
        """Phase 3: Documentation & Integration (Steps 6-8)"""

        steps = [
            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 6, "6",
                "Document Each Processing Activity in the ROPA Format",
                """**Why this matters:** Now it's time to actually build the record – turning the raw information collected into a structured, written Record of Processing Activities. This documentation is the end goal that demonstrates compliance (Article 30) and will be the reference point for audits, inspections, and compliance checks. How you document the information is important: it must be in writing (including electronic), well-organized, and readily available to produce to the ICO on request. A well-structured ROPA not only meets the letter of the law but also is usable for your organisation's needs.

**What to do:** Using the template from Step 4, enter the information for each processing activity. It's usually best to group or order the entries logically. Many organisations document by business function for controllers: e.g. have all HR-related processing activities listed together, then all Marketing, all Finance, etc. This approach makes the record easier to navigate.

**How to document effectively:** Use clear, simple language in descriptions so that anyone reading (including an ICO auditor) can understand. Avoid internal jargon or abbreviations, or if you use them, include a glossary. Fill in every applicable field for each entry. Ensure consistency in terminology across entries. After entering data, double-check a few entries with the stakeholders who provided the info to catch any misunderstandings.""",
                [
                    "Open your ROPA template (spreadsheet, document, or software system)",
                    "Organize entries logically by business function or department",
                    "For each processing activity, populate all required fields",
                    "Ensure data subjects and personal data categories are specific to each activity",
                    "Link lawful bases appropriately to each processing purpose",
                    "Use clear, jargon-free language that ICO auditors can understand",
                    "Mark 'N/A' for fields that truly don't apply (rather than leaving blank)",
                    "Ensure consistent terminology across entries (e.g., 'Contact details' vs 'Name and contact info')",
                    "Review sample entries with department stakeholders for accuracy",
                    "Ensure each entry has sufficient granularity (not too broad, not too narrow)",
                    "Split overly broad entries (e.g., 'HR management') into specific activities (recruitment, payroll, etc.)",
                    "Add identifying details on every page (company name, date, version number)",
                    "Compare completed ROPA with original activity list to ensure nothing is missing"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 7, "7",
                "Integrate ROPA with Your Wider Privacy Compliance Framework",
                """**Why this matters:** A ROPA is not an isolated checkbox – it's central to and interconnected with many other GDPR compliance tasks. Integrating it with your privacy notices, DPIAs, data sharing agreements, and transfer mechanisms ensures consistency and makes the ROPA a living hub of your privacy program. This integration demonstrates that privacy isn't just paperwork; it's embedded in your operations. Cross-referencing these elements in your ROPA will save time if the ICO asks questions, showing a comprehensive compliance story.

**What to do:** Connect the dots between your ROPA and other documents/processes:

**Privacy Notices:** Use your ROPA as a reference to ensure all purposes and data uses in your privacy notices are covered. There are many overlaps between what you document internally and what you must tell individuals in a privacy notice. Go through your ROPA line by line and check that each processing activity is reflected in the appropriate privacy notice.

**DPIAs:** Identify which processing activities in your ROPA required a DPIA or screening for high risk. For any ROPA entry that is likely high risk, ensure you have done a DPIA as required by Article 35. Record the DPIA's existence and link to it.

**Data Sharing Agreements & Processor Contracts:** For each external recipient or data processor listed in your ROPA, confirm a proper agreement is in place as required by GDPR. The ROPA can include a reference to the contract or DSA.

**International Transfers Documentation:** Where your ROPA lists transfers outside the UK, make sure you have the necessary transfer mechanism in place (e.g., UK adequacy, IDTA, or Art.49 exception).

**Appropriate Policy Documents (APDs):** If your organisation processes special category data under certain DPA 2018 Schedule 1 conditions, you must have an APD. Link these to your ROPA entries involving that data.""",
                [
                    "Cross-check ROPA against privacy notices – ensure all purposes are disclosed",
                    "Update privacy notices if any processing in ROPA is not mentioned",
                    "Add ROPA entries for any processing mentioned in privacy notices but not in ROPA",
                    "For each high-risk processing activity, confirm a DPIA exists or create one",
                    "Add DPIA references or links to relevant ROPA entries",
                    "For each processor/recipient, verify a contract or agreement is in place (Art. 28)",
                    "Add contract references (name, date signed, internal ID) to ROPA",
                    "For international transfers, confirm transfer mechanism exists (IDTA, adequacy, etc.)",
                    "Add transfer safeguard details to ROPA entries",
                    "For special category data, link to Appropriate Policy Document (APD)",
                    "Note the DPA 2018 condition being relied upon for each special category entry",
                    "For consent-based processing, link to consent records or systems",
                    "Add references to related documents in ROPA: DPIAs, contracts, APDs, privacy notices",
                    "Establish processes to keep ROPA and related documents in sync"
                ]
            ),

            self._create_step(
                project_id, PhaseType.BUILD_VALIDATE, 8, "8",
                "Leverage Templates and Tools for Efficiency",
                """**Why this matters:** Compiling and maintaining a ROPA can be complex, especially as your organisation grows or changes. The good news is you don't have to start from scratch – there are templates and software tools available to streamline the process. Using a well-crafted template ensures you don't overlook required information. And using dedicated privacy management tools or registries can make updating and reporting easier. A good system can reduce manual effort, minimize errors, and integrate ROPA upkeep into business-as-usual.

**What to do:** Decide on the format (e.g. spreadsheet vs database) and consider using existing templates or software.

**Regulator/Standards Templates:** The UK ICO provides basic ROPA templates – one for controllers and one for processors. These are typically Excel spreadsheets with predefined columns covering Article 30 requirements and some extra fields. Using such a template can jump-start your documentation.

**Spreadsheets:** Many SMEs simply use a spreadsheet (Excel, Google Sheets). This is perfectly acceptable under GDPR as long as it's in writing and available. Spreadsheets are easy to customize and use filters to sort by department or risk. The drawback is that as activities multiply, it can become unwieldy.

**Specialist Software / Privacy Management Tools:** For larger or more complex organisations, dedicated ROPA software or broader GRC tools can be very helpful. These tools provide a structured database for records of processing and often include workflows for assigning process owners, getting reminders for review, and generating reports. Solutions include OneTrust, TrustArc, Securiti, WireWheel, DPOrganizer, and others.""",
                [
                    "Download and review ICO's ROPA templates (controller and processor versions)",
                    "Evaluate if ICO template meets needs or if customization is required",
                    "Choose a platform: Spreadsheet (Excel/Google Sheets) vs Privacy management software",
                    "Consider organisation size, complexity, and budget when choosing tools",
                    "If using spreadsheet: Add custom columns as needed, set up filters, use data validation",
                    "If using software: Research options (OneTrust, TrustArc, Securiti, DPOrganizer, etc.)",
                    "Configure chosen system with all required and optional ROPA fields",
                    "Set up access controls – determine who can view, edit, and approve entries",
                    "Provide training to team members on how to use the chosen tool/template",
                    "Test the system: Can you easily search, filter, and export data?",
                    "Implement version control (file naming, version numbers, change tracking)",
                    "Set up backups and security for the ROPA (it contains sensitive metadata)",
                    "Document where the official 'master' ROPA is stored",
                    "Consider integration with other compliance tools (asset registers, DPIA tools, etc.)"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.BUILD_VALIDATE,
            name="Phase 3: Documentation & Integration",
            description="Document all activities in ROPA format, integrate with compliance framework, and set up tools",
            order=3,
            steps=steps
        )

    def _create_phase_4_maintenance(self, project_id: str) -> NEOMPhase:
        """Phase 4: Maintenance & Continuous Improvement (Step 9)"""

        steps = [
            self._create_step(
                project_id, PhaseType.DEPLOYMENT_MONITORING, 9, "9",
                "Maintain and Update the ROPA Regularly",
                """**Why this matters:** GDPR compliance is an ongoing obligation, and so your Record of Processing Activities must be kept up-to-date. Article 30 records are meant to reflect the current state of processing at any given time. If your organisation launches a new product, changes a data processor, or retires a system, your ROPA should be adjusted accordingly as soon as possible. Treat the ROPA as a "living document" that evolves with your business. This continuous maintenance is crucial for accountability – an outdated ROPA could mislead you or a regulator about your practices.

**What to do:** Establish a process for ongoing ROPA maintenance. This includes periodic reviews and event-triggered updates:

**Assign ownership for maintenance:** Ensure there is a designated person or team (often the DPO or data governance manager) responsible for the ROPA's upkeep. Maintain a list of "ROPA contacts" in each department who will inform you of changes.

**Periodic review cycle:** Decide how often you will formally review the entire ROPA. Many organisations do this annually or bi-annually. During a review, check if any new processes started, any listed process ceased, or if any details need updating.

**Change management integration:** Incorporate ROPA updates into project and change management workflows. For instance, if a new IT system involving personal data is introduced, add a step in that project's deployment checklist: "Update ROPA" or "Inform Privacy Officer to update ROPA."

**Monitor regulatory updates:** Keep an eye on any changes in the law or guidance that might affect ROPA requirements. Stay subscribed to ICO newsletters or participate in privacy forums.

**Audit and improvement:** Periodically audit the ROPA for compliance and effectiveness. Check a random sample of ROPA entries against actual practice to uncover issues.""",
                [
                    "Assign clear ownership for ROPA maintenance (DPO, Privacy Manager, etc.)",
                    "Nominate ROPA contacts in each department to report changes",
                    "Schedule regular ROPA reviews (annually or bi-annually at minimum)",
                    "During reviews: Check for new processes, ceased processes, or updated details",
                    "Integrate ROPA updates into change management workflows",
                    "Add 'Update ROPA' as a checkpoint in new system deployment checklists",
                    "Create process for departments to notify privacy team of data processing changes",
                    "Update ROPA whenever: New processing starts, Purpose changes, New recipient added",
                    "Update when: Retention period changes, Processor changes, International transfer added",
                    "Maintain a change log or version history of ROPA updates",
                    "Monitor ICO and regulatory updates for changes to ROPA requirements",
                    "Conduct periodic audits: Verify random ROPA entries against actual practice",
                    "Test ROPA readiness: Simulate ICO request and ensure you can produce records quickly",
                    "For retired processes: Mark as 'Ceased' with end date rather than deleting",
                    "Provide refresher training to staff on when to report processing changes",
                    "Review ROPA in compliance meetings or board reports regularly",
                    "Keep backups of ROPA and protect it appropriately (it contains sensitive information)",
                    "Ensure ROPA reflects reality at all times – not just a historical snapshot"
                ]
            ),
        ]

        return NEOMPhase(
            id=str(uuid.uuid4()),
            project_id=project_id,
            phase_type=PhaseType.DEPLOYMENT_MONITORING,
            name="Phase 4: Maintenance & Continuous Improvement",
            description="Establish processes for keeping the ROPA up-to-date and continuously improving compliance",
            order=4,
            steps=steps
        )
