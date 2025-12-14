# Prompt the user to enter their name and store the input in the variable 'name'
print("please note name is case sensitive")
name = input("Enter your name: ")

# Print a greeting message using the entered name
print("Hello,", name, "! Welcome to the program.")

# if conditioning for John

if name == "John":
    print(name)
elif name != "John": 
    print("Not John")  
