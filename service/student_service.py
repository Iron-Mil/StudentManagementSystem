import backend_logic
from repo import student_repo


def list_of_students():
    return student_repo.students()


def average_grade(student_id):
    grade = 0
    grades = 0
    course = student_repo.student_course_connection('student_id', student_id)
    for temp in course:
        grades += 1
        grade += temp['grade']
    average = grade / grades
    return f"The selected student's average grade is {average}"


def students_attending_given_lecture(lecture_id):
    new_dict = []
    returning_dict = []
    connection = student_repo.student_lecture_connection('lecture_id', lecture_id)
    student = student_repo.students()
    for temp in connection:
        if temp['lecture_id'] == int(lecture_id):
            new_dict.append(temp)

    for temp in student:
        for i in new_dict:
            if i['student_id'] == temp['student_id']:
                returning_dict.append(temp)

    return returning_dict


def mark_grade(student_id, course_id, grade):
    course = student_repo.student_course_connection('student_id', student_id)
    sql = """INSERT INTO student_course_connection (student_id, course_id, grade)
                        VALUES({}, {}, {})""".format(student_id, course_id, grade['grade'])
    for pom in course:
        if pom['student_id'] == int(student_id) and pom['course_id'] == int(course_id):
            return f"The selected student already has their grade marked for this course, " \
                   f"their grade is: {pom['grade']}"

    backend_logic.execute_sql(sql)
    return "Grade marked"
