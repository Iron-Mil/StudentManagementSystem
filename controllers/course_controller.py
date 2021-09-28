from repo import backend_logic
from flask import jsonify


def courses():
    return jsonify(backend_logic.courses())
