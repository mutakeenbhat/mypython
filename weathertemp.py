
temp=[]
user=int(input("enter the temperature of day1 days "))
user2=int(input("enter the temperature of day2 days "))
user3=int(input("enter the temperature of day3 days "))
user4=int(input("enter the temperature of day4 days "))
temp.append(user)
temp.append(user2)
temp.append(user3)
temp.append(user4)
print(f"the daily temperature in celcius is  {temp}")
#tempnew=(temp[0]+temp[1]+ temp[2]+temp[3])/len(temp)
#print("the average temperature in celcius is ",tempnew)
print("the av of the temperature in c is ",sum(temp)/len(temp))
