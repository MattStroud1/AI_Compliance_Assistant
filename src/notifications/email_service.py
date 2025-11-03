"""Email notification service for NEOM Trustworthy AI"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional
from datetime import datetime
from dotenv import load_dotenv

from src.models import PitstopCheckpoint, NEOMProject, PhaseType

load_dotenv()


class EmailService:
    """Send email notifications for pitstops and compliance events"""

    def __init__(self):
        """Initialize email service with configuration from environment"""
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_username = os.getenv("SMTP_USERNAME", "")
        self.smtp_password = os.getenv("SMTP_PASSWORD", "")
        self.from_email = os.getenv("FROM_EMAIL", self.smtp_username)
        self.enabled = os.getenv("EMAIL_ENABLED", "false").lower() == "true"

    def send_email(
        self,
        to_emails: List[str],
        subject: str,
        body_html: str,
        body_text: Optional[str] = None
    ) -> bool:
        """
        Send an email

        Args:
            to_emails: List of recipient email addresses
            subject: Email subject
            body_html: HTML email body
            body_text: Plain text alternative (optional)

        Returns:
            True if sent successfully, False otherwise
        """
        if not self.enabled:
            print(f"📧 Email disabled. Would send to {to_emails}: {subject}")
            return False

        if not self.smtp_username or not self.smtp_password:
            print("❌ Email credentials not configured")
            return False

        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.from_email
            msg['To'] = ', '.join(to_emails)

            # Add text and HTML parts
            if body_text:
                msg.attach(MIMEText(body_text, 'plain'))
            msg.attach(MIMEText(body_html, 'html'))

            # Send via SMTP
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)

            print(f"✅ Email sent to {to_emails}: {subject}")
            return True

        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False

    def send_pitstop_notification(
        self,
        project: NEOMProject,
        pitstop: PitstopCheckpoint
    ) -> bool:
        """
        Send notification for upcoming pitstop meeting

        Args:
            project: NEOM project
            pitstop: Pitstop checkpoint

        Returns:
            True if sent successfully
        """
        # Determine phase name
        phase_names = {
            PhaseType.PLANNING_DESIGN: "Planning & Design",
            PhaseType.DATA_PREPARATION: "Data Preparation",
            PhaseType.BUILD_VALIDATE: "Build & Validate",
            PhaseType.DEPLOYMENT_MONITORING: "Deployment & Monitoring"
        }

        phase_name = phase_names.get(pitstop.phase_completed, "Unknown Phase")

        # Build recipient list
        recipients = []
        if pitstop.pdpo_reviewer:
            recipients.append(pitstop.pdpo_reviewer)
        recipients.extend(pitstop.participants)

        # Build email
        subject = f"🎯 Pitstop Meeting: {project.project_name} - {phase_name} Complete"

        html_body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                .header {{ background-color: #1f77b4; color: white; padding: 20px; }}
                .content {{ padding: 20px; }}
                .info-box {{ background-color: #f0f0f0; padding: 15px; margin: 10px 0; border-left: 4px solid #1f77b4; }}
                .button {{ background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; display: inline-block; margin: 10px 0; }}
                ul {{ margin-left: 20px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🎯 Pitstop Meeting Notification</h1>
            </div>

            <div class="content">
                <h2>Project: {project.project_name}</h2>

                <div class="info-box">
                    <h3>Phase Completed</h3>
                    <p><strong>{phase_name}</strong></p>
                    <p>Status: Ready for review</p>
                </div>

                <h3>Meeting Details</h3>
                <ul>
                    <li><strong>AI System:</strong> {project.ai_system_name}</li>
                    <li><strong>Purpose:</strong> {project.ai_system_purpose}</li>
                    <li><strong>Risk Level:</strong> {project.risk_level.value if project.risk_level else 'Not yet assessed'}</li>
                    <li><strong>PDPO Reviewer:</strong> {pitstop.pdpo_reviewer or 'To be assigned'}</li>
                </ul>

                <h3>What to Review</h3>
                <p>This pitstop meeting will review the {phase_name} phase, including:</p>
                <ul>
                    <li>Evidence collected during this phase</li>
                    <li>Compliance documentation</li>
                    <li>Outstanding issues or concerns</li>
                    <li>Readiness to proceed to next phase</li>
                </ul>

                <h3>Next Steps</h3>
                <ol>
                    <li>Review the evidence and documentation in the compliance tool</li>
                    <li>Prepare any questions or concerns</li>
                    <li>Attend the pitstop meeting</li>
                    <li>Provide sign-off to proceed (or identify remediation actions)</li>
                </ol>

                <p><em>This is an automated notification from the NEOM AI Compliance Assistant.</em></p>
            </div>
        </body>
        </html>
        """

        text_body = f"""
        Pitstop Meeting Notification

        Project: {project.project_name}
        Phase Completed: {phase_name}

        AI System: {project.ai_system_name}
        Purpose: {project.ai_system_purpose}

        This pitstop meeting will review the evidence and documentation from the {phase_name} phase.
        Please review all materials before the meeting and prepare any questions.

        ---
        NEOM AI Compliance Assistant
        """

        return self.send_email(recipients, subject, html_body, text_body)

    def send_pitstop_reminder(
        self,
        project: NEOMProject,
        pitstop: PitstopCheckpoint
    ) -> bool:
        """
        Send reminder for scheduled pitstop

        Args:
            project: NEOM project
            pitstop: Pitstop checkpoint

        Returns:
            True if sent successfully
        """
        recipients = []
        if pitstop.pdpo_reviewer:
            recipients.append(pitstop.pdpo_reviewer)
        recipients.extend(pitstop.participants)

        subject = f"⏰ Reminder: Pitstop Meeting for {project.project_name}"

        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <h2>⏰ Pitstop Meeting Reminder</h2>
            <p>This is a reminder about the upcoming pitstop meeting for:</p>
            <p><strong>Project:</strong> {project.project_name}</p>
            <p><strong>Scheduled:</strong> {pitstop.scheduled_date.strftime('%Y-%m-%d %H:%M') if pitstop.scheduled_date else 'Not yet scheduled'}</p>
            <p>Please ensure you have reviewed all evidence and are prepared for the meeting.</p>
        </body>
        </html>
        """

        return self.send_email(recipients, subject, html_body)

    def send_approval_notification(
        self,
        project: NEOMProject,
        pitstop: PitstopCheckpoint
    ) -> bool:
        """
        Send notification that pitstop was approved

        Args:
            project: NEOM project
            pitstop: Approved pitstop checkpoint

        Returns:
            True if sent successfully
        """
        phase_names = {
            PhaseType.PLANNING_DESIGN: "Planning & Design",
            PhaseType.DATA_PREPARATION: "Data Preparation",
            PhaseType.BUILD_VALIDATE: "Build & Validate",
            PhaseType.DEPLOYMENT_MONITORING: "Deployment & Monitoring"
        }

        phase_name = phase_names.get(pitstop.phase_completed, "Unknown Phase")

        recipients = []
        if project.project_lead:
            recipients.append(project.project_lead)
        recipients.extend(pitstop.participants)

        subject = f"✅ Approved: {project.project_name} - {phase_name}"

        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <div style="background-color: #4CAF50; color: white; padding: 20px;">
                <h1>✅ Pitstop Approved</h1>
            </div>
            <div style="padding: 20px;">
                <h2>{project.project_name}</h2>
                <p>The <strong>{phase_name}</strong> phase has been reviewed and approved.</p>

                <h3>Approval Details</h3>
                <ul>
                    <li><strong>Approved by:</strong> {pitstop.approved_by}</li>
                    <li><strong>Approved at:</strong> {pitstop.approved_at.strftime('%Y-%m-%d %H:%M') if pitstop.approved_at else 'N/A'}</li>
                </ul>

                {f"<p><strong>Notes:</strong> {pitstop.approval_notes}</p>" if pitstop.approval_notes else ""}

                {f"<h3>Action Items</h3><ul>{''.join(f'<li>{item}</li>' for item in pitstop.action_items)}</ul>" if pitstop.action_items else ""}

                <p><strong>You may now proceed to the next phase.</strong></p>
            </div>
        </body>
        </html>
        """

        return self.send_email(recipients, subject, html_body)

    def send_issues_notification(
        self,
        project: NEOMProject,
        pitstop: PitstopCheckpoint
    ) -> bool:
        """
        Send notification that issues were raised during pitstop

        Args:
            project: NEOM project
            pitstop: Pitstop with issues

        Returns:
            True if sent successfully
        """
        recipients = []
        if project.project_lead:
            recipients.append(project.project_lead)
        recipients.extend(pitstop.participants)

        subject = f"⚠️ Issues Raised: {project.project_name}"

        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif;">
            <div style="background-color: #ff9800; color: white; padding: 20px;">
                <h1>⚠️ Issues Raised</h1>
            </div>
            <div style="padding: 20px;">
                <h2>{project.project_name}</h2>
                <p>Issues were identified during the pitstop review that require attention.</p>

                <h3>Issues</h3>
                <ul>
                    {''.join(f'<li>{issue}</li>' for issue in pitstop.issues_raised)}
                </ul>

                <h3>Required Actions</h3>
                <ul>
                    {''.join(f'<li>{action}</li>' for action in pitstop.action_items)}
                </ul>

                <p><strong>Please address these issues before proceeding to the next phase.</strong></p>
            </div>
        </body>
        </html>
        """

        return self.send_email(recipients, subject, html_body)
