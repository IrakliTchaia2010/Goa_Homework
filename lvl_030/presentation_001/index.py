print('===Registration===')
login_user = input('enter your user:')
login_password = input('enter your passowrd (password must be bellow 20 characters ):')
while len(login_password)>20 or len(login_password)<1:
    print("invalid password, try again")
    login_password=input("enter your  password (Password must be below 20 characters): ")
print(f'welcome {login_user}')



print()
print('loading main menu...')
print()






new_balance = 0
while True:
 balance = []

 print("===GOA Bank===")
 print("1) Check balance:")
 print("2) Deposit money:")
 print("3) Withdraw money:")
 print('4) Transfer money:')
 print("5) Leave system:")


 choice = int(input("enter your choice:"))



 if choice == 1:
   print()
   print('checking balance...')
   print(f'your balance is {new_balance}')
   print()
  
 
 elif choice ==5:
  print()
  print("goodbye")
  break
  print()
 
 elif choice ==2:
  print()
  amount = int(input('enter amount you want to deposit:'))
  print()
  print(f"you deposited {amount} to your account")
  print("your new balance is:")
  new_balance = new_balance + amount
  print(new_balance)
  print()

 elif choice ==3:
  withdraw_amount = int(input('enter how much u want to withdraw:'))
  print()
  if withdraw_amount > new_balance:
   print('sorry you dont have enough money on your account')
   print('taking loan...')
   print()
  
  
  print(f"you withdrawed {withdraw_amount} from your account")
  print('new balance is:')
  new_balance = new_balance - withdraw_amount
  print(new_balance)
  print()

 elif choice ==4:
  print()
  reciver = input('Enter receiver user: ')
  transfer_amount = int(input('Enter how much u want to transfer: '))
  if transfer_amount>new_balance:
    print('Not enough money on your account try again')
  transfer_amount = int(input('Enter how much u want to transfer: '))
  print()
  if  transfer_amount<= new_balance:
    print(f'transfering money to {reciver}...')
  new_balance = new_balance - transfer_amount
  print('money transfered succesfully')
  print(f'new balance is {new_balance}')
  print()
  

  
 



 

    