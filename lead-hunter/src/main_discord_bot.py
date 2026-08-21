import random, logging
from pathlib import Path

Path('logs').mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[logging.FileHandler('logs/system.log'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

locations = ['Miami', 'Austin', 'Denver', 'NYC', 'Seattle']
companies = ['Realty Pro', 'Dream Homes', 'Local Realty', 'Property Plus', 'Home Sales Inc']
pains = ['listing_gap', 'review_gap', 'ad_inactivity', 'social_lag', 'crm_leak']
hooks = [
    "I noticed your MLS only has 3 listings vs competitors with 15+",
    "Your Google reviews are at 2.3 stars with no recent activity",
    "You haven't run Google Ads in 60 days",
    "Your social media hasn't posted in 45 days",
    "You don't have automated follow-up"
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
    "How about a strategy call?"
]

def generate(location, company):
    logger.info(f"\n{'='*60}")
    logger.info(f"📍 {location} | 🏢 {company}")
    logger.info('='*60)
    logger.info(f"🎯 PAIN: {random.choice(pains)} (85/100)")
    logger.info(f"🪝 HOOK: {random.choice(hooks)}")
    logger.info(f"🌉 BRIDGE: {random.choice(bridges)}")
    logger.info(f"📞 CTA: {random.choice(ctas)}")
    logger.info(f"✅ Ready to send\n")
    return True

if __name__ == "__main__":
    logger.info("\n🤖 LEAD HUNTER V1 - INTERACTIVE MODE\n")
    logger.info("Commands:")
    logger.info("  /generate [location] [company]")
    logger.info("  /batch [count]")
    logger.info("  /status")
    logger.info("")
    
    # Demo mode - generate 5 random
    for i in range(5):
        loc = random.choice(locations)
        co = random.choice(companies)
        generate(loc, co)
    
    logger.info(f"✅ Demo complete | Ready for live commands\n")

