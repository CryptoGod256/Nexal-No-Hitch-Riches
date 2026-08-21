from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI(title="Nexal Intelligence API", version="1.0")

CONFIG_PATH = "config.json"
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
else:
    config = {
        "business_name": "Nexal Intelligence",
        "identity": "Nexal Agent",
        "tone": "professional",
        "services": ["AI Solutions"],
        "conversion_goal": "Retainer Onboarding"
    }

class ProspectRequest(BaseModel):
    prospect_name: str
    industry: str

@app.post("/generate-pitch")
def generate_pitch(prospect: ProspectRequest):
    business_name = config.get("business_name", "Nexal Intelligence")
    services = ", ".join(config.get("services", ["AI Solutions"]))
    goal = config.get("conversion_goal", "Partnership")
    
    pitch = (
        f"Hello {prospect.prospect_name}, we at {business_name} notice your growth in the {prospect.industry} sector. "
        f"We specialize in {services}. Our mission is to achieve: {goal}."
    )
    
    return {
        "status": "success",
        "prospect": prospect.prospect_name,
        "pitch": pitch
    }

class WebhookEvent(BaseModel):
    event_type: str
    payload: dict

@app.post("/webhook")
async def handle_webhook(event: WebhookEvent):
    # Live listener entry point for incoming chat or lead events
    return {
        "status": "received",
        "event_type": event.event_type,
        "message": "Event successfully logged and queued for processing."
    }

from database import SessionLocal, LeadLog

@app.post("/webhook-persist")
async def persist_webhook(event: WebhookEvent):
    db = SessionLocal()
    try:
        # Extract payload data or default values
        p_name = event.payload.get("prospect_name", "Unknown")
        ind = event.payload.get("industry", "General")
        pitch_text = event.payload.get("pitch", "Automated webhook event log")
        
        db_lead = LeadLog(
            prospect_name=p_name,
            industry=ind,
            generated_pitch=pitch_text
        )
        db.add(db_lead)
        db.commit()
        db.refresh(db_lead)
        
        return {
            "status": "success",
            "lead_id": db_lead.id,
            "message": "Webhook event successfully persisted to database."
        }
    except Exception as e:
        db.rollback()
        return {"status": "error", "detail": str(e)}
    finally:
        db.close()

# --- Nexus Master Orchestrator Integration ---
try:
    from nexus_hub.nexus import router as nexus_router
    app.include_router(nexus_router)
    print("Nexus Master Orchestrator successfully mounted.")
except Exception as e:
    print(f"Nexus mount warning: {e}")
