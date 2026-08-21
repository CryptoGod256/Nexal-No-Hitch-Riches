#!/bin/bash
echo "=== NEXAL INTELLIGENCE SYSTEM STATUS ==="
echo "[+] Repository Directory:" && pwd
echo ""
echo "[+] Active Logs & Manifests:" && ls -la logs/
echo ""
echo "[+] Latest Intelligence State:"
if [ -f logs/autonomous_intelligence_state.json ]; then
    cat logs/autonomous_intelligence_state.json
else
    echo "No intelligence state log found."
fi
echo ""
echo "=== SYSTEM CHECK COMPLETE ==="
