import psycopg2
from psycopg2 import errors

from backend_logic import execute_sql, create_connection


def create(student):
    sql = """INSERT INTO students (first_name, last_name, year_studying, date_of_birth)
                Values({}, {}, {}, {});""".format(student['first_name'], student['last_name'],
                                                  student['year_studying'], student['date_of_birth'])
    execute_sql(sql)


# Returns the entire students table
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


# Returns a single student whose primary key matches the given value
def student(student_id):
    sql = "SELECT * FROM students WHERE student_id = {}".format(student_id)
    conn, cur = create_connection()
    cur.execute(sql)
    temp = cur.fetchall()
    description = cur.description
    column_names = [col[0] for col in description]
    return dict(zip(column_names, temp[0]))


def student_lecture_connection(key, value):
    if key == 'student_id':
        sql = "SELECT * FROM student_lecture_connection WHERE student_id = {}".format(value)
    elif key == 'lecture_id':
        sql = "SELECT * FROM student_lecture_connection WHERE lecture_id = {}".format(value)
    else:
        print("Wrong key value for s_l_connection table")
        return

    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1} for
                           (col0, col1) in cur.fetchall()]
    conn.close()
    return result_list_of_dict


def student_course_connection(key, value):
    if key == 'student_id':
        sql = "SELECT * FROM student_course_connection WHERE student_id = {}".format(value)
    elif key == 'course_id':
        sql = "SELECT * FROM student_course_connection WHERE course_id = {}".format(value)
    else:
        print("Wrong key value for s_c_connection table")
        return

    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2} for
                           (col0, col1, col2) in cur.fetchall()]
    conn.close()
    return result_list_of_dict


def create_s_l_connection(connection):
    sql = """INSERT INTO student_lecture_connection (student_id, lecture_id)
                Values({}, {});""".format(connection['student_id'], connection['lecture_id'])
    try:
        execute_sql(sql)
    except psycopg2.errors.UniqueViolation:
        print("this combination already exists")


def create_s_c_connection(connection):
    sql = """INSERT INTO student_course_connection (student_id, course_id, grade)
                Values({}, {}, {});""".format(connection['student_id'], connection['course_id'], connection['grade'])
    try:
        execute_sql(sql)
    except psycopg2.errors.UniqueViolation:
        print("this combination already exists")
