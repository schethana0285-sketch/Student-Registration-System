import csv
import os

from validator import validate_contact
from loader import load_students
from analytics import generate_report


# Load existing student records
def get_students():

    if os.path.exists("students_clean.csv"):

        with open("students_clean.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    return load_students()


# Save student records
def save_students(students):

    with open("students_clean.csv", "w", newline="") as file:

        fields = ["name", "phone", "email"]

        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(students)


# Display all students
def view_students(students):

    print("\n===== ALL REGISTERED STUDENTS =====")

    if not students:
        print("No student records found.")
        return

    print("-" * 65)
    print("ID   NAME                 PHONE        EMAIL")
    print("-" * 65)

    for i, student in enumerate(students, start=1):

        print(i, student["name"],
              student["phone"], student["email"])

    print("-" * 65)


# Search student
def search_student(students):

    value = input("Enter name, phone or email to search: ").strip().lower()

    found = False

    for i, student in enumerate(students, start=1):

        if (value in student["name"].lower()
            or value == student["phone"]
            or value == student["email"].lower()):

            print("\nStudent ID:", i)
            print("Name:", student["name"])
            print("Phone:", student["phone"])
            print("Email:", student["email"])

            found = True

    if not found:
        print("Student not found.")


# Register new student
def register_student(students):

    name = input("Enter student name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    is_valid, reason = validate_contact(name, phone, email)

    if not is_valid:
        print("Registration failed:", reason)
        return

    for student in students:

        if phone == student["phone"]:
            print("Phone number already exists.")
            return

        if email.lower() == student["email"].lower():
            print("Email already exists.")
            return

    student = {
        "name": name,
        "phone": phone,
        "email": email
    }

    students.append(student)

    save_students(students)

    print("Student registered successfully!")


# Update student
def update_student(students):

    try:
        student_id = int(input("Enter student ID to update: "))

        if student_id < 1 or student_id > len(students):
            print("Invalid student ID.")
            return

        student = students[student_id - 1]

        name = input("Enter new name: ").strip()
        phone = input("Enter new phone: ").strip()
        email = input("Enter new email: ").strip()

        is_valid, reason = validate_contact(name, phone, email)

        if not is_valid:
            print("Update failed:", reason)
            return

        for i, other in enumerate(students):

            if i != student_id - 1:

                if phone == other["phone"]:
                    print("Phone number already exists.")
                    return

                if email.lower() == other["email"].lower():
                    print("Email already exists.")
                    return

        student["name"] = name
        student["phone"] = phone
        student["email"] = email

        save_students(students)

        print("Student updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Delete student
def delete_student(students):

    try:
        student_id = int(input("Enter student ID to delete: "))

        if student_id < 1 or student_id > len(students):
            print("Invalid student ID.")
            return

        deleted = students.pop(student_id - 1)

        save_students(students)

        print(deleted["name"], "deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def main():

    students = get_students()

    while True:

        print("\n================================")
        print(" STUDENT REGISTRATION SYSTEM")
        print("================================")

        print("1. View All Students")
        print("2. Search Student")
        print("3. Register Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Analytics Report")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            view_students(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            register_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            save_students(students)
            generate_report()

        elif choice == "7":
            save_students(students)
            print("Thank you for using Student Registration System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()