import psycopg2


def connect(conn=None):
    return psycopg2.connect(
        host="localhost",
        database="lalana",
        user="postgres",
        password="")
