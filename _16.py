#WAP to check an alphabates whether it is a vowel or consonant
user_input = input("Enter ja ichha ").lower()
vowel = "aeiou"

if user_input in vowel:
    print(f"{user_input} is a vowel")
else:
    print(f"{user_input} is a consonant")



