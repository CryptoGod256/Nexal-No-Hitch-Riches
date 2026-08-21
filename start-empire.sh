#!/bin/bash
cd ~/nexal-intelligence || exit 1

cat << 'ENV' > .env
STRIPE_SECRET_KEY=Sk_live_51TvfdqGTw4JQB6tL4ja82x8IukKOrXOZhEhivN0uueyfPtJjQ3kUUqnkMEVvzuXL3FBiv9NOsdVToetoKUAWqY8G00GZk6HjPK
PORT=3000
ENV

export STRIPE_SECRET_KEY="Sk_live_51TvfdqGTw4JQB6tL4ja82x8IukKOrXOZhEhivN0uueyfPtJjQ3kUUqnkMEVvzuXL3FBiv9NOsdVToetoKUAWqY8G00GZk6HjPK"
export PORT=3000

grep -qF ".env" .gitignore 2>/dev/null || echo ".env" >> .gitignore

npm install express stripe dotenv --silent

echo "🚀 Booting Nexal API Gateway..."
node server.js
