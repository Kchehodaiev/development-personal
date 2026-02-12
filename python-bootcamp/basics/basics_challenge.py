a = 1

b = 0.3
c = True
d = 'John'
print(a, b, c, d)

# Change this script so that it follows the Python naming and style conventions described in PEP8.

my_name = 'Andrei'
value = 100


# This is 
# an example of a multiline
# comment in Python.


hello_str = 'Hello'
print(hello_str)

# This script contains some syntax errors.
# Modify the script so that it runs without any errors.

best_friend = 'Anne'
print('My best friend is:', best_friend)

age = 18
age -=8
print(age)

a, _4b = 10, 20
print(a + _4b)

print('To comment a line of code you') # at the beginning of the line.

# Consider the following Python expression: a = 16 / 2 + 6 / 2  2

# Add parenthesis to change the order of operations so that a is 1.0

a = (16 / (2 + 6) / 2) 
print(a)

# An IPv6 address is represented using 128 bits.

# Write a Python script that calculates how many IPv6 addresses are available. You can also include reserved IP addresses.
ipv6_no = 2 ** 128
print('There are', ipv6_no, 'IPv6 available in the world!')


# A company's revenue is 45,897,513.

# Calculate the company's profit if the profit represents 12.7% of the revenue.

# Display the profit using 2 decimal places.
revenue = 45_897_513
print(revenue)

profit = revenue * 12.7 / 100
print(round(profit, 2))



# A junior Python programmer writes the following code snippet and gets surprised that the comparison operator returns False instead of True.

# a = 0.1
# b = 0.3
# print(a * 3 == b) # => False
# Your job is to modify the code so that the comparison returns True which is correct.

from math import isclose
a = 0.1
b = 0.3
print(isclose(a * 3, b))