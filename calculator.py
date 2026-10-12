

operator = input("Enter opearator(+ - * /) ")
num1 = float(input("Enter num1: "))
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
  result = num1 / num2
  print(round(result,2))

else:
  print(f"{operator} is not a valid opearator")