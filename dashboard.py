import streamlit as st
import json
import os
from database import SessionLocal, LeadLog, init_db
import datetime

init_db()

st.set_page_config(page_title="Nexal Intelligence Dashboard", layout="wide")

st.title("⚡ Nexal Intelligence Control Center")
st.sidebar.header("Agent Configuration")

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

st.sidebar.text(f"Business: {config.get('business_name')}")
st.sidebar.text(f"Tone: {config.get('tone')}")

st.header("Generate Live Sales Pitch")
prospect_name = st.text_input("Prospect Name")
industry = st.text_input("Prospect Industry")

if st.button("Generate & Save Pitch"):
    if prospect_name and industry:
        services = ", ".join(config.get("services", ["AI Solutions"]))
        goal = config.get("conversion_goal", "Retainer Onboarding")
        
        pitch = (
            f"Hello {prospect_name}, we at {config.get('business_name')} recognize your work in {industry}. "
            f"We specialize in {services}. Our goal is to achieve: {goal}."
        )
        
        db = SessionLocal()
        db_log = LeadLog(prospect_name=prospect_name, industry=industry, generated_pitch=pitch)
        db.add(db_log)
        db.commit()
        db.close()
        
        st.success("Pitch generated and logged successfully!")
        st.write(pitch)
    else:
        st.warning("Please fill out both fields.")

st.divider()
st.subheader("📊 Recent Lead Interactions")
db = SessionLocal()
logs = db.query(LeadLog).order_by(LeadLog.timestamp.desc()).all()
db.close()

if logs:
    for log in logs:
        st.markdown(f"**{log.prospect_name}** ({log.industry}) - _{log.timestamp}_")
        st.code(log.generated_pitch)
else:
    st.info("No logs found yet.")

# --- Phase 3: Dashboard Refinement Metrics ---
st.sidebar.divider()
st.sidebar.subheader("📊 System Metrics")
db_metrics = SessionLocal()
total_leads = db_metrics.query(LeadLog).count()
db_metrics.close()
st.sidebar.metric(label="Total Leads Logged", value=total_leads)
