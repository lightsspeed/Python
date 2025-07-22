import hashlib
import re

def validate_and_hash_password(password: str) -> tuple[bool, str]:
    # Validation rules
    # 1. Minimum 6 characters
    # 2. At least one uppercase letter
    # 3. At least one lowercase letter
    # 4. At least one digit
    # 5. At least one special character
    if len(password) < 6:
        return False, ""
    if not re.search(r"[A-Z]", password):
        return False, ""
    if not re.search(r"[a-z]", password):
        return False, ""
    if not re.search(r"\d", password):
        return False, ""
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, ""

    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return True, hashed_password

# Test the function
test_passwords = ["Pass123!", "weak", "pass123", "PASSWORD123", "Pass1234!@#"]
for pwd in test_passwords:
    is_valid, hashed = validate_and_hash_password(pwd)
    print(f"Password: {pwd}, Valid: {is_valid}, Hashed: {hashed[:8]}...") 