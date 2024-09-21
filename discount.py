def discount(l,s):
    return ((l-s)/l)*100
user=int(input("enter the original price of an item \n"))
dis=int(input("enter the discount % \n"))
print(f"the final price  of the item is ${discount(user,dis)}")