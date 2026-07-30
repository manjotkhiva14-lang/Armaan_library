import sqlite3 

def get_connection():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
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


def add_student(student_id , name , contact , shift):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students VALUES(?, ?, ?, ?, ?)",
        (student_id , name , contact , shift , None)
    )
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students 

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

def update_seat(student_id , seat_number ):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute (
       " UPDATE students SET seat_allotted = ? WHERE student_id = ?",
       (seat_number , student_id)
    )
    conn.commit()
    conn.close()

def remove_seat(student_id ):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET seat_allotted = NULL  WHERE student_id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()

def get_seat(seat_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seats WHERE seat_number = ?", (seat_number,))
    seat = cursor.fetchone()
    conn.close()
    return seat

def update_seat_allocation(seat_number, shift, student_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    if shift == "9-2":
        cursor.execute(
            "UPDATE seats SET shift_9_2 = ? WHERE seat_number = ?",
            (student_id, seat_number)
        )
    elif shift == "2-7":
        cursor.execute(
            "UPDATE seats SET shift_2_7 = ? WHERE seat_number = ?",
            (student_id, seat_number)
        )
    elif shift == "9-7":
        cursor.execute(
            "UPDATE seats SET shift_9_7 = ? WHERE seat_number = ?",
            (student_id, seat_number)
        )
    
    conn.commit()
    conn.close()

def get_all_seats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seats")
    seats = cursor.fetchall()
    conn.close()
    return seats

