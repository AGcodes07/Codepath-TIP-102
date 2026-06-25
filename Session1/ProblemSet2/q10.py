"""Write a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the number of odd numbers minus the number of even numbers in the list.

Example Usage

lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
Example Output:

1
3
-4"""

def up_and_down(lst):
    odd_new_list = []
    even_new_list = []
    full_new_list = []
    for nums in lst:
        if nums % 2 == 0:
            even_new_list.append(nums)
        else:
            odd_new_list.append(nums)
        full_new_list = len(odd_new_list) - len(even_new_list)
    return full_new_list
    
lst = [1, 2, 3]
print(up_and_down(lst))