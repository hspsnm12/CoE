import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="test"
)

if mydb.is_connected():
    print("Successfully connected to the database!")
else:
    print("Failed to connect.")


mydb.commit()
mycursor.close()
mydb.close()
