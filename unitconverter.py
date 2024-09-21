def lengthmiles(x):
 return x*3.28084 
def km(x):
 return x*0.621371

def weight(x):
 return x*2.2046
def temp (x):
 return x*(9/5)+32
print("enter your choice")
print("1.metr to miles ")
print("2.km to miles")
print("3.kgs to pounds ")
print("4.celsius to fah")
while True:
 choice=input("enter your choice (1/2/3/4): ")
 if choice =='1':
   num1=int(input("enter value in meters :"))
   print(f"mter to feet is {lengthmiles(num1)}")
 elif choice=='2':
   num2=int(input("enter value in km :"))
   print(f"km to m is {km(num2)}")
 elif choice=='3':
    num3=int(input("enter value in kgs:"))
    print(f"kg to pounds is {weight(num3)}")
 else:
   num4=int(input("enter value in celcius :"))
   print(f"temperature from c to fah is {temp(num4)}")
 next=input("do you ant to continue(y/n)")
 if next=='n':
   print("okbye")
   break
 else:
   print("lets do it firse")
   
   
