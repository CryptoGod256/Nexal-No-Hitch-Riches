import openai
import vault

# Initialize Client
client = openai.OpenAI(api_key=vault.get_key("openai"))

def scan_niche(niche_topic):
    """Generates a B2B retainer opportunity analysis."""
    print(f"[*] NEXAL Scanner: Analyzing {niche_topic}...")
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a NEXAL Intelligence Analyst. Output a concise B2B retainer opportunity analysis for the given niche."},
            {"role": "user", "content": f"Find a high-profit automation gap for: {niche_topic}"}
        ]
    )
    
    result = response.choices[0].message.content
    print(f"\n--- NEXAL REPORT ---\n{result}\n--------------------\n")
    return result

if __name__ == "__main__":
    scan_niche("Real Estate Lead Generation")
