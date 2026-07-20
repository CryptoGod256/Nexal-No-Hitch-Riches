import os
from dotenv import load_dotenv

# Initialize vault
load_dotenv()

def get_key(service):
    """Securely pulls keys from .env without manual entry."""
    key = os.getenv(f"{service.upper()}_API_KEY")
    if not key:
        print(f"[!] CRITICAL: Vault empty for {service}")
    return key
