user1=int(input("enter the number a\n "))
user2=int(input("enter the number b \n"))
user3=int(input("enter the number c "))
if user1>user2 and user1>user3:
    print(f"the largest number is a : {user1}")
elif user2>user1 and user2>user3:
    print(f"the largest number is b : {user2}")
else:
    print(f"the largest number is c : {user3}")
