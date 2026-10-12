bank_name = "Kinerax Bank"
account_name = input("Enter your name: ")
correct_pin = 1234
account_number = "0123455789"
balance = 40000
account_type = "Savings"
branch = "Lagos Main"
date_opened = "2026-10-12"

print("______________________________")
print("")
print(f'    {bank_name}')
print("______________________________")
print("")
print(f'Welcome, {account_name}')
print("")
print(f'Account Number: {account_number}')
if balance < 50000:
  print("Tier: Silver")
elif balance >= 200000:
  print("Tier: Platinum")
else:
  print("Tier: Gold")

print(f'Balance: ₦{balance}')
print(f'Account Type: {account_type}')
print(f'Branch: {branch}')
print(f'Date Opened: {date_opened}')
print("")

account_pin = int(input("Enter your PIN: "))

if account_pin == correct_pin:
  print("______________________________")
  print("")
  print("----Menu----")
  print("")
  print("______________________________")
  print("")
  print("What would you like to do?")
  print("")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Exit")
  print("")
  print("______________________________")
  print("")
  choose = int(input("Choose(1-4):  "))

  if choose == 1:
    #asking users for deposit
    print("")
    deposit = int(input("How much do you want to deposit?: "))
    if balance < 50000:
      balance1 = (balance + deposit) - 50
      print("______________________________")
      print("")
      print("Deposit Successful")
      print("Fee: ₦50")
      print(f'You deposited ₦{deposit} to your bank account')
      print(f'Added: ₦{deposit}')
      print(f'New Balance: ₦{balance1}')
    elif balance >= 200000:
      balance = balance + deposit
      print("______________________________")
      print("")
      print("Deposit Successful")
      print("Fee: ₦0")
      print(f'You deposited ₦{deposit} to your bank account')
      print(f'Added: ₦{deposit}')
      print(f'New Balance: ₦{balance}')

    else:
      balance1 = (balance + deposit) - 30
      print("______________________________")
      print("")
      print("Deposit Successful")
      print("Fee: ₦30")
      print(f'You deposited ₦{deposit} to your bank account')
      print(f'Added: ₦{deposit}')
      print(f'New Balance: ₦{balance1}')
#After a customer deposits money, does their tier change immediately? No. I hav'nt buult that part yet.

  elif choose == 2:
    #asking users for withdrawal
    print("")
    withdraw = int(input("How much do you want to withdraw?: "))

    #step 1: determine the fee based on tier
    if balance < 50000:
      fee = 100
    elif balance >= 200000:
      fee = 0
    else:
      fee = 60

    #step 2: check if balance covers withdrawal + fee
    if withdraw + fee > balance:
      print("Insufficient Funds")
    else:
      balance = balance - withdraw - fee
      print("Withdrawal Successful")
      print(f'Fees: ₦{fee}')
      print(f'You have Successfully withdrawn ₦{withdraw} from your bank account')
      print(f'Withdrawn: ₦{withdraw}')
      print(f'New balance: ₦{balance}')

  elif choose == 3:
    print(f'Balance: {balance}')

  elif choose == 4:
    print("Thank you for banking with Kinerax Bank")

  else:
    print("Invalid choice")

else:
  print("INVALID PIN. ACCESS DENIED")
