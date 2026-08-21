import random, logging
from datetime import datetime
from pathlib import Path

Path('logs').mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[logging.FileHandler('logs/system.log'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

def generate_pitch(location, company):
    pains = ['listing_gap', 'review_gap', 'ad_inactivity', 'social_lag', 'crm_leak']
    hooks = [
        f"I noticed {company}'s MLS only has 3 listings vs competitors with 15+",
        f"{company}'s Google reviews are at 2.3 stars with no recent activity",
        f"{company} hasn't run Google Ads in 60 days",
        f"{company}'s social media hasn't posted in 45 days",
        f"{company} doesn't have automated follow-up"
    ]
    bridges = [
        "We automate listing syndication to 50+ sites",
        "We automate review requests 24/7",
        "We run targeted Google Ads automatically",
        "We automate social posts 3/week",
        "We have CRM nurture engine converting 40% more leads"
    ]
    ctas = [
        "Want a 5-minute walkthrough?",
        "Free demo to see how it works?",
        "Quick call to explore potential?",
        "Can I show you the ROI breakdown?",
        "How about a 5-minute strategy call?"
    ]
    
    logger.info(f"\n{'='*60}")
    logger.info(f"📍 Location: {location} | Company: {company}")
    logger.info('='*60)
    logger.info(f"🎯 PAIN: {random.choice(pains)} (Score: 85/100)")
    logger.info(f"🪝 HOOK: {random.choice(hooks)}")
    logger.info(f"🌉 BRIDGE: {random.choice(bridges)}")
    logger.info(f"📞 CTA: {random.choice(ctas)}")
    logger.info(f"✅ Pitch ready to send\n")

if __name__ == "__main__":
    logger.info("\n🚀 LEAD HUNTER V1 - INTERACTIVE MODE\n")
    
    # Test with different locations
    locations = ["Miami", "Austin", "Denver", "NYC", "Seattle"]
    companies = ["Realty Pro", "Home Sales Co", "Dream Properties", "Local Realty", "Real Estate Plus"]
    
    for i in range(5):
        loc = random.choice(locations)
        co = random.choice(companies)
        generate_pitch(loc, co)
    
    logger.info(f"✅ Generated 5 pitches | Ready for outreach\n")
