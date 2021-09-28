from repo import backend_logic
from flask import jsonify


def lectures():
    return jsonify(backend_logic.lectures())

def attending_students(lecture_id):
    return jsonify(backend_logic.attending_students(lecture_id, backend_logic.students()))
