import json
import logging

def run_scan():
    try:
        # Hardcoded mock data for stability test
        # Replace this with your API logic once confirmed working
        data = [
            {"name": "Alpha-Entity-01", "potential": 5000.0},
            {"name": "Beta-Entity-02", "potential": 8500.0}
        ]
        return data
    except Exception as e:
        logging.error(f"Scanner Failure: {e}")
        return []

