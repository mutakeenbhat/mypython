def ci(P,R,N,T):
    return P*(1+R/100*N)**N*T
P=int(input("enter principal amount\n"))
R=int(input("enter rate\n"))
T=int(input("enter time period \n"))
N=int(input("enter the no of times the interest is compounded per year\n"))
print(f"the final ci is {ci(P,R,N,T,)}")