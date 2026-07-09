"""
Write a function common_elements() that takes in two lists lst1 and lst2 and returns a list of the elements that are common to both lists.

Example 1:
Input: lst1 = ["super strength", "super speed", "x-ray vision"], lst2 = ["super speed", "time travel", "dimensional travel"]
Output: ["super speed"]

Example 2:
Input: lst1 = ["super strength", "super speed", "x-ray vision"], lst2 = ["martial arts", "stealth", "master detective"]
Output: []
Example Usage

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
common_elements(lst1, lst2)

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
common_elements(lst1, lst2)
Example Output:

["super speed"]
[]
"""

def common_elements(lst1, lst2):
    new_list = []
    for item in lst1:
        if item in lst2:
            new_list.append(item)
    return new_list 

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))