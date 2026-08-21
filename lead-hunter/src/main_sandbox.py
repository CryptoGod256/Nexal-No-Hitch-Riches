import random, logging, os
from datetime import datetime
from pathlib import Path

Path('logs').mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[logging.FileHandler('logs/system.log'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

def test():
    logger.info("\n🚀 LEAD HUNTER V1 - TERMUX SANDBOX\n")
    hooks = ["I noticed your MLS only has 3 listings vs competitors with 15+", "Your Google reviews are at 2.3 stars with no recent activity", "You haven't run Google Ads in 60 days"]
    bridges = ["We automate listing syndication to 50+ sites", "We automate review requests 24/7", "We run targeted Google Ads automatically"]
    ctas = ["Want a 5-minute walkthrough?", "Free demo to see it in action?", "Quick call to explore potential?"]
    
    for i in range(3):
        logger.info(f"\n{'='*60}")
        logger.info(f"Pitch #{i+1}")
        logger.info('='*60)
        logger.info(f"PAIN: {random.choice(['listing_gap', 'review_gap', 'ad_inactivity'])} (Score: 85/100)")
        logger.info(f"HOOK: {random.choice(hooks)}")
        logger.info(f"BRIDGE: {random.choice(bridges)}")
        logger.info(f"CTA: {random.choice(ctas)}")
        logger.info(f"✅ Pitch generated")
    
    logger.info(f"\n{'='*60}")
    logger.info("✅ TEST COMPLETE - 3 pitches generated")
    logger.info(f"{'='*60}\n")

if __name__ == "__main__":
    test()
