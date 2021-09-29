from repo import course_repo
from flask import jsonify


def courses():
    return jsonify(course_repo.courses())
