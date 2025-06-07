#password generatoer
import random
import string
def generate_password(length=12):
    """Generate a random password of specified length."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Ensure the password contains at least one lowercase, one uppercase, one digit, and one special character
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)
    
    # Fill the rest of the password length with random choices from all character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_length = length - 4
    password = lower + upper + digit + special + ''.join(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    
    return ''.join(password_list)
def main():
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
    while True:
        try:
            play_again = input("Do you want to generate another password? (yes/no): ").lower()
            if play_again == 'yes':
                length = int(input("Enter the desired password length (minimum 4): "))
                password = generate_password(length)
                print(f"Generated password: {password}")
            elif play_again == 'no':
                print("Thanks for using the password generator!")
                break
            else:
                print("Invalid input! Please enter yes or no.")
        except ValueError as e:
            print(e)
            print("Invalid input! Please enter a valid number for password length.")
            continue
            