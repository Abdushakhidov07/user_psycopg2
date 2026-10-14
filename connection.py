from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

password_db = os.getenv("PASSWORD_DB")


def connection():
    try:
        conn = psycopg2.connect(
                port = 5432,
                host = "localhost",                       
                user = "postgres",
                database = "task2_db",
                password = password_db
        )
    except Exception as error:
        print(f"Connection error: {error}")
    finally:
        return conn
        




def create_table():
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id serial primary key,
            full_name varchar(100) not null,
            age int check(age >= 18),
            email varchar(100) unique,
            is_active boolean default true,
            created_at timestamp default now()
        )                
                    """)
        print("Created sucsses")
    except Exception as error:
        print(f"Create table error: {error}")
    finally:
        conn.commit()
        

