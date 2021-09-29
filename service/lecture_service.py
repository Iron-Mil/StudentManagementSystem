from repo import lecture_repo
from repo.student_repo import student_lecture_connection, students


def list_of_lectures():
    return lecture_repo.lectures()


def students_attending_given_lecture(lecture_id):
    new_dict = []
    returning_dict = []
    connection = student_lecture_connection('lecture_id', lecture_id)
    student = students()
    for temp in connection:
        if temp['lecture_id'] == int(lecture_id):
            new_dict.append(temp)

    for temp in student:
        for i in new_dict:
            if i['student_id'] == temp['student_id']:
                returning_dict.append(temp)

    return returning_dict