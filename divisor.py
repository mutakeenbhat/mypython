user=int(input("enter a number"))
div=0
while user>0:
    div+=user
    user-=1
    if user%div==0:
     print(f"{user}it is a devisor")
    else:
       print(f"{user} not a divisor")