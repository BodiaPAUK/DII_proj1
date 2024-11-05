# db_init.py
import sqlite3

def create_tables():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Створення таблиці користувачів
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            login TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Створення таблиці результатів
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS result (
            user_id INTEGER,
            java_skill INTEGER,
            english_skill INTEGER,
            soft_skill INTEGER,
            result_number INTEGER,
            result_word TEXT,
            date_time TEXT,
            FOREIGN KEY(user_id) REFERENCES user(id)
        )
    ''')

    connection.commit()
    connection.close()

# Виклик функції створення таблиць
if __name__ == '__main__':
    create_tables()
