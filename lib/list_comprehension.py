#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]
# Example usage
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)




##...
def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
# Example usage
result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)  # Output: ["Hello!", "I'm doing great!", "Python is fun!"]