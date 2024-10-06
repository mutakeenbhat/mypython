import math as m 
num1=int(input("enter first number"))
num2=int(input("enter second number"))
result=m.gcd(num1,num2)
print(f"{m.gcd(num1,num2)}")
if result==1:
   print("numbers are c0-prime ")
else:
   print("numbers are not co-prime")