
expense={}
while True:
 amount=input("enter the amount spend or type 'exit' ")
 if amount.lower()=='exit':
  break
 else:
  discription=input("enter the discription ")
  expense[amount]=discription
  print(f" current expence is :{expense}")
print("final expense",expense)