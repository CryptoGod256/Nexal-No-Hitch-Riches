import logging
import os
from database import init_db, log_lead
from scanner import run_scan

# Ensure log directory exists
os.makedirs('../../logs', exist_ok=True)

# Configure Logging
logging.basicConfig(
    filename='../../logs/nexal_engine.log',
    level=logging.INFO,
    format='%(asctime)s - Nexal_Engine - %(levelname)s - %(message)s'
)

def start_engine():
    logging.info("Nexal Engine: Initializing secure scan.")
    try:
        init_db()
        leads = run_scan()
        for lead in leads:
            log_lead(lead['name'], 'New', lead['potential'])
            logging.info(f"Successfully logged lead: {lead['name']}")
        logging.info("Orchestration Complete.")
    except Exception as e:
        logging.error(f"Critical Engine Failure: {e}")

if __name__ == "__main__":
    start_engine()
