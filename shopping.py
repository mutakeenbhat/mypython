def discount(x):
    return x*0.1
user=int(input("enter the shooping amount" ))
if user>100:
 print(f"applying a 10% discount the total will be {discount(user)} ")
else:
 print("discount not applied ")