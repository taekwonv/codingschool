print('===========================')
print('Welcome to Torrance Bank')
print('===========================')

account_num = input('Account number: ')

import os
if False == os.path.exists(account_num):
  open(account_num, 'w').close()

f = open(account_num, 'r+')
balance = f.readline()
if len(balance) < 1:
  balance = 0
balance = int(balance)

while True:
  print('Menu')
  print('1. Balance')
  print('2. Deposit')
  print('3. Withdraw')
  print('4. Quit')
  menu = int(input('Choose number: '))

  if menu == 1:
    print('')
    print('Your balance is: $' + str(balance))
    print('')
  elif menu == 2:
    deposit = int(input('Deposit amount: $'))
    balance = balance + deposit
    f.seek(0)
    f.truncate()
    f.write(str(balance))
  elif menu == 3:
    withdraw = int(input('Withdraw amount: $'))
    balance = balance - withdraw
    f.seek(0)
    f.truncate()
    f.write(str(balance))
  elif menu == 4:
    break

f.close()
print('')    
print('Thank you for using Torrance Bank!')

