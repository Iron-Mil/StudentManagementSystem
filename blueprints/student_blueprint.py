from flask import Blueprint

from controllers.student_controller import students, s_c_connection, \
    s_l_connection, average_grade, course_grade, attending_lectures

student_bp = Blueprint('student_bp', __name__)

student_bp.route('/', methods=['GET'])(students)
student_bp.route('/<student_id>', methods=['GET'])(s_c_connection)
student_bp.route('/<student_id>', methods=['GET'])(s_l_connection)
student_bp.route('/<student_id>/average_grade', methods=['GET'])(average_grade)
student_bp.route('/<student_id>/attending_lectures', methods=['GET'])(attending_lectures)
student_bp.route('/<student_id>/courses/<course_id>', methods=['POST'])(course_grade)

