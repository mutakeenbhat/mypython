def bill(a,b,c,d,e):               #making grocery bill using two methods one simple varibale  another is function  
    return a+b+c+d+e

a=input("enter the  grocery items no 1 ")                  # asking the user for five differnt groceries 
b=input("enter the grocery items 2")
c=input("enter the grocery items 3 ")
d=input("enter the grocery items 4 ")
e=input("enter the  grocery items 5" )
user1=int(input("price of first   "))                     #main thing asking for price of each item
user2=int(input("enter the price of second" ))
user3=int(input("enter the price of third" ))
user4=int(input("enter the price of fourth" ))
user5=int(input("enter the price of fifth" ))
#bill=user1+user2+user3+user4+user5                          # making a variable and summing the user input 
#print(f"the grocery bill is : {bill}")                                            #printing the sum value by simply calling the varaible 
print(f"the grocery bill is : {bill(user1,user2,user3,user4,user5)}")                # printing the sum by calling the function 


#another method
items=[]
values=[]
for i in range(5) :
  item =input(f"enter an item in the list {i+1} ")
  value=int(input(f"enter value of {item} "))
  items.append(item)
  values.append(value)

bill=sum(values)
print(f"stotal bill is {bill}")