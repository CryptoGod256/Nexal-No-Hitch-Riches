#!/bin/bash
BACKUP_DIR="backups"
mkdir -p $BACKUP_DIR
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Back up database files if they exist
FOUND=0
for db in database.db nexal_leads.db; do
    if [ -f "$db" ]; then
        cp "$db" "$BACKUP_DIR/${db%.*}_$TIMESTAMP.db"
        echo "[SUCCESS] Backed up $db to $BACKUP_DIR/${db%.*}_$TIMESTAMP.db"
        FOUND=1
    fi
done

if [ $FOUND -eq 0 ]; then
    echo "[WARNING] No standard database files found to back up."
fi
