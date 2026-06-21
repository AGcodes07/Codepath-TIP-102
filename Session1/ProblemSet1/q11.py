"""
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r removed from it.


Example Usage

s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
Example Output:

"suspcous"
""
"Hunny"
"""

def tiggerfy(s):
	new_str = ""
	for char in s: 
		if char not in "tigerTIGER":
			new_str = new_str + char
	return new_str

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
        	

