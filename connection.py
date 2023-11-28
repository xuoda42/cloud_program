import psycopg2

# conn = psycopg2.connect("""
#     host=rc1b-1axp7jy9wejutqav.mdb.yandexcloud.net
#     port=6432
#     sslmode=verify-full
#     dbname=db1
#     user=user1
#     password=152jojo152
#     target_session_attrs=read-write
# """)

conn2 = psycopg2.connect("host=185.86.145.31 dbname=PostgreSQL-2483 user=user password=7M3YHV7+RA2Gh8373")


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
