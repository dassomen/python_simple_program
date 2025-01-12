#write to create a calculator using if else or switch function

while True:
    print("select a operator.")  
    print("1.Add")
    print("2.Subtraction")
    print("3.Multipliction")
    print("4.Divition")
    print("5.Exit")

    choice = input("Enter Your choise(1/2/3/4/5): " )
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))
        except ValueError:
            print("Invalid input, plese enter numbres only")
            continue

        if choice == '1':
            result = num1+num2
            print(f"{num1} + {num2} = {result}")


        elif choice == '2':
            result = num1-num2
            print(f"{num1} - {num2} = {result}")


        elif choice == '3':
            result = num1*num2
            print(f"{num1} * {num2} = {result}")

        elif choice == '4':
            result = num1/num2
            print(f"{num1} / {num2} = {result}")    


    elif choice == '5':
        print("Exiting calculator.")
        break
    else:
        print("Invalid Input")       

