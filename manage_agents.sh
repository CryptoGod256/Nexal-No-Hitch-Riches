#!/usr/bin/env bash
# NEXAL Manager - Agent Oversight Script
# Exit on error, undefined variables, and pipe failures
set -euo pipefail

echo "NEXAL AI Operators Initializing..."

# Verify log file exists before tailing
if [[ -f "logs/nexal_engine.log" ]]; then
    tail -f logs/nexal_engine.log
else
    echo "[ERROR] Log file not found. NEXAL engine must be running first."
    exit 1
fi

