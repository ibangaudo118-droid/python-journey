items = input("What would you like to buy?: ")
price = float(input("How much?: "))
quantity = int(input("How many items?: "))

total = price * quantity

print(f"You have bought {quantity} quantity of {items}")
print(f"Your total is: ${total}")