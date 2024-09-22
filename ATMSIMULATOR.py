while True:
 initial_balance=1000
 def withdraw(x):
    return initial_balance-x
 def deposit(y):
    return y+initial_balance
 ask=input("do you want to check (balance/deposit/withdraw) or type 'exit' ? ")
 if ask=='exit':
    break
 if ask=='balance':
    print("the current balance is",initial_balance)
 elif ask=='deposit':
    ask2=int(input(print("enter the amount to be deposited $")))
    print(f"the new balance is ${deposit(ask2)}")
 elif ask=='withdraw':
    ask3=int(input(print("enter the amount to be deposited $")))
    print(f"the remaining balance after withdrawing is ${withdraw(ask3)}")
 else:
    print("not a valid option")
    