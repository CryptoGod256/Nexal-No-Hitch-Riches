#!/usr/bin/env bash
# NEXAL Sync Module - Pushes to cryptogod256
# Hardened with error checking

cd "$HOME/Nexal-No-Hitch-Riches" || exit

git add .
git commit -m "NEXAL Engine Update: $(date)"
git push origin main

echo "[$(date)] Sync complete: Code mirrored to GitHub." >> logs/nexal_engine.log

