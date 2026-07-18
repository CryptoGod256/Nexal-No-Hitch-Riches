import json

def generate_pitch():
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    pitch = f"""
    --- Nexal Intelligence Sales Pitch ---
    Identity: {config['identity']}
    Tone: {config['tone']}
    
    'We are {config['business_name']}. We specialize in {', '.join(config['services'])}.
    Our mission is to achieve: {config['conversion_goal']}. 
    We invite you to participate in our decentralized ecosystem.'
    --------------------------------------
    """
    return pitch

if __name__ == "__main__":
    print(generate_pitch())
