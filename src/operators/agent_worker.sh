#!/bin/bash
# NEXAL Agentic Worker - Persistent Loop
LOG_FILE="~/Nexal-No-Hitch-Riches/logs/nexal_engine.log"

echo "[$(date)] Worker initiated. Entering deep-work cycle..." >> $LOG_FILE

while true; do
    # Check for new tasks in the queue
    if [ -f ~/Nexal-No-Hitch-Riches/api/task_queue.txt ]; then
        TASK=$(head -n 1 ~/Nexal-No-Hitch-Riches/api/task_queue.txt)
        
        # Route to Brain Pair
        ~/Nexal-No-Hitch-Riches/src/operators/operator_delegation.sh "CODE" "$TASK"
        
        # Log performance
        ~/Nexal-No-Hitch-Riches/src/operators/perf_logger.sh "$TASK" "COMPLETED"
        
        # Clean queue
        sed -i '1d' ~/Nexal-No-Hitch-Riches/api/task_queue.txt
    fi
    sleep 5
done
