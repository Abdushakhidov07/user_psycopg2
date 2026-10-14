from service import *
from connection import *

create_table()
while True:
    n = int(input("1)create user\n2)get users\nChouse one: "))
    match n:
        case 1:
            add_user(input("Enter your Full name: "), int(input("Enter your age: ")), input("Enter your email: "))
        case 2:
            users = get_user()
            for user in users:
                print(f"""
id:{user[0]}
Fullname:{user[1]}
Age:{user[2]}
Email:{user[3]}
                      """)
        case _:
            break
                    