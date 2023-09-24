import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length and complexity
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Password length should be a positive integer.")
    else:
        complexity = input("Enter complexity level (low/medium/high): ").lower()
        if complexity not in ["low", "medium", "high"]:
            print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        else:
            generated_password = generate_password(length, complexity)
            print("Generated Password: " + generated_password)
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")
