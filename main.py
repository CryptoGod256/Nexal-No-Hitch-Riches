import os
from dotenv import load_dotenv
from input_handler import capture_command

# Initialize the Nexal Environment
load_dotenv()

def start_engine():
    print("--- Nexal Automation Engine Online ---")
    print("System status: Operational")
    print("Loading AI Operators...")
    print("Ready to execute tasks.")
    
    # Enable Interactive Mode
    while True:
        command = capture_command()
        if command.lower() in ["exit", "standby"]:
            print("System entering standby. Awaiting Commander...")
            break
        # Logic to route commands will be added here
        print(f"Routing '{command}' to the relevant AI Operator...")

if __name__ == "__main__":
    start_engine()
