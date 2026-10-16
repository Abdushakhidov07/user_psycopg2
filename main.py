from service import *
from connection import *
import asyncio
import time


async def main():
    await create_table()
    while True:
        n = int(input("1)create user\n2)get users\nChouse one: "))
        match n:
            case 1:
                await add_user(input("Enter your Full name: "), int(input("Enter your age: ")), input("Enter your email: "))
            case 2:
                users = await get_user()
                for user in users:
                    print(f"""
    id:{user["user_id"]}
    Fullname:{user["full_name"]}
    Age:{user["age"]}
    Email:{user["email"]}
                        """)
            case _:
                break
                        


if __name__ == "__main__":
    asyncio.run(main())
