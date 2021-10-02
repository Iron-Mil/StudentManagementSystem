from backend_logic import execute_sql, create_connection


def create(course):
    sql = """INSERT INTO courses (course_name, teacher_id)
                Values({}, {});""".format(course['course_name'], course['teacher_id'])
    execute_sql(sql)


def courses():
    sql = "SELECT * FROM courses"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2} for
                           (col0, col1, col2) in cur.fetchall()]
    conn.close()
    return result_list_of_dict


def course(course_id):
    sql = "SELECT * FROM courses WHERE course_id = {}".format(course_id)
    conn, cur = create_connection()
    cur.execute(sql)
    temp = cur.fetchall()
    description = cur.description
    column_names = [col[0] for col in description]
    return dict(zip(column_names, temp[0]))


def read_averages():
    sql = "SELECT * FROM average_grade_storage"
    conn, cur = create_connection()
    cur.execute(sql)
    averages = cur.fetchall()
    conn.close()
    return averages

def delete_averages():
    sql = "TRUNCATE average_grade_storage;"
    # sql = "DELETE FROM average_grade_storage WHERE id = 1"

    execute_sql(sql)


# If a non-fixed amount of grades needs saving
def save_averages(list_of_averages):
    sql = """INSERT INTO average_grade_storage (id, grade) \
          Values({}, {})"""
    conn, cur = create_connection()
    counter = 1
    for average in list_of_averages:
        cur.execute(sql.format(counter, average))
        counter += 1
    conn.commit()
    conn.close()
