import sqlite3

def init_db():
    conn = sqlite3.connect('nexal_intelligence.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS retainers 
                 (id INTEGER PRIMARY KEY, client_name TEXT, status TEXT, value REAL)''')
    conn.commit()
    conn.close()

def log_lead(name, status, value):
    conn = sqlite3.connect('nexal_intelligence.db')
    c = conn.cursor()
    c.execute("INSERT INTO retainers (client_name, status, value) VALUES (?, ?, ?)", (name, status, value))
    conn.commit()
    conn.close()
