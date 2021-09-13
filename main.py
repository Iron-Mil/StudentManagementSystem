import psycopg2 as psy
from constants import *
from flask import Flask
from flask import jsonify


# Creates and populates all the tables we need if they don't exist already
def create_tables():
    conn = psy.connect(dbname=DB_NAME, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students
                (student_id SERIAL PRIMARY KEY, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL, 
                year_of_studying INTEGER NOT NULL,
                date_of_birth DATE NOT NULL);""")

    cur.execute("SELECT COUNT (*) FROM students")
    if cur.fetchall()[0][0] == 0:
        cur.execute("""INSERT INTO students(first_name,last_name,year_of_studying, date_of_birth)
              VALUES('Milos', 'Korac', 2, '1996-02-21'),
              ('Marko', 'Kostic', 3, '1995-03-13');""")

    cur.execute("""CREATE TABLE IF NOT EXISTS lectures
                (lecture_id SERIAL PRIMARY KEY, 
                teacher_id INTEGER NOT NULL, 
                course TEXT NOT NULL, 
                required BOOL NOT NULL)""")

    cur.execute("SELECT COUNT (*) FROM lectures")
    if cur.fetchall()[0][0] == 0:
        cur.execute("""INSERT INTO lectures(teacher_id,course, required)
              VALUES(3, 'Working with data bases', False),
              (2, 'Intro to object orientated programming', True);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS courses
                (course_id SERIAL PRIMARY KEY, 
                course_name TEXT NOT NULL,
                teacher_id INTEGER NOT NULL)""")

    cur.execute("SELECT COUNT (*) FROM courses")
    if cur.fetchall()[0][0] == 0:
        cur.execute("""INSERT INTO courses(course_name, teacher_id)
              VALUES('Data Bases', 1),
              ('Object Programming', 2);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS student_course_connection
                (student_id INTEGER NOT NULL, 
                course_id INTEGER NOT NULL,
                grade INTEGER,
                CONSTRAINT uc_ssc UNIQUE (student_id, course_id))""")

    cur.execute("SELECT COUNT (*) FROM student_course_connection")
    if cur.fetchall()[0][0] == 0:
        cur.execute("""INSERT INTO student_course_connection(student_id, course_id, grade)
              VALUES(1, 1, 7),
              (1, 2, 9);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS teachers
                    (teacher_id SERIAL PRIMARY KEY, 
                    first_name TEXT NOT NULL, 
                    last_name TEXT NOT NULL, 
                    hiring_date DATE NOT NULL,
                    course_id INTEGER NOT NULL)""")

    cur.execute("SELECT COUNT (*) FROM teachers")
    if cur.fetchall()[0][0] == 0:
        cur.execute("""INSERT INTO teachers(first_name,last_name, hiring_date, course_id)
              VALUES('Miodrag', 'Draganovic', '2000-03-03', 2),
              ('Aleksandra', 'Kovacevic', '2010-02-15', 1);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS course_lecture_connection
                (course_id INTEGER NOT NULL,
                lecture_id INTEGER NOT NULL,
                time_held TIMESTAMP,
                CONSTRAINT uc_clc UNIQUE (course_id, lecture_id))""")

    cur.execute("SELECT COUNT (*) FROM course_lecture_connection")
    if cur.fetchall()[0][0] == 0:
        cur.execute("""INSERT INTO course_lecture_connection(course_id, lecture_id, time_held)
              VALUES(1, 1, '2021-09-14 12:30:00'),
              (2, 2, '2021-09-17 15:30:00');""")

    conn.commit()
    conn.close()


def create_connection():
    conn = psy.connect(dbname=DB_NAME, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    return conn, cur


app = Flask(__name__)


@app.route('/students')
def students():
    conn, cur = create_connection()
    cur.execute("SELECT row_to_json (students) FROM students")
    temp = cur.fetchall()
    return jsonify(temp)


@app.route('/lectures')
def lectures():
    conn, cur = create_connection()
    cur.execute("SELECT row_to_json (lectures) FROM lectures")
    temp = cur.fetchall()
    return jsonify(temp)


@app.route('/courses')
def courses():
    conn, cur = create_connection()
    cur.execute("SELECT row_to_json (courses) FROM courses")
    temp = cur.fetchall()
    return jsonify(temp)





if __name__ == '__main__':

    create_tables()
    app.run()
