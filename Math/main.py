# ARTHMETIC OPERATORS
import math
a = 10
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

# Augmented Assignment operators

score = 100
score+=20
print(score)
score-=10
print(score)
score*=2
print(score)
score//=3
print(score)

#  ORDER OF PRECENDENCE:- 1: PARENTHESIS 2: EXPONENTIATION 3: MULTIPLICATION/DIVISION 4: ADDITION/SUBTRACTION

# MATH FUNCTIONS/METHODS IN PYTHON:-

# ABS() returns the absolute value of a number. Its a built in function.

print(abs(-10))
print(abs(8))
print(abs(-3.14))

#  POWER() - pow - used to calulate power of the number. x ** y

print(2**3)
print(pow(2,3))
print(pow(5,2))

# SQAURE ROOT - math.sqrt() - used to calculate the square root of a number. It is a built in function. Returns a floating point number.

print(math.sqrt(25))
print(math.sqrt(2))
print(math.sqrt(81))

# Rounding in Math -> round():-Rounds to the nearest value. , floor():- Rounds down to the greatest integer less than or equal to the number. , ceil():- ounds up to the smallest integer greater than or equal to the number.

print(round(3.6))
print(round(2.3))
print(math.floor(3.6))
print(math.ceil(3.6))

#  4 , 2 ,  3 , 4

#  AREA OF A CIRCLE PROGRAM

radius = float(input("Enter the radius of the circle:- "))
area = math.pi*radius**2
print("Area of the circle is called:- ",area)

#  TRIGNOMETRIC FUNCTIONS IN PYTHON:- math module supports sine cosine and tangent functions.

print(math.sin(math.radians(30)))  # Approximately 0.5
print(math.cos(math.radians(60)))  # Approximately 0.5
print(math.tan(math.radians(45)))  # Approximately 1.0

getDegree = int(input("Enter the degree to check for the  sin value:- "))
print(math.sin(math.radians(getDegree)))


print("========== DISTANCE CALCULATOR ==========")

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

delta_x = x2 - x1
delta_y = y2 - y1

distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

print(f"Horizontal difference: {abs(delta_x):.2f}")
print(f"Vertical difference: {abs(delta_y):.2f}")
print(f"Distance between points: {distance:.2f}")
