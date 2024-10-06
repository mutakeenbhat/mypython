user=int(input("enter a number "))
square=user**2
str_square=str(square)
if  str_square.endswith(str(user)):
        print(f"{user} is automorphic")
else:
        print(f"{user} not automorphic")