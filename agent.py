import json

def generate_pitch():
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    pitch = f"""
    --- Nexal Intelligence Sales Pitch ---
    Identity: {config.get('identity', 'Nexal Agent')}
    Tone: {config.get('tone', 'professional')}
    
    'We are {config.get('business_name', 'Nexal Intelligence')}. We specialize in {', '.join(config.get('services', ['AI Solutions']))}.
    Our mission is to achieve: {config.get('conversion_goal', 'Partnership')}. 
    We invite you to participate in our decentralized ecosystem.'
    --------------------------------------
    """
    return pitch

if __name__ == "__main__":
    print(generate_pitch())
