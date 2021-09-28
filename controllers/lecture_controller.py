from backend_logic import create_connection
from controllers import student_controller
from flask import jsonify

def lectures():
    sql = "SELECT * FROM lectures"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2,
                            column_names[3]: col3} for
                           (col0, col1, col2, col3) in cur.fetchall()]
    conn.close()
    return jsonify(result_list_of_dict)

def attending_students(lecture_id):
    new_dict = []
    returning_dict = []
    student = student_controller.students()
    connection = student_controller.s_l_connection()

    for temp in connection:
        if temp['lecture_id'] == int(lecture_id):
            new_dict.append(temp)

    for temp in student.json:
        for i in new_dict:
            if i['student_id'] == temp['student_id']:
                returning_dict.append(temp)

    return jsonify(returning_dict)
