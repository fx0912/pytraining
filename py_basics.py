# This code demonstrates string concatenation in Python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Produces "John Doe"
print(full_name)

# this code is to get length of the full name
name_length = len(full_name)  # Produces 8
print(name_length)

# string indexing
text = "Python"
first_char = text[0]   # Accessing the first character
second_char = text[1]  # Accessing the second character
third_char = text[2]   # Accessing the third character

# Printing the characters along with their indices
print("First character (index 0):", first_char)
print("Second character (index 1):", second_char)
print("Third character (index 2):", third_char)

#string slicing
first_name = full_name[0:4]
print(first_name) # produce "John"

# upper case conversion
upper_text = full_name.upper()
print(upper_text)  # Produces "JOHN DOE"

# lower case conversion
lower_text = full_name.lower()
print(lower_text)  # Produces "john doe"

#find and replace
index = full_name.find("doe") #finding second name in full name
index = full_name.replace("Doe", "Smith") #replacing last name
print(index)  # Produces "John Smith"

