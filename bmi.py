w=float(input("enter your weight in kgs"))
h=float(input("enter your height in meters "))
if w<0 or h<0:
    print("invalid input negative number")
else :
 bmi=w/(h**2)
 if bmi < 18.5:
    print(f"your bmi is {bmi} and you are underweight")
 elif bmi>18.5 and bmi <=24.9:
    print(f"your bmi is{bmi} and you have healthy weight ")
 elif bmi>25.0 and bmi<=29.9:
    print(f"your bmi is {bmi} and you are overweight ")

 else:
    print(f"your bmi is {bmi} and you have obesity ")


