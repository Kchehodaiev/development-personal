movie = 'The Kingdom of Heaven'
# String slicing allows us to extract a portion of a string by specifying a range of indices. 
# The syntax for string slicing is string[start:end], where start is the index of the first character to include in the slice, and end is the index of the first character to exclude from the slice.
print(movie[0:3]) # prints the first three characters, which is 'The'

# If we omit the start index, it defaults to 0, and if we omit the end index, it defaults to the length of the string.
print(movie[:3]) # prints the first three characters, which is 'The'
print(movie[4:]) # prints the characters from index 4 to the end of the string, which is 'Kingdom of Heaven'
print(movie[-2:]) # prints the last two characters of the string, which is 'en'
print(movie[:-2]) # prints the string except for the last two characters, which is 'The Kingdom of Heav'

# movie[:1] + movie[1:] is equivalent to movie, because it concatenates the first character of the string with the rest of the string.
print(movie[:1] + movie[1:]) # prints 'The Kingdom of Heaven'

# Slicing has also a step value which if not specified defaults to 1, but if specified it will skip n-1 characters in the string.
print(movie[0:5:2]) # prints every second character from index 0 to 4, which is 'TeK'
print(movie[::2]) # prints every second character from the entire string, which is 'TeKndmo evn'
print(movie[::-1]) # prints the string in reverse order, which is 'nevaeH fo modgniK ehT'