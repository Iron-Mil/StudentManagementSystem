import psycopg2 as psy
from constants import *


def create_connection():
    conn = psy.connect(dbname=DB_NAME, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
    cur = conn.cursor()
    return conn, cur


# Initial table setup and filling if they don't exist already
def create_tables():
    conn, cur = create_connection()
    cur.execute(open('initial_setup.sql', 'r').read())
    conn.commit()
    conn.close()


def execute_sql(sql):
    conn, cur = create_connection()
    cur.execute(sql)
    conn.commit()
    conn.close()
