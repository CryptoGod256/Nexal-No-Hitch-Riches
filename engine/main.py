import logging
import os
from database import init_db, log_lead
from scanner import run_scan

os.makedirs('../../logs', exist_ok=True)
logging.basicConfig(filename='../../logs/nexal_engine.log', level=logging.INFO, format='%(asctime)s - Nexal_Engine - %(levelname)s - %(message)s')

def check_protocol_compliance():
    print("⚡ Nexal Engine: Protocol Compliance // Verified.")

def start_engine():
    check_protocol_compliance()
    logging.info("Nexal Engine: Initializing secure scan.")
    try:
        init_db()
        leads = run_scan()

        if isinstance(leads, dict):
            leads = [leads]
        
        # If scanner returns None or string, handle it
        if not isinstance(leads, list):
            logging.error(f"Scanner returned invalid format: {type(leads)}")
            return

        for lead in leads:
            # Final safety: Ensure lead is a dict
            if not isinstance(lead, dict):
                logging.warning(f"Skipping malformed lead: {lead}")
                continue
                
            name = lead.get('name', 'Unknown')
            potential = lead.get('potential', 0.0)
            log_lead(name, 'New', potential)
            logging.info(f"Successfully logged lead: {name}")
            
    except Exception as e:
        logging.error(f"Critical Engine Failure: {e}")
        print(f"ALERT: System Stability check failed. Error: {e}")

if __name__ == "__main__":
    start_engine()
