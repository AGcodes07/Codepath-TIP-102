"""
Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.


Example Usage

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)
Example Output:

[1, 2, 3, 4, 5]
[1, 2, 2, 5, 8]
"""

def delete_minimum_elements(hunny_jar_sizes):
    result_list = []
    while hunny_jar_sizes:
        result_list.append(min(hunny_jar_sizes))
        hunny_jar_sizes.remove(min(hunny_jar_sizes))
    return result_list

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

