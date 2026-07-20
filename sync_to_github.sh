#!/bin/bash
# NEXAL Sync Module - Pushes to cryptogod256
cd ~/Nexal-No-Hitch-Riches
git add .
git commit -m "NEXAL Engine Update: $(date)"
git push origin main
echo "[$(date)] Sync complete: Code mirrored to GitHub." >> logs/nexal_engine.log
