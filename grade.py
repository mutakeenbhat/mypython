def av(x):
   return (sum(x))/(len(x))
mark=[]
for i in range(3):
 marks=int(input(f"enter the marks for subject {i+1} "))
 mark.append(marks)
 if marks>=90 and marks<=100:
    print("grade :A")
 elif marks>=80 and marks<=89:
    print("grade: B")
 elif marks>=70 and marks<=79:
    print("grade: C")  
 elif marks>=60 and marks<=69:
    print("grade :C") 
 else:
    print("grade: F")
      
print(f"the av is {av(mark)}")