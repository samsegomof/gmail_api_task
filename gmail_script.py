import os
import base64

from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.compose",
          "https://mail.google.com/",
          "https://www.googleapis.com/auth/gmail.readonly"]


class GmailClient:
    """A class for interacting with Gmail API."""

    def __init__(self):
        """Initialize GmailClient object."""
        self.service = self._authenticate()

    def _authenticate(self):
        """Authenticate with Gmail API."""
        creds = None

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            # Call the Gmail API
            return build("gmail", "v1", credentials=creds)
        except Exception as e:
            print(f"Error occurred during authentication: {e}")

    def get_last_emails(self, max_results=5):
        """Get information about the last specified number of messages from inbox.

        Args:
            max_results (int): The maximum number of messages of retrieve. Default is 5.
        """
        if not self.service:
            print("Service object is not initialized.")
            return

        results = self.service.users().messages().list(userId='me', labelIds=['INBOX'],
                                                       maxResults=max_results).execute()
        messages = results.get('messages', [])
        for message in messages:
            msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg['payload']['headers']
            subject = next(item['value'] for item in headers if item['name'] == 'Subject')
            sender = next(item['value'] for item in headers if item['name'] == 'From')
            timestamp = int(msg['internalDate'])
            timestamp_seconds = timestamp / 1000.0
            timestamp_datetime = datetime.fromtimestamp(timestamp_seconds)
            print(f"Subject: {subject}, From: {sender}, Timestamp: {timestamp_datetime}")

    def send_email(self, sender, to, subject, message_text):
        """Send an email.

        Args:
            sender (str): The sender's email address.
            to (str): The recipient's email address.
            subject (str): The subject of the email.
            message_text (str): The body of the email.
        """
        message = self._create_message(sender, to, subject, message_text)
        self._send_message('me', message)

    def _create_message(self, sender, to, subject, message_text):
        """Create a message.

        Args:
            sender (str): The sender's email address.
            to (str): The recipient's email address.
            subject (str): The subject of the email.
            message_text (str): The body of the email.

        Returns:
            dict: The formatted email message.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def _send_message(self, user_id, message):
        """Send a message.

        Args:
            user_id (str): The user's email address.
            message (dict): The formatted email message.
        """
        try:
            message = self.service.users().messages().send(userId=user_id, body=message).execute()
            print('Message with Id: %s' % message['id'], 'successfully sent.')
            return message
        except Exception as e:
            print('An error occurred: %s' % e)

    def delete_email(self, message_id):
        """
        Delete an email.

        Args:
            message_id (str): The ID of the message to delete.
        """
        try:
            self.service.users().messages().delete(userId='me', id=message_id).execute()
            print(f"Message with id {message_id} deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting message {message_id}: {e}")


if __name__ == "__main__":
    gmail_client = GmailClient()

    print("Last 5 emails:")
    gmail_client.get_last_emails()

    # to test the message sending method, fill in
    gmail_client.send_email('your_email@example.com', 'recipients_email@example.com', 'subject text', 'message_text')

    gmail_client.delete_email('put here message id')
