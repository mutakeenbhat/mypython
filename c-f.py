def temp (x):          #celcius to fahrenhiet
 return x*(9/5)+32
def tempu(x):           #fahrehiet to celcius 
 return (x-32)*5/9

y=int(input("enter the temp in c"))
print(f"the temp in fah is: {temp(y)}\n")
z=int(input("enter the temp in fah"))
print(f"the temp in C is: {tempu(z)}")