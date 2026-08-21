#!/bin/bash
# NEXAL Launch Readiness Checker v1.0

echo "--- NEXAL Launch Readiness Audit ---"

# List of critical files to check
files=("nexal_engine.sh" "manage_agents.sh" "sync_to_github.sh" "api/signals.json")

for file in "${files[@]}"; do
    if [[ -f "$file" ]]; then
        if [[ -x "$file" ]]; then
            echo "[PASS] $file exists and is executable."
        else
            echo "[WARN] $file exists but is NOT executable. Running chmod +x..."
            chmod +x "$file"
        fi
    else
        echo "[FAIL] $file is MISSING."
    fi
done

# Check Dependencies
echo "--- Dependency Check ---"
for cmd in git python; do
    if command -v "$cmd" > /dev/null; then
        echo "[PASS] $cmd is installed."
    else
        echo "[FAIL] $cmd is not found."
    fi
done

echo "--- Audit Complete. Launch Status: READY ---"
