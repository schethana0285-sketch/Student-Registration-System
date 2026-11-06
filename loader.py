import csv
from validator import validate_contact


def load_students():

    students = []
    seen_phones = set()
    seen_emails = set()

    total_rows = 0
    rejected = 0

    print("\n===== STUDENT DATA LOADING =====")

    # Read the input CSV file
    with open("contacts.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            total_rows += 1

            name = row["name"]
            phone = row["phone"]
            email = row["email"]

            # Validate student details
            is_valid, reason = validate_contact(name, phone, email)

            if not is_valid:
                rejected += 1
                print("Rejected:", name, "-", reason)
                continue

            # Check duplicate phone number
            if phone in seen_phones:
                rejected += 1
                print("Rejected:", name, "- Duplicate phone number")
                continue

            # Check duplicate email
            if email in seen_emails:
                rejected += 1
                print("Rejected:", name, "- Duplicate email")
                continue

            # Store valid student details
            student = {
                "name": name.strip(),
                "phone": phone,
                "email": email
            }

            students.append(student)

            seen_phones.add(phone)
            seen_emails.add(email)

            print("Accepted:", name)

    # Save clean records into another CSV file
    with open("students_clean.csv", "w", newline="") as file:

        fieldnames = ["name", "phone", "email"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

    # Display final report
    print("\n===== INGESTION SUMMARY =====")
    print("Total rows read:", total_rows)
    print("Valid rows accepted:", len(students))
    print("Rejected rows:", rejected)

    return students


if __name__ == "__main__":
    load_students()	
    input("\nPress Enter to close...")