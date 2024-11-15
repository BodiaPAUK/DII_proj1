import sqlite3
from datetime import datetime
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = (BASE_DIR + '\\database.db')

def get_connection():
    return sqlite3.connect(DATABASE)

def save_user(username, login, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (username, login, password) VALUES (?, ?, ?)",
                   (username, login, password))
    conn.commit()
    conn.close()

def get_user_by_login(login):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password FROM user WHERE login = ?", (login,))
    user = cursor.fetchone()
    conn.close()
    return user

def save_user_result(user_id, java_skill, english_skill, soft_skill, result_number, result_word):
    conn = get_connection()
    cursor = conn.cursor()
    date_time = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO result (user_id, java_skill, english_skill, soft_skill, result_number, result_word, date_time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, java_skill, english_skill, soft_skill, result_number, result_word, date_time))
    conn.commit()
    conn.close()

def get_user_results(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM result WHERE user_id = ?", (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results
