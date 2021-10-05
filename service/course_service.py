from repo import course_repo, student_repo


def list_of_courses():
    return course_repo.courses()


def updating_average_grades():
    number_of_grades = 0
    sum_of_grades = 0

    for student in student_repo.students():
        pom = student['student_id']
        lista = student_repo.student_course_connection('student_id', pom)
        for item in lista:
            number_of_grades += 1
            sum_of_grades += item['grade']

    grade_list = [sum_of_grades / number_of_grades]
    course_repo.save_averages(grade_list)

    grade_list = course_repo.read_averages()
    if len(grade_list) > 5:
        course_repo.delete_oldest_average()


def showing_saved_averages():
    grade_list = course_repo.read_averages()
    message = "Currently saved grades are: \n \n"
    for grade in grade_list:
        message = message + "Average grade {:.3f} saved at:".format(grade[0]) + str(grade[1]) + "\n"
    return message
