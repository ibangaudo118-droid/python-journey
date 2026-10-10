#drill 26
def password_ok(pw):
  if pw >= 8:
    return True
  else:
    return False

print(password_ok(len("abcd1234"))) #True
print(password_ok(len("abc"))) #False

#drill 27
def max_of_three(a,b,c):
  if a >= b and a >= c:
    return a
  elif b>= a and b>= c:
    return b
  else:
    return c

print(max_of_three(3,8,5)) #8
print(max_of_three(4,7,10))

#drill 28
def describe_temp(c):
  if c < 15:
    return "cold"
  elif c < 30:
    return "warm"
  else:
    return "hot"

print(describe_temp(10)) #cold
print(describe_temp(22)) #warm
print(describe_temp(35)) #hot


#drill 29
def divisible_by_3_and_5(n):
  if n % 3 == 0 and n % 5 == 0:
    return True
  else: 
    return False

print(divisible_by_3_and_5(15)) #True
print(divisible_by_3_and_5(9))  #False


#drill 30
def greet_by_hour(hour):
  if 5<= hour <= 11:
    return "morning"
  elif 12<= hour <= 17:
    return "afternoon"
  elif 18<= hour <= 21:
    return "evening"
  else:
    return "night"

print(greet_by_hour(8)) #morning
print(greet_by_hour(14)) #afternoon
print(greet_by_hour(20)) #evening
print(greet_by_hour(3)) #night