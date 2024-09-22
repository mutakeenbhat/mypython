count_amar=0
count_fakeer=0
print("vote for your fav candidate ")
while True:
 print("1.amar")
 print("2.fakeer")
 a=input("enter the name to vote for your candidate: (amar/fakeer ) ").lower()
 if a=='amar':
  count_amar+=1
  print(f"the votes for amar is {count_amar}")  
 elif a=='fakeer':
   count_fakeer+=1
   print(f"the vote for fakeer is{count_fakeer} ")
 else:
  print("enter a valid name ")
 again = input("Do you want to vote again? (yes/no): ").lower()
 if again != 'yes':
  break  # Exit the loop if the user doesn't want to vote again
print(f"the vote is for amar is {count_amar} and for fakeer is {count_fakeer}")
