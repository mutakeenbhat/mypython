import math as m
num=int(input("enter a number"))
if num<0:
    print("cant do negative numbers factorial")
elif num==0:
    print(f"factorial of {num} is {num} ")
else:
    print(m.factorial(num))


