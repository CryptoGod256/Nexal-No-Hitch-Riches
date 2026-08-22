#!/bin/bash

# Exit immediately if any command fails
set -e

PROJECT_DIR="/root/nexal-intelligence"

echo "🚀 Starting Nexal Intelligence Automated Setup..."

# 1. Ensure project directory exists on droplet and navigate into it
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# 2. Initialize package.json if missing
if [ ! -f "package.json" ]; then
    echo "📦 Initializing Node.js package..."
    npm init -y
fi

# 3. Install required dependencies
echo "📥 Installing Express..."
npm install express

# 4. Write/Update server.js with the webhook listener engine
echo "📝 Writing server.js webhook engine..."
cat << 'EOF' > server.js
const express = require('express');
const crypto = require('crypto');

const app = express();
const PORT = process.env.PORT || 3000;

// Capture raw body for secure webhook signature validation
app.use(express.json({
  verify: (req, res, buf) => {
    req.rawBody = buf;
  }
}));

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'online', service: 'nexal-api-engine' });
});

// Webhook ingestion endpoint
app.post('/webhook/store-events', (req, res) => {
  const shopifyHeader = req.get('X-Shopify-Topic');
  const stripeHeader = req.get('Stripe-Signature');

  if (shopifyHeader) {
    console.log(`[Shopify Event Received]: ${shopifyHeader}`);
    return res.status(200).send('Shopify webhook received successfully');
  } 
  
  if (stripeHeader) {
    console.log('[Stripe Event Received]');
    return res.status(200).send('Stripe webhook received successfully');
  }

  res.status(400).send('Missing valid webhook headers');
});

app.listen(PORT, () => {
  console.log(`Nexal Intelligence API engine running on port ${PORT}`);
});
EOF

# 5. Start or restart application with PM2
echo "⚙️ Configuring PM2 process manager..."
pm2 restart nexal-intelligence 2>/dev/null || pm2 start server.js --name "nexal-intelligence"
pm2 save

echo "✅ Nexal Intelligence Webhook engine is live and running under PM2!"
