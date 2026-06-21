"""
Session 1 - Problem Set 1 - Question 3
Catchphrases

Problem:
Write a function print_catchphrase() that accepts a string character
as a parameter and prints the catchphrase of the given character:

Pooh -> "Oh bother!"
Tigger -> "TTFN: Ta-ta for now!"
Eeyore -> "Thanks for noticing me."
Christopher Robin -> "Silly old bear."

If the given character does not match one of the characters above,
print "Sorry! I don't know <character>'s catchphrase!"

Example Output:
Oh bother!
Sorry! I don't know Piglet's catchphrase!
"""

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


print_catchphrase("Pooh")
print_catchphrase("Piglet")