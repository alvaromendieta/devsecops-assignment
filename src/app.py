from flask import Flask, request, render_template_string, jsonify
import sqlite3
import os
import subprocess

app = Flask(__name__)

# VULNERABILIDAD 1: Secret hardcodeado
SECRET_KEY = "super-secret-key-12345"
API_KEY = "sk-1234567890abcdefghijklmnop"

# VULNERABILIDAD 2: Debug mode
app.config['DEBUG'] = True

@app.route('/')
def index():
    return """
    <h1>DevSecOps Vulnerable App</h1>
    <ul>
        <li><a href="/search?q=test">SQL Injection</a></li>
        <li><a href="/greet?name=Alice">XSS Demo</a></li>
        <li><a href="/admin">Admin (no auth)</a></li>
    </ul>
    """

@app.route('/search')
def search():
    # VULNERABILIDAD 3: SQL Injection
    query = request.args.get('q', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    sql = f"SELECT * FROM users WHERE name = '{query}'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/greet')
def greet():
    # VULNERABILIDAD 4: XSS
    name = request.args.get('name', 'Guest')
    template = f"<h1>Hello {name}!</h1>"
    return render_template_string(template)

@app.route('/execute')
def execute_command():
    # VULNERABILIDAD 5: Command Injection
    cmd = request.args.get('cmd', 'echo hello')
    result = os.system(cmd)
    return jsonify({"result": result})

@app.route('/admin')
def admin_panel():
    return f"<h1>Admin Panel</h1><p>API Key: {API_KEY}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
