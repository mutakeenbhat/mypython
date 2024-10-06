def addu(summ):
    return sum(summ)
user=int(input("enter a number "))
summ=0
while user>0:
    summ+=user**3
    user-=1
    
print(f"Final sum of cubes: {summ}")
