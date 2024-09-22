mysystem={'items':{'A':2,'B':5,'C':8,'D':9 }}
print(f"{mysystem}")
user=input("do you want to add or del items to the inventory?(add/del)")
if user=='add':
   user2=int(input("enter the item "))
   mysystem['items']['E']=user2
   print(f"{mysystem}")
else:
    user3=(input("enter the item to del "))
    del mysystem['items'][user3]
    print(f"after deleting {user3} from {mysystem}")
