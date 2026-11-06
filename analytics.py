import csv
from collections import Counter


def generate_report():

    # Read original student records
    with open("contacts.csv", "r", newline="") as file:
        raw_students = list(csv.DictReader(file))

    # Read clean student records
    with open("students_clean.csv", "r", newline="") as file:
        students = list(csv.DictReader(file))

    total = len(raw_students)
    accepted = len(students)
    rejected = total - accepted

    # Calculate acceptance percentage
    if total > 0:
        accuracy = (accepted / total) * 100
    else:
        accuracy = 0

    # Count phone starting digits
    phone_counts = Counter()

    for student in students:
        first_digit = student["phone"][0]
        phone_counts[first_digit] += 1

    # Count email domains
    domain_counts = Counter()

    for student in students:
        domain = student["email"].split("@")[1]
        domain_counts["@" + domain] += 1

    # Display report
    print("\n" + "=" * 55)
    print("       STUDENT REGISTRATION - BUSINESS INTELLIGENCE")
    print("=" * 55)

    print("Total Contacts Processed :", total)
    print("Valid Registrations      :", accepted)
    print("Rejected Records         :", rejected)
    print("Data Quality Accuracy    :", round(accuracy, 2), "%")

    print("\n--- Telecom Network Breakdown ---")

    for digit in ["9", "8", "7", "6"]:
        print(digit + "-Series :", phone_counts[digit], "students")

    print("\n--- Email Domain Breakdown ---")

    for domain, count in domain_counts.most_common():
        print(domain, ":", count, "students")

    print("=" * 55)


if __name__ == "__main__":
    generate_report()