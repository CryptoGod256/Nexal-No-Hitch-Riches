# [Your Business Name] - AI Automation Engine

The central repository for high-speed B2B lead response automation. This system is designed for reliability, scalability, and instant client deployment.

## 🚀 Business Mission
Providing 24/7, ultra-fast lead qualification to help [Niche, e.g., HVAC/Real Estate] businesses capture leads within seconds, increasing conversion rates and reducing operational lag.

## 🛠 Tech Stack
* **Gateway:** Android SMS Gateway (Private infrastructure)
* **Brain:** Router-Worker pattern (GPT-4o-mini + Claude 3.5 Sonnet)
* **Database:** Local SQLite (High-speed, zero external cost)
* **Environment:** Python / FastAPI / Termux (Dev) & Linux VPS (Prod)

## 📁 Repository Structure
- `/core`: Shared automation logic & SMS handlers.
- `/clients`: Per-client configurations (Each client gets a dedicated folder).
- `main.py`: The production entry point.
- `.env`: Sensitive API keys (Do NOT commit).

## 📋 Client Onboarding SOP
1. **Clone Repo:** Ensure latest stable build.
2. **Create Client Config:** `mkdir clients/client_name`.
3. **Configure Settings:** Populate `clients/client_name/config.json` with business persona and qualification criteria.
4. **Deploy:** Restart production service on VPS via Termius.

## 🛡 Security & Maintenance
- **API Keys:** Never store in code. Use `.env` file loaded at runtime.
- **Data Privacy:** Local storage ensures client data does not pass through unnecessary third-party connectors.
- **Monitoring:** Check `/logs/` for uptime verification.
- 
