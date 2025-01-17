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

mycursor = mydb.cursor()

name = input("Enter your name: ")
id = input("Enter your id: ")

mycursor.execute("CREATE TABLE IF NOT EXISTS worker (id INT, name VARCHAR(255))")
mycursor.execute("INSERT INTO worker (id, name) VALUES (%s, %s)", (id, name))

mycursor.execute("SELECT * FROM worker")

workers = mycursor.fetchall()

for worker in workers:
    print(worker)

print("Table created and record inserted successfully.")

mydb.commit()
mycursor.close()
mydb.close()
