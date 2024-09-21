while True:
    dis=int(input("enter the distance"))
    if dis==1:
        fare=5
    elif dis>1:
        fare=fare+(dis-1)*3
    else :
        print("invalid")
        continue
    print(f"the total fare for {dis} in km  is  ${fare} ")
    




    