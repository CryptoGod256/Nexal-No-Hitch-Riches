import json
import urllib.request
import logging

def run_scan():
    try:
        with open('../../config.json', 'r') as f:
            config = json.load(f)
        
        req = urllib.request.Request(config['api_endpoint'], headers={'User-Agent': 'Nexal-Intelligence-Engine'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
        return data
    except Exception as e:
        logging.error(f"Scanner Failure: {e}")
        return []
