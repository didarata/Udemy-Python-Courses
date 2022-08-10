import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='3461',
    port='3306',
)

# mycursor= mydb.cursor()
# mycursor.execute("CREATE DATABASE testdb")

mycursor= mydb.cursor()
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)
