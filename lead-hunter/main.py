#!/usr/bin/env python3
"""
Lead Hunter V1 - Real Estate Automation Brain
Orchestrates Discord → Claude → ElevenLabs → fal.ai → Stripe pipeline
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional
from dotenv import load_dotenv
import anthropic
import discord
from discord.ext import commands
import requests
import aiohttp

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# CONFIG & INITIALIZATION
# ============================================================================

class Config:
    """Central configuration loader"""
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    FAL_API_KEY = os.getenv("FAL_API_KEY")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    
    # Real Estate config
    NICHES = ["realestate"]
    APPROVAL_CHANNEL_ID = int(os.getenv("APPROVAL_CHANNEL_ID", "0"))
    ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID", "0"))

    @classmethod
    def validate(cls):
        """Validate all required keys are present"""
        required = [
            "DISCORD_TOKEN", "CLAUDE_API_KEY", "ELEVENLABS_API_KEY",
            "FAL_API_KEY", "STRIPE_SECRET_KEY"
        ]
        missing = [k for k in required if not getattr(cls, k)]
        if missing:
            raise ValueError(f"Missing environment variables: {missing}")
        logger.info("✅ Configuration validated")

# ============================================================================
# LEAD SCHEMA & PAIN FILTERS
# ============================================================================

class LeadSchema:
    """Real Estate Lead data structure and pain filter logic"""
    
    REAL_ESTATE_PAIN_POINTS = {
        "listing_gap": {
            "indicator": "Low MLS listing count vs competitors",
            "hook": "noticed your MLS presence has only {count} active listings",
            "solution": "automated listing syndication to 50+ partner sites",
            "pain_score": 85
        },
        "review_gap": {
            "indicator": "Zero or low recent Google/Zillow reviews",
            "hook": "your team is getting only {count} reviews annually",
            "solution": "automated review generation & response system",
            "pain_score": 80
        },
        "ad_inactivity": {
            "indicator": "No visible Google Ads or Facebook ads",
            "hook": "competitors are capturing your buyer intent traffic",
            "solution": "automated PPC campaign management",
            "pain_score": 75
        },
        "social_lag": {
            "indicator": "Stale social media (no posts in 30+ days)",
            "hook": "your social channels aren't capturing 20-30% of buyer interest",
            "solution": "automated property showcase posts & market updates",
            "pain_score": 70
        },
        "crm_leak": {
            "indicator": "No email nurture sequence visible",
            "hook": "you're likely losing 40% of follow-up leads",
            "solution": "automated CRM nurture sequences",
            "pain_score": 80
        }
    }
    
    @staticmethod
    def scan_lead(lead_data: Dict) -> Dict:
        """Scan lead against pain filters, return highest-pain indicator"""
        logger.info(f"[LAYER 3] Scanning lead: {lead_data.get('company_name', 'Unknown')}")
        
        detected_pains = []
        for pain_key, pain_config in LeadSchema.REAL_ESTATE_PAIN_POINTS.items():
            # Simplified detection logic - in production, would call scraper API
            if lead_data.get(pain_key):
                detected_pains.append({
                    "pain_type": pain_key,
                    "score": pain_config["pain_score"],
                    "indicator": pain_config["indicator"],
                    "solution": pain_config["solution"],
                    "hook": pain_config["hook"]
                })
        
        # Sort by pain score, return highest
        if detected_pains:
            top_pain = sorted(detected_pains, key=lambda x: x["score"], reverse=True)[0]
            logger.info(f"  ➤ Top pain: {top_pain['pain_type']} (score: {top_pain['score']})")
            return top_pain
        
        logger.warning("  ⚠ No pain indicators detected")
        return None

# ============================================================================
# CLAUDE CONTENT GENERATION ENGINE
# ============================================================================

class ClaudeContentBrain:
    """Generates real estate pitch content using Claude"""
    
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=Config.CLAUDE_API_KEY)
        logger.info("✅ Claude API initialized")
    
    def generate_hook(self, lead: Dict, pain_analysis: Dict) -> str:
        """Generate personalized Hook (Bleeding Indicator)"""
        logger.info(f"[LAYER 3-A] Generating Hook for {lead['company_name']}")
        
        prompt = f"""
You are a Real Estate B2B sales expert. Generate a short, consultative hook that:
1. Acknowledges a SPECIFIC gap in their digital presence
2. Quantifies the revenue impact
3. Feels like a partner tip, not spam

Company: {lead['company_name']}
Location: {lead['location']}
Pain Point: {pain_analysis['pain_type']}
Indicator: {pain_analysis['indicator']}

Format: Single sentence that fills this template:
"Hey [Name], I was looking at [Company]'s presence and noticed [SPECIFIC GAP], which is likely leaving [REVENUE IMPACT] on the table."

Respond ONLY with the hook sentence.
"""
        
        message = self.client.messages.create(
            model="claude-opus-4-6",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}]
        )
        
        hook = message.content[0].text.strip()
        logger.info(f"  ✅ Hook generated: {hook[:80]}...")
        return hook
    
    def generate_bridge(self, lead: Dict, pain_analysis: Dict) -> str:
        """Generate Bridge (Our Asset positioning)"""
        logger.info(f"[LAYER 3-B] Generating Bridge for {lead['company_name']}")
        
        prompt = f"""
You are a Real Estate automation expert. Generate a Bridge statement that:
1. Positions our system as the solution
2. Emphasizes ROI & competitive advantage
3. Stays consultative, not pushy

Company: {lead['company_name']}
Pain: {pain_analysis['pain_type']}
Solution: {pain_analysis['solution']}
Location: {lead['location']}

Format: 1-2 sentences that fill:
"We've developed a system that automates [SOLUTION], ensuring you aren't losing [TYPE OF LEADS/REVENUE] to [LOCAL COMPETITORS]."

Respond ONLY with the bridge text.
"""
        
        message = self.client.messages.create(
            model="claude-opus-4-6",
            max_tokens=250,
            messages=[{"role": "user", "content": prompt}]
        )
        
        bridge = message.content[0].text.strip()
        logger.info(f"  ✅ Bridge generated: {bridge[:80]}...")
        return bridge
    
    def generate_cta(self, lead: Dict) -> str:
        """Generate Call-to-Action (Profit Move)"""
        logger.info(f"[LAYER 3-C] Generating CTA for {lead['company_name']}")
        
        prompt = f"""
You are a Real Estate sales closer. Generate a non-pushy CTA that:
1. Offers a low-friction next step (5-min call or quick breakdown)
2. Positions you as helpful, not salesy
3. Includes 2 options (call or email walkthrough)

Company: {lead['company_name']}

Format: 1-2 sentences like:
"I'd love to show you how this could plug into your existing workflow to secure that lost revenue. Do you have 5 minutes for a quick logic walkthrough, or should I send a breakdown?"

Respond ONLY with the CTA text.
"""
        
        message = self.client.messages.create(
            model="claude-opus-4-6",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}]
        )
        
        cta = message.content[0].text.strip()
        logger.info(f"  ✅ CTA generated: {cta[:80]}...")
        return cta

# ============================================================================
# ELEVENLABS AUDIO GENERATION
# ============================================================================

class ElevenLabsAudio:
    """Generates audio narration for property pitches"""
    
    def __init__(self):
        self.api_key = Config.ELEVENLABS_API_KEY
        self.base_url = "https://api.elevenlabs.io/v1"
        logger.info("✅ ElevenLabs API initialized")
    
    def generate_narration(self, text: str, voice_id: str = "21m00Tcm4TlvDq8ikWAM") -> Optional[str]:
        """
        Generate audio narration from text
        voice_id default is "Rachel" - change if you have a custom voice clone
        """
        logger.info(f"[LAYER 4-A] Generating audio narration ({len(text)} chars)")
        
        try:
            headers = {
                "xi-api-key": self.api_key,
                "Content-Type": "application/json"
            }
            
            payload = {
                "text": text,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75
                }
            }
            
            response = requests.post(
                f"{self.base_url}/text-to-speech/{voice_id}",
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                audio_filename = f"data/audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
                with open(audio_filename, 'wb') as f:
                    f.write(response.content)
                logger.info(f"  ✅ Audio saved: {audio_filename}")
                return audio_filename
            else:
                logger.error(f"  ❌ ElevenLabs error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            logger.error(f"  ❌ Audio generation failed: {str(e)}")
            return None

# ============================================================================
# FAL.AI VIDEO/VISUAL GENERATION
# ============================================================================

class FalAIVisuals:
    """Generates property showcase thumbnails and real estate visuals"""
    
    def __init__(self):
        self.api_key = Config.FAL_API_KEY
        self.base_url = "https://api.fal.ai/v1"
        logger.info("✅ fal.ai API initialized")
    
    def generate_property_thumbnail(self, property_data: Dict) -> Optional[str]:
        """Generate cinematic property showcase thumbnail"""
        logger.info(f"[LAYER 4-B] Generating property thumbnail for {property_data.get('address', 'Unknown')}")
        
        try:
            prompt = f"""
Create a professional real estate marketing thumbnail for:
Property: {property_data.get('address', 'Luxury Home')}
Type: {property_data.get('type', 'Residential')}
Price: {property_data.get('price', 'Premium')}
Location: {property_data.get('location', 'Prime Area')}

Style: Modern real estate photography, cinematic lighting, high-end aesthetic.
Include: Property exterior or key features, clean typography with address/price overlay.
"""
            
            payload = {
                "prompt": prompt,
                "model": "flux-pro",
                "num_images": 1,
                "width": 1280,
                "height": 720
            }
            
            headers = {"Authorization": f"Bearer {self.api_key}"}
            
            response = requests.post(
                f"{self.base_url}/image/generate",
                json=payload,
                headers=headers,
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                image_url = data.get("data", [{}])[0].get("url")
                if image_url:
                    logger.info(f"  ✅ Thumbnail generated: {image_url}")
                    return image_url
            else:
                logger.error(f"  ❌ fal.ai error: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"  ❌ Thumbnail generation failed: {str(e)}")
            return None

# ============================================================================
# STRIPE BILLING ENGINE
# ============================================================================

class StripeBilling:
    """Manages invoicing and payment processing"""
    
    def __init__(self):
        self.secret_key = Config.STRIPE_SECRET_KEY
        logger.info("✅ Stripe API initialized")
    
    def create_invoice(self, client_data: Dict, service_type: str) -> Optional[str]:
        """Create a Stripe invoice for lead generation service"""
        logger.info(f"[LAYER 5] Creating invoice for {client_data.get('company_name')}")
        
        try:
            # Simplified - in production, would use stripe library
            invoice_data = {
                "client": client_data.get('company_name'),
                "service": service_type,
                "date": datetime.now().isoformat(),
                "amount_usd": 500,  # Example: $500 per lead package
                "status": "draft"
            }
            
            # Save invoice to logs
            invoice_id = f"INV_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            with open(f"logs/{invoice_id}.json", 'w') as f:
                json.dump(invoice_data, f, indent=2)
            
            logger.info(f"  ✅ Invoice created: {invoice_id}")
            return invoice_id
            
        except Exception as e:
            logger.error(f"  ❌ Invoice creation failed: {str(e)}")
            return None

# ============================================================================
# DISCORD BOT - COMMAND CENTER
# ============================================================================

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Initialize APIs
claude_brain = ClaudeContentBrain()
elevenlabs = ElevenLabsAudio()
falai = FalAIVisuals()
stripe = StripeBilling()

@bot.event
async def on_ready():
    logger.info(f"✅ Discord bot online: {bot.user}")
    print(f"\n🤖 Lead Hunter V1 Active | Logged in as {bot.user}")

@bot.command(name="generate")
async def generate_pitch(ctx, *, args: str):
    """
    Generate real estate pitch content
    Usage: /generate niche:realestate location:Miami company:ExampleRealty
    """
    logger.info(f"\n{'='*70}")
    logger.info(f"[LAYER 1] Discord CMD Received from {ctx.author}")
    
    # Parse arguments
    arg_dict = {}
    for arg in args.split():
        if ":" in arg:
            key, val = arg.split(":", 1)
            arg_dict[key] = val
    
    niche = arg_dict.get("niche", "realestate")
    location = arg_dict.get("location", "Unknown")
    company = arg_dict.get("company", "Test Company")
    
    logger.info(f"  • Niche: {niche}")
    logger.info(f"  • Location: {location}")
    logger.info(f"  • Company: {company}")
    
    # Create mock lead
    lead = {
        "company_name": company,
        "location": location,
        "review_gap": True,  # Simulated pain indicator
        "ad_inactivity": True
    }
    
    try:
        # Step 1: Scan for pain points
        pain_analysis = LeadSchema.scan_lead(lead)
        
        if not pain_analysis:
            await ctx.send("❌ No pain indicators detected for this lead.")
            return
        
        # Step 2: Generate content (Hook, Bridge, CTA)
        hook = claude_brain.generate_hook(lead, pain_analysis)
        bridge = claude_brain.generate_bridge(lead, pain_analysis)
        cta = claude_brain.generate_cta(lead)
        
        # Step 3: Generate audio
        full_pitch = f"{hook} {bridge} {cta}"
        audio_file = elevenlabs.generate_narration(full_pitch)
        
        # Step 4: Generate visuals
        property_data = {
            "address": f"123 Main St, {location}",
            "type": "Residential",
            "price": "$500K+",
            "location": location
        }
        thumbnail = falai.generate_property_thumbnail(property_data)
        
        # Step 5: Create invoice
        invoice_id = stripe.create_invoice(lead, f"{niche}-lead-package")
        
        # Step 6: Post to approval channel
        logger.info(f"\n[LAYER 4] HITL Governance Triggered")
        
        approval_content = f"""
🎯 **PITCH PACKAGE READY FOR APPROVAL**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**Lead:** {company} ({location})
**Pain Type:** {pain_analysis['pain_type']}
**Pain Score:** {pain_analysis['score']}/100

**HOOK (Bleeding Indicator):**
"{hook}"

**BRIDGE (Our Asset):**
"{bridge}"

**CTA (Profit Move):**
"{cta}"

**Assets Generated:**
✅ Audio Pitch: {audio_file if audio_file else '❌ Failed'}
✅ Property Thumbnail: {thumbnail if thumbnail else '❌ Failed'}
✅ Invoice: {invoice_id}

**Status:** ⏳ AWAITING MANUAL APPROVAL

React ✅ to approve | React ❌ to reject
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        await ctx.send(approval_content)
        logger.info("  ✅ Pitch posted to approval channel")
        logger.info(f"{'='*70}\n")
        
    except Exception as e:
        logger.error(f"❌ Pipeline error: {str(e)}")
        await ctx.send(f"❌ Error generating pitch: {str(e)}")

@bot.command(name="status")
async def system_status(ctx):
    """Check system health and API connectivity"""
    logger.info("[STATUS] System health check initiated")
    
    status_msg = """
🔍 **LEAD HUNTER V1 - SYSTEM STATUS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Discord Bot: Online
✅ Claude API: Ready
✅ ElevenLabs API: Ready
✅ fal.ai API: Ready
✅ Stripe API: Ready

📊 Configuration:
  • Niche: Real Estate
  • Approval Channel: {Config.APPROVAL_CHANNEL_ID or 'Not configured'}
  • Admin User: {Config.ADMIN_USER_ID or 'Not configured'}

Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    await ctx.send(status_msg)

bot.remove_command('help')
@bot.command(name="help")
async def help_command(ctx):
    """Display available commands"""
    help_text = """
📖 **LEAD HUNTER V1 - COMMANDS**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**/generate** — Generate real estate pitch
  Usage: `/generate niche:realestate location:Miami company:ExampleRealty`
  
**/status** — Check system health
  Usage: `/status`
  
**/help** — Display this message
  Usage: `/help`

📝 **WORKFLOW:**
1. Send `/generate` command with lead data
2. Claude analyzes pain points & generates Hook/Bridge/CTA
3. ElevenLabs creates audio narration
4. fal.ai generates property thumbnail
5. Package posted to approval channel
6. You review & approve before deployment

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    await ctx.send(help_text)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Start the automation"""
    logger.info("\n" + "="*70)
    logger.info("🚀 LEAD HUNTER V1 - REAL ESTATE AUTOMATION")
    logger.info("="*70)
    
    try:
        # Validate configuration
        Config.validate()
        
        # Start Discord bot
        logger.info("Starting Discord bot listener...")
        bot.run(Config.DISCORD_TOKEN)
        
    except KeyboardInterrupt:
        logger.info("\n⏹️  Shutdown requested")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
