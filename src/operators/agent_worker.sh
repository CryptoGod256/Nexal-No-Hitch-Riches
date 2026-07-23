#!/bin/bash
# NEXAL Agentic Worker - Persistent Scalable Loop
BASE_DIR="$HOME/Nexal-No-Hitch-Riches"
LOG_FILE="$BASE_DIR/logs/nexal_engine.log"
QUEUE_FILE="$BASE_DIR/api/task_queue.txt"

mkdir -p "$(dirname "$LOG_FILE")"
mkdir -p "$(dirname "$QUEUE_FILE")"

echo "[$(date -u)] Worker initiated with fault-tolerant scaling. Entering deep-work cycle..." >> "$LOG_FILE"

while true; do
    if [ -f "$QUEUE_FILE" ] && [ -s "$QUEUE_FILE" ]; then
        TASK=$(head -n 1 "$QUEUE_FILE")
        
        if [ -n "$TASK" ]; then
            echo "[$(date -u)] Processing task: $TASK" >> "$LOG_FILE"
            
            # Route to Brain Pair if delegation script exists
            DELEGATION_SCRIPT="$BASE_DIR/src/operators/operator_delegation.sh"
            if [ -f "$DELEGATION_SCRIPT" ]; then
                "$DELEGATION_SCRIPT" "CODE" "$TASK"
            fi
            
            # Log performance if logger exists
            PERF_LOGGER="$BASE_DIR/src/operators/perf_logger.sh"
            if [ -f "$PERF_LOGGER" ]; then
                "$PERF_LOGGER" "$TASK" "COMPLETED"
            fi
            
            # Clean queue safely using temp file or sed
            sed -i '1d' "$QUEUE_FILE"
        fi
    fi
    sleep 2
done
