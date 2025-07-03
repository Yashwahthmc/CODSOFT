import random
import string
def generate_password(len=12):
    if len<6:
        return "Password too short. Use at least 6 characters."
    all_chars=string.ascii_letters + string.digits + string.punctuation
    passwd=''.join(random.choice(all_chars) for _ in range(len))
    return passwd
print("🔐 Welcome to Yashwanth's Password Generator 🔐")
try:
    len=int(input("Enter the desired password length:"))
    print("Generated Password:",generate_password(len))
except ValueError:
    print("Please enter a valid number.")
