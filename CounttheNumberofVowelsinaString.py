# Write a Python program that counts the number of vowels (a, e, i, o, u) in the string provided by the user.

# Step 1: Ask the user to input a string
user_string = "Python ID - Online Python Compiler"

# Step 2: Define the vowels
vowels = "aeiouAEIOU"

# Step 3: Count the number of vowels
vowel_count = sum(1 for char in user_string if char in vowels)

# Step 4: Display the result
print(f"The number of vowels in the string is: {vowel_count}")