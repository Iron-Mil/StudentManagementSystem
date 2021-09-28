from backend_logic import create_connection
from flask import jsonify

def courses():
    sql = "SELECT * FROM courses"
    conn, cur = create_connection()
    cur.execute(sql)
    description = cur.description
    column_names = [col[0] for col in description]
    result_list_of_dict = [{column_names[0]: col0, column_names[1]: col1, column_names[2]: col2} for
                           (col0, col1, col2) in cur.fetchall()]
    conn.close()
    return jsonify(result_list_of_dict)
