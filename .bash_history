pkg update && pkg upgrade
pkg install wget unzip python nano
chmod +x setup.sh
./setup.sh
chmod +x setup.sh
./setup.sh
ls
Lead Hunter V1/
├── src/
│   └── main.py                    # Main orchestrator (2,000 lines)
├── config/
│   └── lead_schema.json           # Real Estate pain point definitions
├── logs/
│   └── system.log                 # Operational logs
├── data/
│   ├── audio_*.mp3                # Generated narrations
│   ├── thumbnails_*.jpg           # Property thumbnails
│   └── invoices_*.json            # Stripe invoice records
├── agents/
│   └── sales_agent.md             # Claude manifest & constraints
├── .env                           # API keys (NEVER commit)
├── requirements.txt               # Python dependencies
├── setup.sh                       # Ubuntu VPS setup script
└── README.md                      # This file
# SSH into your Ubuntu VPS
ssh user@your-vps-ip
# Clone or download Lead Hunter V1
cd /home/user
git clone <your-repo-url> lead-hunter-v1
cd lead-hunter-v1
# Make setup script executable
chmod +x setup.sh
# Run setup
./setup.sh
sudo systemctl daemon-reload
sudo systemctl enable lead-hunter.service
sudo systemctl start lead-hunter.service
# Check status
sudo systemctl status lead-hunter.service
# View logs
tail -f logs/system.log
# ============================================================================
# LEAD HUNTER V1 - SETUP SCRIPT FOR UBUNTU VPS
# Run: chmod +x setup.sh && ./setup.sh
# ============================================================================
echo "🚀 Lead Hunter V1 - Setup Initialization"
echo "=========================================="
# Create directory structure
echo "📁 Creating 4-Layer Foundry..."
mkdir -p src
mkdir -p config
mkdir -p logs
mkdir -p data
mkdir -p agents
mkdir -p backups
# Initialize files
touch logs/system.log
touch config/lead_schema.json
touch data/.gitkeep
touch backups/.gitkeep
echo "✅ Directories created"
# Check Python version
echo ""
echo "🐍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then     echo "❌ Python3 not found. Installing...";     sudo apt-get update;     sudo apt-get install -y python3 python3-pip python3-venv; fi
PYTHON_VERSION=$(python3 --version)
echo "✅ $PYTHON_VERSION found"
# Create virtual environment
echo ""
echo "🔧 Setting up Python virtual environment..."
if [ ! -d "venv" ]; then     python3 -m venv venv;     echo "✅ Virtual environment created"; else     echo "✅ Virtual environment already exists"; fi
# Activate virtual environment
source venv/bin/activate
echo "✅ Virtual environment activated"
# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -eq 0 ]; then     echo "✅ All dependencies installed"; else     echo "❌ Dependency installation failed";     exit 1; fi
