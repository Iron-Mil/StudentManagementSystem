from flask import Blueprint

from controllers.lecture_controller import lectures, attending_students

lecture_bp = Blueprint('lecture_bp', __name__)

lecture_bp.route('/', methods=['GET'])(lectures)
lecture_bp.route('/<lecture_id>/attending_students', methods=['GET'])(attending_students)
