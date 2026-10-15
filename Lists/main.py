# LISTS:- a list lets us to store many items in a single variable.

employees = ["Suhag","Rahul","Karan"]
print(employees)
print(employees[0])
print(employees[1])
print(employees[2])

# LISTS ARE MUTABLE MEANING YOU CAN CHANGE THIER CONTENTS AFTER CREATING THEM.

ListsHavingManyDataTypes = ["Suhag",23,45000.70,True]
print(ListsHavingManyDataTypes[-1])
# TRUE

# ACCESSING AND SLICING LISTS

numbers = [10,20,30,40,50]
print(numbers[0])
# 10
print(numbers[-1])
# 50
print(numbers[1:4])
# 20 30 40
print(numbers[:3])
# 10 20 30
print(numbers[2:])
# 30 40 50

# TO PRINT NUMBERS FROM BACK
print(numbers[::-1])
# 50 40 30 20 10

# TRAVERSING A LIST WITH LOOPS

scores = [10,20,30,40,50]
for score in scores:
  print(score)