import sqlite3

def setup_database():
    conn = sqlite3.connect('sudoku_game.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT,
                    wins INTEGER,
                    losses INTEGER
                )''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('sudoku_game.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password, wins, losses) VALUES (?, ?, 0, 0)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False  # Username already exists
    finally:
        conn.close()
    return True

def login_user(username, password):
    conn = sqlite3.connect('sudoku_game.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user

def update_user_stats(username, won):
    conn = sqlite3.connect('sudoku_game.db')
    c = conn.cursor()
    if won:
        c.execute('UPDATE users SET wins = wins + 1 WHERE username = ?', (username,))
    else:
        c.execute('UPDATE users SET losses = losses + 1 WHERE username = ?', (username,))
    conn.commit()
    conn.close()
