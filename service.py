from connection import *
import asyncio

async def add_user(full_name, age, email):
    try:
        conn = await connection()
        await conn.execute("""
        INSERT INTO users(full_name, age, email) VALUES
        ($1, $2, $3)  
            """, full_name, age, email)
        print("User added")
    except Exception as error:
        print(f"Add user error: {error}") 
    finally:
        await conn.close()
        
            
async def get_user():
    try:
        conn = await connection()
        users = await conn.fetch("""
        select * from users
            """)
        return users
    except Exception as error:
        print(f"Get user error: {error}") 
    finally:
        await conn.close()
        