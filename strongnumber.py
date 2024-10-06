import math as m
def is_fact(x):
    user_str=str(x)
    digit_sum=0
    for digit in user_str:
        digit_sum+=int(digit)
    return m.factorial(digit_sum)

user=int(input("enter a number"))
print(f"the sum of factorial is {is_fact(user)}")
    

