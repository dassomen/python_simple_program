'''
    write a program that accept second from keyboard as integer. your program should convert second 
    in hour, minutes and second. your output should be like this 
    Enter second : 13400
    Hours : 43
    Mintus : 43
    Seconds : 20
'''

second = int(input("Enter Second : "))

#Calculate total hour 
hours = second//3600

remaining_Second = second%3600


#calculate Minutes
minutes = remaining_Second//60


#calculate second
second = remaining_Second%60

print("Hours : ",hours)
print("Minutes : ",minutes)
print("Second : ",second)


