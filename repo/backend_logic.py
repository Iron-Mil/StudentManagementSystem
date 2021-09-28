import psycopg2 as psy
from constants import *


def create_connection():
    conn = psy.connect(dbname=DB_NAME, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    return conn, cur


# Initial table setup and filling if they don't exist already
def create_tables():
    conn, cur = create_connection()
    cur.execute(open('repo/initial_setup.sql', 'r').read())
    conn.commit()
    conn.close()


# Fetches a table we request, and returns the data within, used for /students, /lectures, and /courses
def fetch_table(table):
    conn, cur = create_connection()
    sql = "SELECT * FROM {}".format(table)
    cur.execute(sql)
    temp = cur.fetchall()
    print(temp)
    print((temp[0]))
    conn.close()
    return temp

def students():
    sql = "SELECT * FROM students"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2,
                            column_names[3]: col3, column_names[4]: col4} for
                           (col0, col1, col2, col3, col4) in cur.fetchall()]
    conn.close()
    return result_list_of_dict

def lectures():
    sql = "SELECT * FROM lectures"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2,
                            column_names[3]: col3} for
                           (col0, col1, col2, col3) in cur.fetchall()]
    conn.close()
    return result_list_of_dict

def s_c_connection():
    sql = "SELECT * FROM student_course_connection"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2} for
                           (col0, col1, col2) in cur.fetchall()]
    conn.close()
    return result_list_of_dict

def s_l_connection():
    sql = "SELECT * FROM student_lecture_connection"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1} for
                           (col0, col1) in cur.fetchall()]
    conn.close()
    return result_list_of_dict

def attending_lectures(student_id, lecture):
    new_dict = []
    returning_dict = []
    connection = s_l_connection()
    for temp in connection:
        if temp['student_id'] == int(student_id):
            new_dict.append(temp)

    for temp in lecture:
        for i in new_dict:
            if i['lecture_id'] == temp['lecture_id']:
                returning_dict.append(temp)

    return returning_dict

def average_grade(student_id, courses):
    grade = 0
    grades = 0
    for course in courses:
        if course['student_id'] == int(student_id):
            grades += 1
            grade += course['grade']
    average = grade / grades
    return f"The selected student's average grade is {average}"

def course_grade(student_id, course_id, grade):
    course = s_c_connection()
    sql = """INSERT INTO student_course_connection (student_id, course_id, grade)
                        VALUES({}, {}, {})""".format(student_id, course_id, grade['grade'])
    for pom in course:
        if pom['student_id'] == int(student_id) and pom['course_id'] == int(course_id):
            return f"The selected student already has their grade marked for this course, " \
                   f"their grade is: {pom['grade']}"

    conn, cur = create_connection()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return "Grade marked"

def courses():
    sql = "SELECT * FROM courses"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2} for
                           (col0, col1, col2) in cur.fetchall()]
    conn.close()
    return result_list_of_dict

def attending_students(lecture_id, student):
    new_dict = []
    returning_dict = []
    connection = s_l_connection()
    for temp in connection:
        if temp['lecture_id'] == int(lecture_id):
            new_dict.append(temp)

    for temp in student:
        for i in new_dict:
            if i['student_id'] == temp['student_id']:
                returning_dict.append(temp)

    return returning_dict
