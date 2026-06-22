"""
Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.

Example Usage

words = ["vengeance", "darkness", "batman"]
concatenate(words)

words = []
concatenate(words)
Example Output:

"vengeancedarknessbatman"
"""

def concatenate(words):
	new_str = ""
	for word in words:
		new_str = new_str + word
	return new_str

words = ["vengeance", "darkness", "batman"]
print(concatenate(words))

words = []
print(concatenate(words))