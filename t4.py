weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))
age = int(input("Enter your age: "))
gender = input("Enter your gender(male/female): ")

bmi = round(weight / (height ** 2),1)

if age < 18:
  print(f'Your BMI is: {bmi}')
  print("(Note: BMI for minors is intepreted differently)")
  
elif bmi < 18.5 or bmi > 30 and age > 65:
  print(f'Your BMI is: {bmi}')
  print("Consult a doctor")

elif bmi > 30 and age <= 60:
  print(f'Your BMI is: {bmi}')
  print("High health risk")

else:
  print(f'Your BMI is: {bmi}')
  print("Normal")
  

