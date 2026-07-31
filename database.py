import sqlite3

conn = sqlite3.connect("games.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS games(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               white text,
               black text,
               result text,
               opening text,
               white_elo INTEGER,
               black_elo INTEGER,
               pgn TEXT,
               analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

conn.commit()
conn.close()
