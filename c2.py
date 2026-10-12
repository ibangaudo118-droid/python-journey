print("____MENU____")
print("1. Kg to Pounds")
print("2. Celcius to Fahrenheit")
print("3. Kilometerzs to Miles")

choose = (input("Choose number(1-3: "))
value = float(input("Enter value: "))

if choose == "1":
  result = value * 2.205
  print(f'The result is {round(result,2)} pounds')

elif choose == "2":
  result = value * 9/5 + 32
  print(f'The result is {round(result,2)} Fahrenheiht')

elif choose == "3":
  result = value * 0.621
  print(f'The result is {round(result,2)} miles')

else: 
  print("Invalid Choice")


