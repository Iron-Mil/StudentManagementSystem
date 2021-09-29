from flask import jsonify
from service import lecture_service, student_service


def lectures():
    return jsonify(lecture_service.list_of_lectures())


def attending_students(lecture_id):
    return jsonify(student_service.students_attending_given_lecture(lecture_id))
