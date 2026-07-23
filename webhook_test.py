import requests
import os
from dotenv import load_dotenv

load_dotenv()
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

data = {"content": "🚀 Webhook connection test successful!"}
response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("✅ Webhook sent successfully!")
else:
    print(f"❌ Failed to send webhook. Status code: {response.status_code}")
