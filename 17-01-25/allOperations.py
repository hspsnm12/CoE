#insert student details
#delete student details by student id
# update student details
#display all the students
#display all the students asc order based on name
#display all the students whose score btwn 70-90
# display students whose city is hyderabad
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
mycursor.execute('''
CREATE TABLE IF NOT EXISTS workers (
    worker_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    score INT,
    city VARCHAR(100)
)
''')
def insert_worker():
    worker_id = int(input("Enter worker ID: "))
    name = input("Enter name: ")

    while True:
        try:
            score = int(input("Enter score: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for score.")

    city = input("Enter city: ")

    mycursor.execute("INSERT INTO workers (worker_id, name, score, city) VALUES (%s, %s, %s, %s)",
                     (worker_id, name, score, city))
    print(f"Worker {name} added successfully.")
def update_worker():
    worker_id = int(input("Enter worker ID to update: "))
    name = input("Enter new name: ")
    score = int(input("Enter new score: "))
    city = input("Enter new city: ")

    mycursor.execute("UPDATE workers SET name = %s, score = %s, city = %s WHERE worker_id = %s",
                     (name, score, city, worker_id))
    print(f"Worker with ID {worker_id} updated successfully.")
def delete_worker():
    worker_id = int(input("Enter worker ID to delete: "))
    mycursor.execute("DELETE FROM workers WHERE worker_id = %s", (worker_id,))
    print(f"Worker with ID {worker_id} deleted successfully.")
def display_workers():
    mycursor.execute("SELECT * FROM workers")
    rows = mycursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Insert a new worker")
        print("2. Update an existing worker")
        print("3. Delete a worker")
        print("4. Display all workers")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            insert_worker()
        elif choice == "2":
            update_worker()
        elif choice == "3":
            delete_worker()
        elif choice == "4":
            display_workers()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
mydb.commit()
mycursor.close()
mydb.close()
