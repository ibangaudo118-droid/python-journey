import math

score = math.floor(float(input("Enter your score: ")))


if score < 0 or score > 100:
  print("Invalid")

elif score >= 90:
  print('A')

elif score >= 80:
  print('B')

elif score >= 70:
  print('C')

elif score >= 60:
  print('D')

elif score >= 50:
  print('E')

else:
  print('F')
  
