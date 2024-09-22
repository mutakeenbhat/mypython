#def roomA(x):
    #return x*(2000)
#def roomB(y):
    #return y*(1500)
#def roomC(z):
    #return z*(1000)
#def roomD
# #return c*(500)

hotel={'types':{'A':2000,'B':1500,'C':1000,'D':500}}
user=input("enter the type of room you want to stay (A/B/C/D) ")
user2=int(input("enter how many nights you want to spend  "))
if user=='A':
 print(f"the cost will be", {hotel['types']['A']*user2})
elif user=='B':
 print("the cost will be", {hotel['types']['B']*user2})
elif user=='C':
 print("the cost will be ", {hotel['types']['C']*user2})
else:
 print("the cost will be", {hotel['types']['D']*user2})

