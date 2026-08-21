import requests
from bs4 import BeautifulSoup

def find_prospect_email(url):
    """Simple scraper to find contact info on a webpage."""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Logic to find email patterns
        text = soup.get_text()
        # Very basic regex search for emails
        import re
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        return emails[0] if emails else "No email found"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Example usage: Scrape a business site
    target_site = "https://example-business.com"
    print(f"[*] Scraper: Extracting data from {target_site}...")
    email = find_prospect_email(target_site)
    print(f"[!] Contact Found: {email}")
