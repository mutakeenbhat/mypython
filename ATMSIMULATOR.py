initial_balance=1000
def withdraw(x):
     global initial_balance
     initial_balance-=x
     return initial_balance
def deposit(y):
     global initial_balance
     initial_balance+=y
     return initial_balance
while True:
 ask=input("do you want to check (balance/deposit/withdraw) or type 'exit' ? ")
 if ask=='exit':
  break
 if ask=='balance':
    print(f"the current balance is",{initial_balance})
 elif ask=='deposit':
    ask2=int(input("enter the amount to be deposited $ "))
    new_bal=deposit(ask2)
    print(f"the new balance is ${new_bal}")
 elif ask=='withdraw':
    ask3=int(input("enter the amount to be deposited $"))
    if ask3>initial_balance:
       print("insufficient balance")
    else:
     new_bal=withdraw(ask3)
     print(f"the remaining balance after withdrawing is ${new_bal}")
 else:
    print("not a valid option")
    