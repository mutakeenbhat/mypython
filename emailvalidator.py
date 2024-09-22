user=str(input("enter your email id "))
if '@' in user  and '.' in user:
    print("valid email id")
else:
    print("missing @ or .")