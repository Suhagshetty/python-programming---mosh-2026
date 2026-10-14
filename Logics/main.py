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