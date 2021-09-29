from flask import Blueprint

from controllers.course_controller import courses

course_bp = Blueprint('course_bp', __name__)

course_bp.route('/', methods=['GET'])(courses)
