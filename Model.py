import backend_logic


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
