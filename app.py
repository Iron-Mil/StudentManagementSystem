import backend_logic
from flask import Flask
from flask import jsonify
from controllers import student_controller, lecture_controller, course_controller
from blueprints import student_blueprint, lecture_blueprint, course_blueprint


app = Flask(__name__)
app.register_blueprint(student_blueprint.student_bp, url_prefix='/students')
app.register_blueprint(lecture_blueprint.lecture_bp, url_prefix='/lectures')
app.register_blueprint(course_blueprint.course_bp, url_prefix='/courses')


@student_blueprint.student_bp.route('/')
def students():
    return jsonify(student_controller.students())

@lecture_blueprint.lecture_bp.route('/')
def lectures():
    return jsonify(lecture_controller.lectures())

@course_blueprint.course_bp.route('/')
def courses():
    return jsonify(course_controller.courses())

@lecture_blueprint.lecture_bp.route('/<lecture_id>/attending_students')
def attending_students(lecture_id):
    return jsonify(lecture_controller.attending_students(lecture_id))

@student_blueprint.student_bp.route('<student_id>/attending_lectures')
def attending_lectures(student_id):
    return jsonify(student_controller.attending_lectures(student_id))

@student_blueprint.student_bp.route('/<student_id>/courses/<course_id>', methods=['POST'])
def course_grade(student_id, course_id):
    return student_controller.course_grade(student_id, course_id)

@student_blueprint.student_bp.route('<student_id>/average_grade')
def average_grade(student_id):
    return student_controller.average_grade(student_id)


if __name__ == '__main__':
    backend_logic.create_tables()
    app.run()
