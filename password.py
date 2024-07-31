import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    return ''.join(password)

def password_generator():
    length = int(input("Enter the length for the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    password_generator()
