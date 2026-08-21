#!/bin/bash
# ==========================================
# NEXAL INTELLIGENCE MULTIVERSE DEPLOYMENT
# ==========================================

set -e

echo "⚡ Initializing Nexal Intelligence Multiverse Setup..."

# 1. Update system packages
echo "🔄 Updating package lists..."
sudo apt update && sudo apt upgrade -y

# 2. Install Node.js & npm (if not already installed)
if ! command -v node &> /dev/null; then
    echo "📦 Installing Node.js LTS..."
    curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo bash -
    sudo apt install -y nodejs
else
    echo "✅ Node.js is already installed ($(node -v))"
fi

# 3. Create project directory structure
echo "📁 Setting up workspace directories..."
mkdir -p nexal-intelligence/public nexal-intelligence/server
cd nexal-intelligence

# 4. Initialize package.json and install dependencies
echo "📦 Installing required npm modules (Express, CORS, Stripe, http-server)..."
if [ ! -f "package.json" ]; then
    npm init -y
fi
npm install express cors stripe http-server --save

# 5. Generate backend server.js
echo "⚙️ Writing server.js backend controller..."
cat << 'EOF' > server.js
const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/health', (req, res) => {
    res.json({ status: 'online', system: 'Nexal Intelligence Core', timestamp: new Date() });
});

app.listen(PORT, () => {
    console.log(`🚀 Nexal Multiverse Server live on port ${PORT}`);
});
EOF

# 6. Generate frontend cyberpunk interface
echo "🌐 Writing public/index.html UI module..."
cat << 'EOF' > public/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexal Intelligence Multiverse</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .neon-border { border: 1px solid rgba(6, 182, 212, 0.4); box-shadow: 0 0 15px rgba(6, 182, 212, 0.15); }
        .neon-btn { background: linear-gradient(135deg, #06b6d4, #3b82f6); color: black; font-weight: bold; transition: all 0.3s ease; }
        .neon-btn:hover { box-shadow: 0 0 20px rgba(6, 182, 212, 0.6); }
    </style>
</head>
<body class="bg-black text-white min-h-screen p-6 font-mono">
    <div class="max-w-7xl mx-auto space-y-6">
        <header class="neon-border rounded-lg bg-black/80 p-6 flex justify-between items-center">
            <div>
                <h1 class="text-2xl font-black text-cyan-400">NEXAL INTELLIGENCE MULTIVERSE</h1>
                <p class="text-xs text-gray-400">Cloud Droplet Environment Active | Node & Comm-Matrix Online</p>
            </div>
            <div class="text-xs bg-cyan-950 text-cyan-300 border border-cyan-500/50 px-3 py-1 rounded">
                Status: Operational ⚡
            </div>
        </header>
        <div class="neon-border rounded-lg bg-black/80 p-8 text-center space-y-4">
            <h2 class="text-xl font-bold text-cyan-300">Welcome to Your Cyberpunk Command Grid</h2>
            <p class="text-sm text-gray-400 max-w-xl mx-auto">Your full-stack infrastructure, Discord/YouTube feeds, and Comm-Matrix modules are successfully initialized and ready for deployment.</p>
            <button class="neon-btn px-6 py-2.5 rounded text-sm cursor-pointer">Launch Core System</button>
        </div>
    </div>
</body>
</html>
EOF

echo "🎉 Deployment preparation complete!"
echo "🚀 Starting Nexal Multiverse Server..."
node server.js
