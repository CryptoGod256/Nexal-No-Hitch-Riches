import os
import json
from dotenv import load_dotenv

# Load security keys from the .env file
load_dotenv()

class AutomationBrain:
    def __init__(self, client_id):
        self.client_id = client_id
        # We will create this config file in the next step
        self.config = self.load_config()

    def load_config(self):
        """Loads specific client instructions from the /clients folder"""
        with open(f"clients/{self.client_id}/config.json", 'r') as f:
            return json.load(f)

    def classify_intent(self, message):
        """Brain A: Fast/Cheap Router"""
        print(f"[Brain A] Routing message for {self.client_id}...")
        return "lead" 

    def generate_response(self, message, intent):
        """Brain B: High-Quality Responder"""
        print(f"[Brain B] Generating response for {intent}...")
        return f"Response based on {self.config['business_name']} style."

def main():
    client_id = "hvac_pro_01" 
    incoming_text = "Do you have availability next Tuesday?"
    
    # Check if config exists before running
    if os.path.exists(f"clients/{client_id}/config.json"):
        brain = AutomationBrain(client_id)
        intent = brain.classify_intent(incoming_text)
        
        if intent == "lead":
            response = brain.generate_response(incoming_text, intent)
            print(f"Action: Send SMS -> {response}")
    else:
        print(f"Error: Configuration for {client_id} not found. Please setup the client folder.")

if __name__ == "__main__":
    main()
