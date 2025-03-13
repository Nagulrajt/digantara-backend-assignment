
import sqlite3

def init_db():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        algorithm TEXT,
                        input_data TEXT,
                        output_data TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def log_api_call(algorithm, input_data, output_data):
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (algorithm, input_data, output_data) VALUES (?, ?, ?)", 
                   (algorithm, str(input_data), str(output_data)))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    conn.close()
    return [{"id": log[0], "algorithm": log[1], "input": log[2], "output": log[3], "timestamp": log[4]} for log in logs]

# Initialize database on startup
init_db()