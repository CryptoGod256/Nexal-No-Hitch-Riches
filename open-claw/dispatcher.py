import urllib.request
import json
import time

def dispatch_payload(data):
    url = "http://localhost:3000/api/v1/webhook"
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            print(f"✅ OpenClaw Payload Dispatched: {response.read().decode('utf-8')}")
    except Exception as e:
        print(f"⚠️ OpenClaw Dispatch Error: {e}")

if __name__ == "__main__":
    test_data = {"source": "OpenClaw", "event": "DATA_ACQUIRED", "timestamp": time.time()}
    dispatch_payload(test_data)
