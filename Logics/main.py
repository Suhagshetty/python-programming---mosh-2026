# IF STATEMENTS IN PYTHON

age = 15
if age>=18:
    print("You are elogible to vote")
else:
    print("You are not eligible to vote")
    
# IF ELIF AND ELSE STATEMENTS IN PYTHON

marks = 85
if marks>=85:
    print("GRADE A")
elif marks>=75:
    print("GRADE B")
elif marks>=65:
    print("GRADE C")
else:
    print("Needs some performance")
    
# NESTED IF STATEMENTS IN PYTHON

age = 23
hasId = True
if age>=18:
    if hasId:
        print("Entry Allowed")
    else:
        print("Id is required")
else:
    print("Entry denied")
    
#  COMPARISON EXAMPLES

salary = 45000
print(salary>30000)
print(salary<30000)
print(salary==45000)
print(salary!=45000)

# LOGICAL OPERATORS

# AND:- BOTH CONDITIONS MUST BE TRUE.

age = 23
hasId = True
if age>=18 and hasId:
    print("Entry Allowed")
else:
    print("Denied")

#  OR:- atleast one condition must be true.

day = "saturday"
if day=="saturday" or day=="sunday":
    print("Its a weekend")
else:
    print("weekday")
    
#  NOT:- reverses a boolean result

isBlocked = False
print( not isBlocked)
#  TRUE

# WEIGHT CONVERTER PROGRAM


weight = float(input("Enter your weight: "))
unit = input("Convert to (K)g or (L)b? ").strip().lower()

if weight < 0:
    print("Weight cannot be negative.")
elif unit == "k":
    converted_weight = weight / 2.20462
    print(f"Weight in kilograms: {converted_weight:.2f} kg")
elif unit == "l":
    converted_weight = weight * 2.20462
    print(f"Weight in pounds: {converted_weight:.2f} lb")
else:
    print("Invalid unit. Enter K or L.")



# Project: Employee Fitness & Wellness Report


import math

print("\n========== EMPLOYEE WELLNESS SYSTEM ==========\n")

# 1. Collect employee details
employee_name = input("Enter employee name: ").strip().title()
employee_id = input("Enter employee ID: ").strip().upper()
age = int(input("Enter age: "))

# 2. Collect fitness details
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# 3. Collect additional information
department = input("Enter department: ").strip().title()
is_active = input("Is the employee active? (yes/no): ").strip().lower() == "yes"

# 4. Validate the input
if age <= 0 or weight <= 0 or height <= 0:
    print("\nInvalid input! Age, weight, and height must be positive.")

elif not employee_name or not employee_id:
    print("\nEmployee name and ID cannot be empty.")

else:
    # 5. Calculate BMI
    bmi = weight / (height ** 2)
    rounded_bmi = round(bmi, 2)

    # 6. Calculate a reference weight range for the given height
    min_healthy_weight = 18.5 * (height ** 2)
    max_healthy_weight = 24.9 * (height ** 2)

    # 7. Classify BMI (adult screening categories)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Healthy weight range"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity range"

    # 8. Check employee eligibility for a wellness follow-up
    needs_followup = (
        is_active
        and age >= 18
        and (bmi < 18.5 or bmi >= 25)
    )

    # 9. Generate the report
    print("\n========== WELLNESS REPORT ==========")

    print(f"Employee Name : {employee_name}")
    print(f"Employee ID   : {employee_id}")
    print(f"Age           : {age}")
    print(f"Department    : {department}")
    print(f"Active        : {is_active}")

    print("\n---------- FITNESS SUMMARY ----------")
    print(f"Weight        : {weight:.2f} kg")
    print(f"Height        : {height:.2f} m")
    print(f"BMI           : {rounded_bmi:.2f}")
    print(f"Category      : {category}")

    print(
        f"Reference weight range: "
        f"{min_healthy_weight:.1f}–{max_healthy_weight:.1f} kg"
    )

    if needs_followup:
        print("Follow-up     : Wellness check-in recommended")
    else:
        print("Follow-up     : No automatic follow-up flagged")

    print("\n---------- TECHNICAL DETAILS ----------")
    print(f"BMI absolute value: {abs(bmi):.2f}")
    print(f"Rounded age       : {math.floor(age)}")
    print(f"Name characters   : {len(employee_name)}")
    print(f"Name starts with S: {employee_name.startswith('S')}")

    print("\n========== REPORT COMPLETE ==========")
