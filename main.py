import sqlite3

con = sqlite3.connect("database.db")

con.executescript('''
    DROP TABLE IF EXISTS author;
    
    CREATE TABLE author (
           author_id INTEGER PRIMARY KEY AUTOINCREMENT,
           author_name VARCHAR(30)
    );
    
    ''')

con.close()