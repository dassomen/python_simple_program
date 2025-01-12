#write a program to convert uppercase to lower case     lower case to uppercase 

user_Input = input("Enter any thing : ")
result = ""

for char in user_Input:
    if char.isupper():
        result+=char.lower()
    elif char.islower():
        result+=char.upper()
    else:
        result+=char
print("Converted string:",result)