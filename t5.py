monthly_income = int(input("Enter Monthly income: "))
employment_type = input("Enter your employment type: ")
TIN = input("Do you have a TIN(yes or no): ")



if monthly_income < 30000:
  Tax_rate = (0/100)
  Tax_amount = monthly_income * (0/100)
  net_income = monthly_income - Tax_amount
  

elif monthly_income <= 100000:
  Tax_rate = (7/100)
  Tax_amount = monthly_income * (7/100)
  net_income = monthly_income - Tax_amount


elif monthly_income <= 300000:
  Tax_rate = (11/100)
  Tax_amount = monthly_income * (11/100)
  net_income = monthly_income - Tax_amount


elif monthly_income <= 600000:
  Tax_rate = (15/100)
  Tax_amount = monthly_income * (15/100)
  net_income = monthly_income - Tax_amount


else:
  Tax_rate = (24/100)
  Tax_amount = monthly_income * (24/100)
  net_income = monthly_income - Tax_amount

  



#special case:

if employment_type == "self employed" and monthly_income > 300000:
  Tax_rate = 15% + (2/100)
  print(Tax_rate)

else:
  print()
  
if TIN == "no":
  penalty = 5000
  Total_tax = Tax_amount + penalty
  
  print(f'TIN Penalty: {penalty}')
  print(f'Total Tax: {Total_tax}')
  print(f'Net Income: {net_income}')

else:
  print(f'Your Tax rate is: {Tax_rate} ')
  print("No penalty")
  print(f'Tax amount: {Tax_amount}')
  print(f'Net Income: {net_income}')
