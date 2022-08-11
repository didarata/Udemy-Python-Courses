import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='3461',
    port='3306',
    database='testdb'
)

# Creating database!
# mycursor= mydb.cursor()
# mycursor.execute("CREATE DATABASE testdb")

# Checking if database is created and what other databases we have.
# mycursor= mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# Creating a table
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# Checking if table is created and what other tables we have.
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
