import random
import string

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Smart Password Generator 🔐")
    
    length = int(input("Enter password length: "))
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, symbols)
    
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
