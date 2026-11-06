def validate_contact(name, phone, email):

    # 1. Validate Name
    if not name or len(name.strip()) == 0:
        return False, "Name is blank"

    # 2. Validate Phone Number
    if not phone or len(phone) != 10 or not phone.isdigit() or phone[0] not in "6789":
        return False, "Invalid phone number"

    # 3. Validate Email
    if not email or email.count("@") != 1:
        return False, "Invalid email: incorrect @ symbol"

    if any(char.isspace() for char in email):
        return False, "Invalid email: contains whitespace"

    username, domain = email.split("@")

    if len(username) == 0:
        return False, "Invalid email: missing username"

    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False, "Invalid email: incorrect domain"

    # All validations passed
    return True, "Valid contact"