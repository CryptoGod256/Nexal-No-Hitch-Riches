#!/bin/bash
echo "=== Nexal Intelligence System Status ==="
echo "Checking Uvicorn (FastAPI)..."
pgrep -f "uvicorn app:app" > /dev/null && echo "[ACTIVE] FastAPI is running." || echo "[DOWN] FastAPI is stopped!"

echo "Checking Streamlit Dashboard..."
pgrep -f "streamlit run dashboard.py" > /dev/null && echo "[ACTIVE] Streamlit is running." || echo "[DOWN] Streamlit is stopped!"
echo "========================================"
