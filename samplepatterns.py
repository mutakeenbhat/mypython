for i in range(5-1):             #this whole code is for a diamond shape 
    for j in range(i,5):         #but this dirst block of code in the for loop is a triange on the upper side 
     print(" ",end=" ")
    for j in range(i):
     print("#",end=" ")
    for j in range(i+1):
     print("#",end=" ")
    print()
for i in range(5):
    for j in range(i+1):
     print(" ",end=" ")
    for j in range(i,5-1):          #this one is the lower side 
     print("#",end=" ")
    for j in range(i,5):
     print("#",end=" ")
    print()