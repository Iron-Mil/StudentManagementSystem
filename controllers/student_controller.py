from flask import request, jsonify
from repo import backend_logic

# Extracts data from students database and returns it as a dictionary
def students():
    return jsonify(backend_logic.students())

def s_c_connection():
    return jsonify(backend_logic.s_c_connection())

def s_l_connection():
    return jsonify(backend_logic.s_l_connection())

def attending_lectures(student_id):
    return jsonify(backend_logic.attending_lectures(student_id, backend_logic.lectures()))

def average_grade(student_id):
    return backend_logic.average_grade(student_id, backend_logic.s_c_connection())

def course_grade(student_id, course_id):
    return backend_logic.course_grade(student_id, course_id, request.get_json())
