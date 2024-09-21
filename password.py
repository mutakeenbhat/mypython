ask=input("enter your password")
if len(ask)>=8 and any(char.isdigit() for char in ask ) and any(char.isalpha() for char in ask ):
    print("pswrd is strong")
else:
    print("not strong ")