# Nexal Command Interface
# This module captures the Commander's directives.

def capture_command():
    try:
        command = input("Nexal Command > ")
        print(f"Acknowledged: Executing '{command}'...")
        # Future logic: Route to respective AI Operator (Claude/Gemini)
        return command
    except KeyboardInterrupt:
        print("\nSystem standby.")
        exit()

if __name__ == "__main__":
    capture_command()
