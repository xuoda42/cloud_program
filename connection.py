import psycopg2

conn = psycopg2.connect("""
    host=<хост>
    port=6432
    sslmode=verify-full
    dbname=db1
    user=user1
    password=<пароль от базы>
    target_session_attrs=read-write
""")


def get_cursor_columns(cursor):
    return [column[0] for column in cursor.description]


def get_elements_as_dict(cursor):
    columns = get_cursor_columns(cursor)
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    return results


def close_db():
    conn.close()
