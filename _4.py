#devolop a program that proms the user to enter the number if the number is positive print its squre root otherwise print "Invalid input"

import math
num = int(input("Enter a number"))
if num >= 0:
    squte_root = math.sqrt(num)
    print(f"The squre root of {num} is {squte_root}")
else:
    print("Invalid input , plese try again")    
