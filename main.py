import backend_logic
from flask import Flask
from flask import jsonify


class Model(object):
    def fetch_table(table):
        return backend_logic.fetch_table(table)

    def average_grade(self, student_id):
        return backend_logic.average_grade(student_id)

    def attending_students(self, lecture_id):
        return backend_logic.attending_students(lecture_id)

    def attending_lectures(self, student_id):
        return backend_logic.attending_lectures(student_id)

    def course_grade(self, student_id, course_id):
        return backend_logic.course_grade(student_id, course_id)


class Controller(object):

    def __init__(self, model):
        self.model = model

    def students(self):
        return jsonify(self.model.fetch_table("students"))

    def lectures(self):
        return jsonify(self.model.fetch_table("lectures"))

    def courses(self):
        return jsonify(self.model.fetch_table("courses"))

    def attending_students(self, lecture_id):
        return jsonify(self.model.attending_students(self, lecture_id))

    def attending_lectures(self, student_id):
        return jsonify(self.model.attending_lectures(self, student_id))

    def course_grade(self, student_id, course_id):
        return jsonify(self.model.course_grade(self, student_id, course_id))

    def average_grade(self, student_id):
        temp = self.model.average_grade(self, student_id)
        return temp


app = Flask(__name__)

@app.route('/students')
def students():
    return c.students()

@app.route('/lectures')
def lectures():
    return c.lectures()

@app.route('/courses')
def courses():
    return c.courses()

@app.route('/lectures/<lecture_id>/attending_students')
def attending_students(lecture_id):
    return c.attending_students(lecture_id)

@app.route('/students/<student_id>/attending_lectures')
def attending_lectures(student_id):
    return c.attending_lectures(student_id)

@app.route('/students/<student_id>/courses/<course_id>', methods=['POST'])
def course_grade(student_id, course_id):
    return c.course_grade(student_id, course_id)

@app.route('/students/<student_id>/average_grade')
def average_grade(student_id):
    return c.average_grade(student_id)


if __name__ == '__main__':
    c = Controller(Model)
    backend_logic.create_tables()
    app.run()
