import sqlite3
import hashlib

# VULNERABILIDAD: Credenciales hardcodeadas
DB_PASSWORD = "admin123"
DB_USER = "root"

def hash_password(password):
    # VULNERABILIDAD: MD5 es inseguro
    return hashlib.md5(password.encode()).hexdigest()

def create_user(username, password):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    hashed = hash_password(password)
    # VULNERABILIDAD: SQL Injection
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
