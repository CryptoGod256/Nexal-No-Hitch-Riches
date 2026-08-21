from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import SessionLocal, LeadLog

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r") as f:
        return f.read()

@app.get("/api/leads")
def get_leads(db: Session = Depends(get_db)):
    leads = db.query(LeadLog).all()
    return {"status": "success", "count": len(leads), "leads": leads}

