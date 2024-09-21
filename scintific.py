import math as m
def calculator():
    while True:
     a=int(input("enter first number "))
     b=int(input("enter second number "))
     c=str(input("choose operation +,*,-,/,sqrt,exp,log,sin,cos,tan"))
     if c=='+':
      print(f"the result is {a+b}")
     elif c=='-':
      print(f"the result is{a-b}")
     elif c=="*":
      print(f"the result is {a*b}")
     elif c=='sqrt':
       a=m.sqrt(a)
       b=m.sqrt(b)
       print(a)
       print(b)
     elif c=='cos':
       a=m.cos(a)
       b=m.cos(b)
       print(a)
       print(b)
     elif c=='sin':
       a=m.sin(a)
       b=m.sin(b)
       print(a)
       print(b) 
     elif c=='tan':
       a=m.tan(a)
       b=m.tan(b)
       print(a)
       print(b) 
     elif c=='log':
       a=m.log2(a)
       b=m.log2(b)
       print(a)
       print(b)
     elif c=='exp':
       a=m.exp(a)
       b=m.exp(b)
       print(a)
       print(b)
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
 
