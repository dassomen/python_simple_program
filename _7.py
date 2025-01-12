'''write a program which accept principal, rate, and time from user and print the simple interest 
the fomula of calculate simple interest is : (principal * rate * time) /100'''

principal_Ammount = float(input("Enter Principal Amount"))
rate_Of_Intetest = float(input("Enter rate of interest (%)"))
time = float(input("Enter time in Year"))

simple_Interest = (principal_Ammount*rate_Of_Intetest*time)/100

print("The Simple Interest is : ",simple_Interest)




