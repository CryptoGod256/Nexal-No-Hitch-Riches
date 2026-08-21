import json

def update_learning_log(niche, result):
    """Records if a pitch worked or failed to optimize future outputs."""
    log = {"niche": niche, "result": result}
    
    # Append to our "Lessons Learned" database
    with open('data/learning_log.json', 'a') as f:
        json.dump(log, f)
        f.write('\n')
        
    if result == "FAIL":
        print("[!] NEXAL Optimizer: Analyzing failure pattern to improve strategy...")
        # (This is where the AI will later ingest these logs to evolve)
