from google_auth_oauthlib.flow import InstalledAppFlow
import os

# Define the scope (Read-only access to Gmail for now)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    
    # This triggers the authentication flow
    creds = flow.run_local_server(port=0, open_browser=False)
    
    # Save the token for the next time so you don't have to re-login
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    
    print("Authentication successful! token.json has been created.")

if __name__ == '__main__':
    main()
