import os
import base64
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class GmailClient:
    def __init__(self, token_path='token.json'):
        self.token_path = token_path
        self.service = self._build_service()

    def _build_service(self):
        creds = Credentials.from_authorized_user_file(self.token_path)
        return build('gmail', 'v1', credentials=creds)

    def send_email(self, to, subject, body):
        try:
            message = EmailMessage()
            message.set_content(body)
            message['To'] = to
            message['Subject'] = subject
            
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            create_message = {'raw': raw_message}
            
            sent_message = self.service.users().messages().send(userId="me", body=create_message).execute()
            print(f"✅ Professional email sent to {to}")
            return sent_message
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return None

    def get_recent_emails(self, max_results=5):
        try:
            results = self.service.users().messages().list(userId='me', maxResults=max_results).execute()
            messages = results.get('messages', [])
            return messages
        except Exception as e:
            print(f"❌ Error fetching emails: {e}")
            return []
