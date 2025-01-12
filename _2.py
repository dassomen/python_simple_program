#take 5 number in 5 subject and calculate total parcentage avarage
subject1 = int(input("Enter Your obtin marks in bangali"))
subject2 = int(input("Enter Your obtin marks in English"))
subject3 = int(input("Enter Your obtin marks in Physics"))
subject4 = int(input("Enter Your obtin marks in Chemistry"))
subject5 = int(input("Enter Your obtin marks in Biology"))

total = subject1+subject2+subject3+subject4+subject5
avg = total/5
parcentage = (total/500)*100

print("The Total obtain Marks is : ",total)
print("The Avarage marks is : ",avg)
print("The parcentage is : ",parcentage,"%")