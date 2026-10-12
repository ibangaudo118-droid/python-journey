age = int(input("Enter your age: "))

if age >=100:
  print("You are too old")

elif age >= 18:
  print("You are signed in")

else: 
  print("You are not allowed to sign up")


#exercise2

response = input("Would you like some food?(Y/N): ")

if response == "Y":
  print("Have some food!")

else:
  print("No food for you!")

#exercise 3

name = input("Enter your name: ")

if name == "":
  print("You did not type in your name")

else:
  print(f"Hello, {name}!")