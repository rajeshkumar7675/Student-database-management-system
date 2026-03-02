import sqlite3

# ---------------- Database Connection ----------------
def connect_db():
    return sqlite3.connect("students.db")

# ---------------- Create Table ----------------
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            email TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

# ---------------- Add Student ----------------
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    email = input("Enter email: ")

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
            (name, age, course, email)
        )
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Email already exists!")
    conn.close()

# ---------------- View Students ----------------
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nID | Name | Age | Course | Email")
    print("-" * 40)
    for row in rows:
        print(row)

    conn.close()

# ---------------- Update Student ----------------
def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("New name: ")
    age = int(input("New age: "))
    course = input("New course: ")
    email = input("New email: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?, email=?
        WHERE id=?
    """, (name, age, course, email, student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found!")

    conn.close()

# ---------------- Delete Student ----------------
def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found!")

    conn.close()

# ---------------- Menu ----------------
def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

# ---------------- Main Program ----------------
def main():
    create_table()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
