temperature = float(input("Enter your Temperature: "))
unit = input("Choose the unit(c or F): ")

if unit == "c":
  temperature = temperature + 32
  print(f'Your temperature in Fahrenheit is: {temperature}F')

elif unit == "F":
  temperature = temperature - 32
  print(f'Your temperature in celcius is: {temperature}C')

else:
  print(f'Invalid input')