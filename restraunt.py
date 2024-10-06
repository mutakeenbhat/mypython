def tip(x):
     return x*0.10 
user=float(input("enter your bill"))
print("calculating a 10% tip")
print(f"the tip for you is {tip(user)}")
print(f"the total amount to be paid is {user+tip(user)}")