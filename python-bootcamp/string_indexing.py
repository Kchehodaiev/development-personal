movie = 'The Kingdom of Heaven'
print(movie[3]) # prints the fourth character, which is space
print(movie[2]) # prints out the third character, which is 'e'
print(movie[-1]) # Negative indexing starts from the end of the string, so -1 refers to the last character, which is 'n' in this case.


# What will happen if we try to access an invalid index

# print('Python'[10]) # This will raise an IndexError because the index is out of range.

# can use a len function to return the number of characters in a string, including spaces and punctuation.
print(len(movie))

s1 = 'Hello'
n = len(s1)
print(s1[n-1]) # prints the last character of the string, which is 'o'

# Strings are immutable, which means that we cannot change individual characters in a string. If we try to assign a new value to an index of a string, we will get a TypeError.
print(s1[0]) # prints 'H'
s1[0] = 'g' # This will raise a TypeError because strings are immutable and we cannot change individual characters.