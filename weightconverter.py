weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds(Kg or Lsb?: ")

if unit == "Kg":
  weight = weight * 2.205
  print(f'Your weight is: {weight} {unit}')

elif unit == "Lsb":
  weight = weight / 2.205
  print(f'Your weight is:{weight} {unit}')

else: 
  print(f'{unit} is an invalid operator')