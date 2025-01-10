from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(_name_)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Insecure password storage (storing plain text password)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

if _name_ == "_main_":
    app.run(debug=True)
    from werkzeug.security import generate_password_hash, check_password_hash

# Storing password hash
hashed_password = generate_password_hash(password)

# Verifying password
if check_password_hash(hashed_password, password_input):
    # Allow login
 cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
                app.run(debug=False)
                from flask import session

# Set session data after successful login
session['user_id'] = user['id']

# Check if user is logged in
if 'user_id' in session:
    return redirect(url_for('dashboard'))
    pip install bandit
bandit -r myapp/
