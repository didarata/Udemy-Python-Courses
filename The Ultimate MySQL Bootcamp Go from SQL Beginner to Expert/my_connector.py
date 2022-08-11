import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql3461',
    port='3306',
    # database='python_test'
)


mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM users')

users = mycursor.fetchall()

for user in users:
    print(f"id: {user[0]}, Username: {user[1]}, Password: {user[2]}")
    print(f'{"-" * len(users)}' * 17)
