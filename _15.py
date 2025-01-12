#WAP in check the given input is alphabat or number or character
user_Input = input("Enter any input")
if user_Input.isalpha():
    print(f"{user_Input} is an Alphabat.")
elif user_Input.isdigit():
    print(f"{user_Input} is a Digit.")
else:
    print(f"{user_Input} is a special charecter")
