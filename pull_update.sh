#!/bin/bash
echo "Pulling latest updates from GitHub..."
git pull origin main
echo "Restarting background services..."
pkill -f "uvicorn app:app"
pkill -f "streamlit run dashboard.py"
nohup uvicorn app:app --host 0.0.0.0 --port 8000 &
nohup streamlit run dashboard.py --server.port 8501 --server.headless true &
echo "Done! Services restarted."
