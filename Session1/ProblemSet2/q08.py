"""
Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.

Example Usage

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
Example Output:

[1, 4, 6]

"""
def find_villain(crowd, villain):
	new_list = []
	for i, char in enumerate(crowd):
		if char == villain:
			new_list.append(i)
	return new_list

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))