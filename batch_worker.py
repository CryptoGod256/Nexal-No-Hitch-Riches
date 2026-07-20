import scanner
import strategist
import time

# NEXAL BATCH WORKER // HIGH-FREQUENCY GROWTH
niches = ["Real Estate", "SaaS", "E-commerce", "Local Solar", "Digital Agencies"]

def run_nexal_empire():
    print("--- NEXAL EMPIRE: INITIATING AUTONOMOUS CYCLE ---")
    for niche in niches:
        print(f"[+] Targeting: {niche}")
        
        # 1. Recursive Scan
        data = scanner.scan_niche(niche)
        
        # 2. Dynamic Strategy (Generating 2 pitches)
        pitch_a = strategist.draft_proposal(data)
        
        # 3. Store for CEO Review
        with open('data/pending_deals.txt', 'a') as f:
            f.write(f"\n--- {niche} ---\n{pitch_a}\n")
            
        time.sleep(2) # Prevent API rate limits
    print("--- NEXAL EMPIRE: CYCLE COMPLETE. STANDING BY. ---")

if __name__ == "__main__":
    run_nexal_empire()
