"""Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.

Example Usage

num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)
Example Output:

9 # Explanation: 4 + 2 + 3 = 9
4 
"""

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    return sum 
    


num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))