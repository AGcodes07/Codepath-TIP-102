"""
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.

Example Usage:

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
Example Output:

"fluff with stuffed all cubby little tubby"
"Pooh"
"""
def reverse_sentence(sentence):
    word = sentence.split()
    new_sentence = ' '.join(word[::-1])
    return new_sentence

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))
