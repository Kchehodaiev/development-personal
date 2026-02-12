# String concat and repetition
# + => the concatenation operator
movie = 'Gay Sex in the City'
director = 'Michael Bay'
movie_director = movie + ' was directed by ' + director
print(movie_director)
# or print function can take multiple arguments and concatenate them with a space in between
print('was directed by', 'michael bay', '123') # This will concatenate the two strings with a space in between, resulting in 'was directed by michael bay 123'

# * => the repetition operator

# in python you can not concatenate a string with an integer, you need to convert the integer to a string first
language = 'Python'
version = 3.10
# print(language + version) # This will raise a TypeError because we cannot concatenate a string with a float.
print(language + ' ' + str(version)) # This will concatenate the string 'Python' with the string representation of the float 3.10, resulting in 'Python 3.10'. Or you can use f-strings to achieve the same result in a more concise and readable way.
print(f'{language} {version}') # This will also print 'Python 3.10

# * operator can be used to repeat a string a certain number of times
print((movie + ' ') * 5) # This will print the value of the variable movie 5 times
print('#' * 50) # This will print the character '#' 50 times, resulting in a line of 50 '#' characters