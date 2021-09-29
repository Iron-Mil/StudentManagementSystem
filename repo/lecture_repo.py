from backend_logic import create_connection, execute_sql


def create(lecture):
    sql = """INSERT INTO students (first_name, last_name, year_studying, date_of_birth)
                Values({}, {}, {});""".format(lecture['teacher'], lecture['course'], lecture['required'])
    execute_sql(sql)


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
    return result_list_of_dict


def lecture(lecture_id):
    sql = "SELECT * FROM lectures WHERE lecture_id = {}".format(lecture_id)
    conn, cur = create_connection()
    cur.execute(sql)
    temp = cur.fetchall()
    description = cur.description
    column_names = [col[0] for col in description]
    return dict(zip(column_names, temp[0]))
