from flask import request, jsonify
from service import student_service, lecture_service


def students():
    return jsonify(student_service.list_of_students())


def attending_lectures(student_id):
    return jsonify(lecture_service.lectures_student_is_attending(student_id))


def average_grade(student_id):
    return student_service.average_grade(student_id)


def course_grade(student_id, course_id):
    return student_service.mark_grade(student_id, course_id, request.get_json())
