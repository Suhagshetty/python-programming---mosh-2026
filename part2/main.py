# TAKING USER INPUT IN PYTHON:- in python we use input() function to read data entered by a user.

name = (input("Enter your Name:- "))
print("Hello", name)

age = int(input("Enter your age:- "))
print("your age is" , age , " you will be turning " , age+1," next year")

# Adding two numbers

a = int(input("Enter the first number:- "))
b = int(input("Enter the second number:- "))
print("The sum of these two numbers is:- " ,a+b)

# A complete industry-style beginner example

name = input("Enter your Name:- ")
age = int(input("Enter your age:- "))
salary = float(input("Enter your salary:- "))
annualSalary = salary*12
print("\n--- DEVELOPER PORTFOLIO ---")
print("Name:- ",name)
print("Current Age:- ",age )
print("Monthly salary:- ",salary)
print("Annual Salary:- ",annualSalary)

# Challenge: Employee Salary & Profile Generator

print("\n ========== EMPLOYEE REPORT ========== \n")

employeeName = str(input("Employee Name:- "))
employeeId = str(input("Employee ID:- "))
Age = int(input("Age:- "))
monthlySalarry = int(input("Monthly Salary:- "))
Bonus = int(input("Bonus Percentage:- "))
permanentEmployee = bool(input("Permanent Employee? (yes/no):- "))
annualSalary = float(monthlySalarry*12)
bonusAmount = float((Bonus/100)*annualSalary)
totalComp = float(annualSalary+bonusAmount)

print("\n ========== DATA TYPES ========== \n")

print(type(employeeName))
print(type(employeeId))
print(type(Age))
print(type(monthlySalarry))
print(type(Bonus))
print(type(permanentEmployee))
print(type(annualSalary))
print(type(bonusAmount))
print(type(totalComp))
