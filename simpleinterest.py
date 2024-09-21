def SI(p,r,t):
    return (p*r*t)/100
p=int(input("enter principal"))
r=int(input("enter rate"))
t=int(input("enter time"))
print(f"the SI is : {SI(p,r,t)}")