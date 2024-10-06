
def is_harshad(number):
    # Convert the number to a string to get its digits
    digits = [int(digit) for digit in str(number)]
    
    # Calculate the sum of digits
    digit_sum = sum(digits)
    
    # Check if the number is divisible by the sum of its digits
    return number % digit_sum == 0

# Example usage
num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
