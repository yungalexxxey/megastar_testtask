import psycopg2
import os

from tools.config_parser import DB_PORT, DB_NAME, DB_PASS, DB_HOST, DB_USER
from psycopg2.errors import DuplicateTable


def init_sql():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    cursor = conn.cursor()

    with open(os.path.abspath('./service/db/init/init.sql')) as f:
        try:
            cursor.execute(f.read())
        except DuplicateTable:
            print("Already initialized. Starting service...")
            return
    conn.commit()
    cursor.close()
    conn.close()
