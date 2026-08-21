import sqlite3
import os

DB_PATH = "nexal_leads.db"

def ensure_table_exists():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            contact_email TEXT NOT NULL,
            status TEXT DEFAULT 'NEW',
            retainer_value REAL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def record_successful_payment(company_name: str, contact_email: str, retainer_value: float):
    ensure_table_exists()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO leads (company_name, contact_email, status, retainer_value)
        VALUES (?, ?, 'ACTIVE_RETAINER', ?)
    ''', (company_name, contact_email, retainer_value))
    
    conn.commit()
    conn.close()
    print(f"Revenue node locked: {company_name} registered with retainer value ${retainer_value}")

def fetch_all_active_nodes():
    ensure_table_exists()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads WHERE status='ACTIVE_RETAINER'")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    ensure_table_exists()
    print("Nexal Billing Controller online and synchronized.")
