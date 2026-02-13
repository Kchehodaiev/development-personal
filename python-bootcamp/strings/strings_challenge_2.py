# Challenge 7 

"""
Write a Python program to get a string from a given string where all occurrences of its first character have been changed to '$'
except the first character itself.

Sample String: 'mama'

Expected Result: 'ma$a'
"""
orig_str = input('Enter a string:')

first_char = orig_str[0]

new_str = orig_str[1:].replace(first_char, '#')
print(first_char + new_str)

"""
Challenge 8 
Write a Python script that removes the characters which have odd index values of a given string.
"""

odd_str = input('Enter a string:')
print(odd_str[::2])

"""
Challenge 9
Write a Python script that prompts the user for the radius of a circle and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
"""
rad = input('Enter a radius:')

area = 3.1415 * float(rad) ** 2
print(f'Area of radius {rad} circle is {area:.2f}')

"""
Write a Python script that finds the number of occurrences of a substring in a given string by ignoring the letter case.
"""
occur_str = input('Enter a string:')
sub_str = 'error'
n = occur_str.lower().count(sub_str)
print(n)

"""
Write a Python script that displays a number with a comma (,) as the thousands separator (US and UK format) 
and with a period(.) as the thousands separator (EU format).
"""
number = int(input('Enter a number:')) # User input that converts to an int
print(f'{number:,}') # using Python formatting to put ',' as a thousands separator (build-in formatting in Python automatically puts coma every 3 characters)
print(f"{number:,}".replace(",", ".")) # converting resulting integer with a replace method to put '.' instead of ','

n = 12384756982 # already an integer, no need to convert
n_comma = f'{n:,}' # build-in formatting in Python automatically puts coma every 3 characters

print(n_comma)
