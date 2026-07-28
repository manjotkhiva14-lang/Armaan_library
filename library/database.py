import sqlite3 

def get_connection():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXIST students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL ,
            contact TEXT NOT NULL,
            shift TEXT NOT NULL,
            seat_allotted INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seats (
            seat_number INTEGER PRIMARY KEY,
            shift_9_2 INTEGER,
            shift_2_7 INTEGER,
            shift_9_7 INTEGER
       )
    ''')

    conn.commit()
    conn.close()