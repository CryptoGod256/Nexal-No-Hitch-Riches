#!/bin/bash
# NEXAL Cost Watchdog - Budget Governance
LOG_FILE="~/Nexal-No-Hitch-Riches/logs/nexal_engine.log"

TASK_COUNT=$(grep -c "Assigning task" $LOG_FILE)

if [ "$TASK_COUNT" -gt 50 ]; then
    echo "[$(date)] ALERT: Budget threshold approaching. Routing to Tier-1 models." >> $LOG_FILE
else
    echo "[$(date)] Operational status: Budget nominal." >> $LOG_FILE
fi
