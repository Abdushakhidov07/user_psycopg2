from connection import *

def add_user(full_name, age, email):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO users(full_name, age, email) VALUES
        (%s, %s, %s)  
            """, (full_name, age, email,))
        print("User added")
    except Exception as error:
        print(f"Add user error: {error}") 
    finally:
        cur.close()
        conn.commit()      
        
        
def get_user():
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("""
        select * from users
            """)
        users = cur.fetchall()
        return users
    except Exception as error:
        print(f"Get user error: {error}") 
    finally:
        cur.close()
        conn.commit()      
        