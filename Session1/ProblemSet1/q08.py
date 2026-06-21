"""
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...

Example Usage

tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(tasks)

tasks = []
print_todo_list(tasks)
Example Output:

Pooh's To Dos:
1. Count all the bees in the hive
2. Chase all the clouds from the sky
3. Think
4. Stoutness Exercises

Pooh's To Dos:

"""

def print_todo_list(tasks):
	print("Pooh's To Dos:")
	for i, task in enumerate(tasks):
		print(f"{i+1}. {task}")
	
tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(tasks)

tasks = []
print_todo_list(tasks)