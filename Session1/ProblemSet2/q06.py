"""
Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. Return the squared list.

Example Usage

numbers = [1, 2, 3]
squared(numbers)
Example Output:

[1, 4, 9]
"""

def squared(numbers):
	new_list = []
	for number in numbers:
	    new_list.append(number*2)
	return new_list

numbers = [1, 2, 3]
print(squared(numbers))
    