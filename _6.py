'''Write a program thats promts the user to input a celcius temperature and output the equivalent temparature in fahrenheit. the formula to convert the temparature is : F = (9/5) * C  + 32 where F is the Farhenhite temparature and C is the celsius tempareture '''

celcius = float(input("Enter a temperature in celcius : "))
fahrenheit = (9/5)*celcius+32
print(f"temperature in fahrenheit :{fahrenheit:.2f}")
