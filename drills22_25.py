# drill 22
def bigger(a, b):
  if a > b:
    return a
  else: 
    return b

print(bigger(7, 10))
print(bigger(20,5))


# drill 23
def grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

print(grade(85))
print(grade(72))
print(grade(45))

#drill 24
def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

print(is_even(4))
print(is_even(7))

#drill 25
def can_vote(age):
  if age >= 18:
    return True
  else: 
    return False

print(can_vote(20))
print(can_vote(15))