from repo import course_repo, student_repo


def list_of_courses():
    return course_repo.courses()


def list_of_average_grades():
    grade_list = []
    test = course_repo.read_averages()
    for temp in test:
        grade_list.append(temp[1])

    number_of_grades = 0
    sum_of_grades = 0

    for student in student_repo.students():
        pom = student['student_id']
        lista = student_repo.student_course_connection('student_id', pom)
        for item in lista:
            number_of_grades += 1
            sum_of_grades += item['grade']
    average_grade = sum_of_grades / number_of_grades
    grade_list.append(round(average_grade, 3))

    if len(grade_list) > 5:
        del grade_list[0]

    print("Currently saved grade averages are: ")
    print(grade_list)
    print()


    # Clears the old order and saves the new one in its place
    course_repo.delete_averages()
    course_repo.save_averages(grade_list)
