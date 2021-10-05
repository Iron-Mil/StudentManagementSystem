from flask import Blueprint

from controllers.course_controller import courses, showing_saved_averages

course_bp = Blueprint('course_bp', __name__)

course_bp.route('/', methods=['GET'])(courses)
course_bp.route('/average_grades', methods=['GET'])(showing_saved_averages)
