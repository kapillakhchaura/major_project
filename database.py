import bcrypt
import sqlite3
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "ai_doctor.db")

print("DB PATH:", DB_NAME)
# ---------------------------
# Initialize Database
# ---------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT,
        security_question TEXT,
        security_answer TEXT
    )
    """)

    # REPORTS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        disease TEXT,
        result TEXT,
        pdf_path TEXT,
        created_at TEXT,
        risk_score REAL,
        risk_category TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------------------
# Add User
# ---------------------------
def add_user(username, password, role, question, answer):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 🔥 check if user already exists
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        raise Exception("User exists")
    

    # 🔐 hash password
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    cursor.execute("""
        INSERT INTO users (username, password, role, security_question, security_answer)
        VALUES (?, ?, ?, ?, ?)
    """, (username, hashed.decode(), role, question, answer.lower()))

    conn.commit()
    conn.close()

def user_exists(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()
    return result is not None

# ---------------------------
# Verify User
# ---------------------------
def verify_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row:
        stored_hash = row[0]
        role = row[1]

        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            return role

    return None


def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user


def update_password(username, new_password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())

    cursor.execute(
        "UPDATE users SET password = ? WHERE username = ?",
        (hashed.decode(), username)
    )

    conn.commit()
    conn.close()

# ---------------------------
# Security Question
# ---------------------------
def get_security_question(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT security_question FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    return row[0] if row else None


# ---------------------------
# Reset Password
# ---------------------------
def reset_password(username, answer, new_password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT security_answer FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    if row and row[0] == answer.lower():
        hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        cursor.execute(
            "UPDATE users SET password = ? WHERE username = ?",
            (hashed.decode(), username)
        )
        conn.commit()
        conn.close()
        return True

    conn.close()
    return False


# ---------------------------
# Save Report
# ---------------------------
def save_report_to_db(username, disease, result, pdf_path, risk_score, risk_category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reports 
    (username, disease, result, pdf_path, created_at, risk_score, risk_category)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        username,
        disease,
        result,
        pdf_path,
        datetime.now().isoformat(),
        risk_score,
        risk_category
    ))

    conn.commit()
    conn.close()


# ---------------------------
# Get User Reports
# ---------------------------
def get_user_reports(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT disease, result, pdf_path, created_at, risk_score, risk_category
    FROM reports
    WHERE username = ?
    ORDER BY created_at DESC
    """, (username,))

    rows = cursor.fetchall()
    conn.close()

    reports = []

    for r in rows:
        reports.append({
            "disease": r[0],
            "result": r[1],
            "pdf_path": r[2],
            "created_at": r[3],
            "risk_score": r[4],
            "risk_category": r[5]
        })

    return reports

# ---------------------------
# Get All Reports
# ---------------------------
def get_all_reports():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    return rows


# ---------------------------
# Get All Users
# ---------------------------
def get_all_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT username, role, created_at FROM users")
    rows = cursor.fetchall()
    conn.close()

    return rows


# ===========================
# 📊 ANALYTICS FUNCTIONS
# ===========================

def get_risk_distribution():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT disease, risk_category, COUNT(*)
    FROM reports
    GROUP BY disease, risk_category
    """)

    data = cursor.fetchall()
    conn.close()
    return data


def get_average_risk():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT disease, AVG(risk_score)
    FROM reports
    GROUP BY disease
    """)

    data = cursor.fetchall()
    conn.close()
    return data


def get_monthly_trend():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT strftime('%Y-%m', created_at), AVG(risk_score)
    FROM reports
    GROUP BY strftime('%Y-%m', created_at)
    ORDER BY strftime('%Y-%m', created_at)
    """)

    data = cursor.fetchall()
    conn.close()
    return data


def get_top_high_risk():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT username, disease, risk_score
    FROM reports
    ORDER BY risk_score DESC
    LIMIT 10
    """)

    data = cursor.fetchall()
    conn.close()
    return data