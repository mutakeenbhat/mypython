def running(x):
    return x*11
def cycling(y):
    return y*20
def swimming(z):
    return z*30

user=input("which exercise did you perform (running/cycling/swimming) ? ")
user2=int(input("how many minutes did you exercise"))
if user=='running':
    print(f"the calories burned by running is {running(user2)}")
elif user=='cycling':
    print(f"the calories burned by cycling is {cycling(user2)}")
else:
    print(f"the calories burned by swimming is {swimming(user2)}")