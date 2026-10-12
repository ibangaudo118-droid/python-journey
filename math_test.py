import math

#exercise 1

radius = float(input("Enter radius: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)}cm²")

#exercise2

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2

print(f"The area is: {round(area,3)}cm²")

#exercise3

radius = float(input("Enter radius: "))
area = math.pi * pow(radius, 2)

print(area)

#exercise 4

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(c)