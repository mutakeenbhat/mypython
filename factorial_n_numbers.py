import math as m
def facto(x):
   return m.factorial(x)
   
num= int(input("enter a number"))
sum1=0
for i in range(1,num+1):
   sum1 +=facto(i)
print(f"the sum of {num} is {sum1}")

