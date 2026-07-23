#!/bin/bash

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
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip python3-venv
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ $PYTHON_VERSION found"

# Create virtual environment
echo ""
echo "🔧 Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate
echo "✅ Virtual environment activated"

# Install dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed"
else
    echo "❌ Dependency installation failed"
    exit 1
fi

# Setup environment variables
echo ""
echo "🔐 Setting up environment configuration..."
if [ ! -f ".env" ]; then
    cp .env.template .env
    echo "✅ .env template copied"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env with your API keys:"
    echo "   nano .env"
    echo ""
else
    echo "✅ .env already exists"
fi

# Setup gitignore
echo ""
echo "🛡️  Configuring security (.gitignore)..."
cat > .gitignore << 'EOF'
.env
*.pyc
__pycache__/
*.log
logs/*.log
data/*.csv
data/*.mp3
data/*.jpg
data/*.png
venv/
.DS_Store
*.swp
*.swo
backups/*
.idea/
.vscode/
EOF
echo "✅ .gitignore configured"

# Create systemd service file (for auto-start on Ubuntu)
echo ""
echo "🔄 Creating systemd service for auto-start..."
SCRIPT_PATH=$(pwd)

sudo tee /etc/systemd/system/lead-hunter.service > /dev/null << EOF
[Unit]
Description=Lead Hunter V1 - Real Estate Automation
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$SCRIPT_PATH
ExecStart=$SCRIPT_PATH/venv/bin/python $SCRIPT_PATH/src/main.py
Restart=on-failure
RestartSec=30
StandardOutput=append:$SCRIPT_PATH/logs/system.log
StandardError=append:$SCRIPT_PATH/logs/system.log

[Install]
WantedBy=multi-user.target
EOF

echo "✅ Systemd service created at /etc/systemd/system/lead-hunter.service"
echo ""
echo "To enable auto-start:"
echo "  sudo systemctl daemon-reload"
echo "  sudo systemctl enable lead-hunter.service"
echo "  sudo systemctl start lead-hunter.service"

# Display startup command
echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "📝 Next Steps:"
echo "1. Edit .env with your API keys:"
echo "   nano .env"
echo ""
echo "2. Test the bot locally:"
echo "   source venv/bin/activate"
echo "   python src/main.py"
echo ""
echo "3. Or run as systemd service:"
echo "   sudo systemctl start lead-hunter.service"
echo "   sudo systemctl status lead-hunter.service"
echo ""
echo "4. Monitor logs:"
echo "   tail -f logs/system.log"
echo ""
echo "=========================================="
