def calculator():
    while True:
     a=int(input("enter first number "))
     b=int(input("enter second number "))
     c=str(input("choose operation +,*,-,/ "))
     if c=='+':
      print(f"the result is {a+b}")
     elif c=='-':
      print(f"the result is{a-b}")
     elif c=="*":
      print(f"the result is {a*b}")
     elif b==0:
       print("denominator should not be 0")
     else:
       print(f"the result is {a/b}")
     y=input("do you want to perform another calcualtion ? (YES/NO): ").upper()
     if y=='NO':
      print("bye")
      break
     else : 
      print("ok")
calculator()
 
