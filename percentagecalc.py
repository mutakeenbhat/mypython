def per(a,b):
    return (a/100)*b
def per2(a,b):
    return 100*(a/b)
def per3(new,old):
    return 100*((new-old)/old)
choice =input("enter your choice\n 1.calculate percentage of a number\n  2. calculate what percentage one number is of another \n 3.calculate percentage increase or decrease )")
x=int(input("enter the number"))
y=int(input("enter another "))
while True:
    if choice=='1':
        print(f"the % of a number is {per(x,y)}")
    elif choice=='2':
        print(f"the %of one number to another is {per2(x,y)}")
    else:
        print(f"the percentage is {per3(x,y)}")
    break