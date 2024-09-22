def share(x,y):
    return x/y
fare=int(input("enter the flight fare :"))
peeps=int(input("enter how many people are sharing the fare : "))
print(f" the cost for each person to pay is {share(fare,peeps)}")