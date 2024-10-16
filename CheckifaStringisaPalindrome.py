# Write a Python program that checks if the string entered by the user is a palindrome (a word that reads the same forward and backward).

# Step 1: Ask the user to input a string
user_string = "Python ID - Online Python Compiler"

# Step 2: Normalize the string (remove spaces and convert to lowercase)
normalized_string = user_string.replace(" ", "").lower()

# Step 3: Check if the string is a palindrome
if normalized_string == normalized_string[::-1]:
    print(f"'{user_string}' is a palindrome.")
else:
    print(f"'{user_string}' is not a palindrome.")