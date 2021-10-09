import psycopg2 as psy
from constants import *
from functools import lru_cache, wraps
from datetime import datetime, timedelta


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


def timed_lru_cache(refresh_rate: int, cache_size: int = 32):

    def wrapper_cache(func):
        func = lru_cache(maxsize=cache_size)(func)
        func.lifetime = timedelta(minutes=refresh_rate)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)
        return wrapped_func
    return wrapper_cache
