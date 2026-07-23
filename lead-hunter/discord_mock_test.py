import random, logging
from datetime import datetime
from pathlib import Path

Path('logs').mkdir(exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[logging.FileHandler('logs/system.log'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

class Bot:
    def __init__(self):
        self.locs = ["Miami", "Austin", "Denver", "Seattle", "NYC"]
        self.cos = ["DreamHomes", "RealtyCo", "LocalRealty", "Urban Properties", "HomeExperts"]
        self.pains = ["listing_gap", "review_gap", "ad_inactivity", "social_lag", "crm_leak"]
        self.hooks = [
            "I noticed your MLS only has 3 listings vs competitors with 15+",
            "Your Google reviews are at 2.3 stars with no recent activity",
            "You haven't run Google Ads in 60 days",
            "Your social media hasn't posted in 45 days",
            "You don't have automated follow-up"
        ]
        self.bridges = [
            "We automate listing syndication to 50+ sites",
            "We automate review requests 24/7",
            "We run targeted Google Ads automatically",
            "We automate social posts 3/week",
            "We have CRM nurture engine converting 40% more leads"
        ]
        self.ctas = ["Want a 5-minute walkthrough?", "Free demo?", "Quick call?", "Can I show you ROI?", "Strategy call?"]
    
    def generate(self, location, company):
        pain = random.choice(self.pains)
        logger.info(f"\n{'='*70}")
        logger.info(f"📍 Location: {location} | 🏢 Company: {company}")
        logger.info(f"{'='*70}")
        logger.info(f"🎯 PAIN: {pain} (Score: 85/100)")
        logger.info(f"🪝 HOOK: {random.choice(self.hooks)}")
        logger.info(f"🌉 BRIDGE: {random.choice(self.bridges)}")
        logger.info(f"📞 CTA: {random.choice(self.ctas)}")
        logger.info(f"✅ Ready to send\n")
    
    def test(self):
        logger.info("\n" + "="*70)
        logger.info("🤖 DISCORD COMMAND CENTER - MOCK TEST")
        logger.info("="*70)
        logger.info("\nSimulating Discord /generate commands...\n")
        
        commands = [
            ("Miami", "DreamHomes"),
            ("Austin", "RealtyCo"),
            ("NYC", "LocalRealty"),
            ("Denver", "Urban Properties"),
            ("Seattle", "HomeExperts"),
            ("Miami", "Property Plus"),
            ("Austin", "Real Estate Co"),
        ]
        
        for i, (loc, co) in enumerate(commands, 1):
            logger.info(f"COMMAND #{i}: /generate niche:realestate location:{loc} company:{co}")
            self.generate(loc, co)
        
        logger.info("="*70)
        logger.info(f"✅ MOCK TEST COMPLETE - {len(commands)} pitches generated")
        logger.info("="*70 + "\n")

if __name__ == "__main__":
    bot = Bot()
    bot.test()
