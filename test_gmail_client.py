from gmail_client import GmailClient
client = GmailClient()
print("Fetching recent emails...")
print(client.get_recent_emails())
