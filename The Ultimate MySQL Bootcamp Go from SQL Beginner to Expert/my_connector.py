import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='3461',
    port='3306',
    database='baba'
)


# mycursor = mydb.cursor()
#
# mycursor.execute('SELECT * FROM users')
#
# users = mycursor.fetchall()
#
# for user in users:
#     print('Username ' + user[1])
#     print('Password ' + user[2])