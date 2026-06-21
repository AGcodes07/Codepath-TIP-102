"""
Session 1 - Problem Set 1 - Question 2
Hundred Acre Wood Greeting

Problem:
Write a function greeting() that accepts a single parameter,
a string name, and prints the string
"Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

Example Usage:
greeting("Michael")
greeting("Winnie the Pooh")

Example Output:
Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.
"""

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")


if __name__ == "__main__":
    greeting("Michael")
    greeting("Winnie the Pooh")
