from service import course_service
from flask import jsonify


def courses():
    return jsonify(course_service.list_of_courses())


def average_grades():
    course_service.updating_average_grades()


def showing_saved_averages():
    return course_service.showing_saved_averages()
