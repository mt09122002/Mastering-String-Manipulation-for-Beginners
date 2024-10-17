# Write a Python program that takes a sentence from the user and finds the longest word in the sentence.

# Step 1: Ask the user to input a sentence
sentence = "Python ID - Online Python Compiler"

# Step 2: Split the sentence into words
words = sentence.split()

# Step 3: Find the longest word
longest_word = max(words, key=len)

# Step 4: Display the longest word
print(f"The longest word is: {longest_word}")