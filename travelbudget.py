budget=int(input("enter your budget bro "))
flight=input("do you want to travel from (economic or business)")
if flight=='economic':
    budget-=2000
else:
    budget-=5000
acc=input("enter the accomadation (fancy/normal)")
if acc=='fancy':
    budget-=4000
else:
    budget-=2000
food=input("enter the food type (chefmade/grocerystorefood)")
if acc=='chefmade':
    budget-=3000
else:
    budget-=1000
Transport=input("enter the transport you want to use  (taxi/bus)")
if acc=='taxi':
    budget-=4000
else:
    budget-=2000
print("the remaining balance after your expenses is :",budget)

