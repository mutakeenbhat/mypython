def is_armstrong(number):
    # Convert the number to a string to calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    return armstrong_sum == number

# Prompt the user to enter the range (a and b)
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

# Check for Armstrong numbers in the range
print(f"Armstrong numbers between {a} and {b} are:")
for number in range(a, b + 1):
    if is_armstrong(number):
        print(number)

