import os
import json

class ReverseProxyGenerator:
    def __init__(self):
        self.settings_path = "automation/dns/domain_settings.json"
        self.caddyfile_path = "automation/dns/Caddyfile"
        
    def generate_config(self):
        if not os.path.exists(self.settings_path):
            print("[ERROR] Domain settings not found. Run domain registration first.")
            return
            
        with open(self.settings_path, 'r') as f:
            data = json.load(f)
            
        domain = data.get("domain", "nexal-intelligence.cloud")
        
        caddy_config = f"""
{domain} {{
    # Reverse proxy secure edge traffic to FastAPI core backend
    reverse_proxy localhost:8000
    
    log {{
        output file automation/dns/caddy_access.log
    }}
}}
"""
        with open(self.caddyfile_path, 'w') as f:
            f.write(caddy_config.strip() + "\n")
            
        print(f"[REVERSE PROXY] Caddy configuration generated for '{domain}' pointing to localhost:8000.")
        print(f"[SSL] Automatic TLS provisioning template locked and secured.")

if __name__ == "__main__":
    generator = ReverseProxyGenerator()
    generator.generate_config()
