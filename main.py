from fastapi import FastAPI, Request, HTTPException
from billing_controller import record_successful_payment

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Nexal Intelligence Core Online", "system": "Active"}

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.json()
    event_type = payload.get("type")
    
    # Handle simulated or live checkout session completion
    if event_type == "checkout.session.completed" or payload.get("simulation") == True:
        data = payload.get("data", {}).get("object", {})
        company_name = payload.get("company_name") or data.get("metadata", {}).get("company_name", "Apex Autonomous Corp")
        contact_email = payload.get("contact_email") or data.get("customer_email", "billing@apexautonomous.io")
        retainer_value = payload.get("retainer_value") or (data.get("amount_total", 150000) / 100.0)
        
        record_successful_payment(company_name, contact_email, float(retainer_value))
        return {"status": "success", "node_locked": company_name}
        
    return {"status": "received", "event": event_type}
