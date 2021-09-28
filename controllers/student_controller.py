from flask import request, jsonify
from models import student_model
from backend_logic import create_connection
from controllers import lecture_controller
from controllers import course_controller

# Extracts data from students database and returns it as a dictionary
def students():
    sql = "SELECT * FROM students"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2,
                            column_names[3]: col3, column_names[4]: col4} for
                           (col0, col1, col2, col3, col4) in cur.fetchall()]
    '''rep = student_model.Student(result_list_of_dict[0])
    print(rep.first_name)'''
    conn.close()
    return jsonify(result_list_of_dict)

def s_c_connection():
    sql = "SELECT * FROM student_course_connection"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2} for
                           (col0, col1, col2) in cur.fetchall()]
    conn.close()
    return jsonify(result_list_of_dict)


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


def attending_lectures(student_id):
    new_dict = []
    returning_dict = []
    lecture = lecture_controller.lectures()
    connection = s_l_connection()

    for temp in connection:
        if temp['student_id'] == int(student_id):
            new_dict.append(temp)

    for temp in lecture.json:
        for i in new_dict:
            if i['lecture_id'] == temp['lecture_id']:
                returning_dict.append(temp)

    return jsonify(returning_dict)

def average_grade(student_id):
    courses = s_c_connection()
    grade = 0
    grades = 0
    for course in courses.json:
        if course['student_id'] == int(student_id):
            grades += 1
            grade += course['grade']
    average = grade / grades
    return f"The selected student's average grade is {average}"


def course_grade(student_id, course_id):
    grade = request.get_json()
    course = s_c_connection()
    sql = """INSERT INTO student_course_connection (student_id, course_id, grade)
                        VALUES({}, {}, {})""".format(student_id, course_id, grade['grade'])
    for pom in course.json:
        if pom['student_id'] == int(student_id) and pom['course_id'] == int(course_id):
            return f"The selected student already has their grade marked for this course, " \
                   f"their grade is: {pom['grade']}"

    conn, cur = create_connection()
    cur.execute(sql)
    conn.commit()
    conn.close()
    return "Grade marked"

