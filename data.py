import sqlite3
import os

# --- DB file name
db_file = "school-year.db"

# --- Remove old DB file if exists (for a clean start)
if os.path.exists(db_file):
    os.remove(db_file)

# --- Connect to actual DB file (creates it if not exists)
conn = sqlite3.connect(db_file)
cur = conn.cursor()

cur.executescript("""
    CREATE TABLE student_tbl (
        student_id TEXT PRIMARY KEY,
        student_name VARCHAR(50),
        student_email VARCHAR(50)
    );

    CREATE TABLE course_tbl (
        course_id TEXT PRIMARY KEY,
        course_name VARCHAR(50),
        department_name VARCHAR(50)
    );

    CREATE TABLE instructor_tbl (
        instructor_id TEXT PRIMARY KEY,
        instructor_name VARCHAR(50),
        instructor_email VARCHAR(50),
        semester VARCHAR(50)
    );

    CREATE TABLE room_tbl (
        room_id TEXT PRIMARY KEY,
        room_name VARCHAR(50),
        room_capacity INT
    );

    CREATE TABLE schedule_tbl (
        schedule_id TEXT PRIMARY KEY,
        day VARCHAR(50),
        time VARCHAR(50)
    );

    CREATE TABLE enrollment_tbl (
        student_id TEXT,
        course_id TEXT,
        instructor_id TEXT,
        room_id TEXT,
        schedule_id TEXT,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES student_tbl(student_id),
        FOREIGN KEY (course_id) REFERENCES course_tbl(course_id),
        FOREIGN KEY (instructor_id) REFERENCES instructor_tbl(instructor_id),
        FOREIGN KEY (room_id) REFERENCES room_tbl(room_id),
        FOREIGN KEY (schedule_id) REFERENCES schedule_tbl(schedule_id)
    );

    INSERT INTO enrollment_tbl
    (student_id, course_id, instructor_id, room_id, schedule_id)
    VALUES 
    ("S101", "C001", "I101", "R101", "SCH001"),
    ("S102", "C002", "I102", "R102", "SCH002"),
    ("S103", "C003", "I103", "R103", "SCH003");
    
    INSERT INTO course_tbl
    (course_id, course_name, department_name)
    VALUES 
    ("C001", "Database", "IT Department"),
    ("C002", "Web Development", "IT Department"),
    ("C003", "Networking", "Engineering");
    
    INSERT INTO instructor_tbl
    (instructor_id, instructor_name, instructor_email, semester)
    VALUES 
    ("I101", "Prof. Rivera", "rivera@school.edu", "1st Sem"),
    ("I102", "Prof. Cruz", "cruz@school.edu", "1st Sem"),
    ("I103", "Prof. Santos", "santos@school.edu", "2nd Sem");
    
    INSERT INTO room_tbl
    (room_id, room_name, room_capacity)
    VALUES 
    ("R101", "Lab A", 30),
    ("R102", "Lab B", 25),
    ("R103", "Lab C", 20);

    INSERT INTO schedule_tbl
    (schedule_id, day, time)
    VALUES 
    ("SCH001", "Monday", "8:00-10:00"),
    ("SCH002", "Tuesday", "10:00-12:00"),
    ("SCH003", "Wednesday", "1:00-3:00");

    INSERT INTO student_tbl
    (student_id, student_name, student_email)
    VALUES 
    ("S101", "Maria Santos", "maria@school.edu"),
    ("S102", "John Cruz", "john@school.edu"),
    ("S103", "Ana Rivera", "ana@school.edu");
    
    SELECT * FROM student_tbl
    WHERE student_name LIKE "m%";
""")




conn.commit()
conn.close()