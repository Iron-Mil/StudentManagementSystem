from repo import lecture_repo
from repo.student_repo import student_lecture_connection


def list_of_lectures():
    return lecture_repo.lectures()


def lectures_student_is_attending(student_id):
    new_dict = []
    returning_dict = []
    connection = student_lecture_connection('student_id', student_id)
    lecture = lecture_repo.lectures()
    for temp in connection:
        if temp['student_id'] == int(student_id):
            new_dict.append(temp)

    for temp in lecture:
        for i in new_dict:
            if i['lecture_id'] == temp['lecture_id']:
                returning_dict.append(temp)

    return returning_dict
