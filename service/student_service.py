import backend_logic
from repo import student_repo
from repo.lecture_repo import lectures


def list_of_students():
    return student_repo.students()


def lectures_student_is_attending(student_id):
    new_dict = []
    returning_dict = []
    connection = student_repo.student_lecture_connection('student_id', student_id)
    lecture = lectures()
    for temp in connection:
        if temp['student_id'] == int(student_id):
            new_dict.append(temp)

    for temp in lecture:
        for i in new_dict:
            if i['lecture_id'] == temp['lecture_id']:
                returning_dict.append(temp)

    return returning_dict


def average_grade(student_id):
    grade = 0
    grades = 0
    course = student_repo.student_course_connection('student_id', student_id)
    print(course)
    for temp in course:
        grades += 1
        grade += temp['grade']
    average = grade / grades
    return f"The selected student's average grade is {average}"


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
