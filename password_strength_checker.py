# Password Strength Checker
# Author: Panasa chandu
# Simple Cyber Security Project

import re

def check_password_strength(password):
    strength = 0
    remarks = ''

    # Length check
    if len(password) < 6:
        remarks = "Password too short. Must be at least 6 characters."
        return "Weak", remarks

    # Check for uppercase, lowercase, digits, and special chars
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[@$!%*?&]', password):
        strength += 1

    # Strength levels
    if strength == 1:
        remarks = "Weak password. Try adding more variety of characters."
        return "Weak", remarks
    elif strength == 2:
        remarks = "Moderate password. Add symbols or numbers to strengthen it."
        return "Moderate", remarks
    elif strength >= 3:
        remarks = "Strong password. Good job!"
        return "Strong", remarks


# Main program
if __name__ == "__main__":
    print("=== PASSWORD STRENGTH CHECKER ===")
    user_password = input("Enter your password: ")
    level, message = check_password_strength(user_password)
    print(f"\nPassword Strength: {level}")
    print(f"Feedback: {message}")
