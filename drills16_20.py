#drill 16

def area_rect(l,w):
  return (l*w)

print(area_rect(5,3))

#drill 17
#predicting 77.0 as output

def celsius_to_f(c):
  return (c * 9/5 +32)

print(celsius_to_f(25))

#drill 18

def say_hello(name):
  print(f'Hello, {name}!')

say_hello("David")
say_hello("Jason")
say_hello("Jacob")



#drill 19

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print(is_adult(20))   # True
print(is_adult(15))   # False

#drill 20

def bmi(weight, height):
  return weight / (height ** 2)

print(bmi(70, 1.75))

