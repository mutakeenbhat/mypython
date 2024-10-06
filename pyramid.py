def pyramid(height):
    for i in range(height):
        print(" "*(height-i-1),end=" ") 
        print("*"*(2*i+1))

    
rows=int(input("enter the number of rows"))
pyramid(rows)

