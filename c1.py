num1 = float(input("Enter num1: "))
operator = input("Enter operator(+ - * /): ")
num2 = float(input("Enter num2: "))

if operator == "+":
  result = num1 + num2
  print(round(result,2))

elif operator == "-":
  result = num1 - num2
  print(round(result,2))

elif operator == "*":
  result = num1 * num2
  print(round(result,2))
  

elif operator == "/":
  if num2 == 0:
    print("Cannot divide by zero")
  else:
    result = num1 / num2
    print(round(result,2))

else: 
  print("Invalid operator")