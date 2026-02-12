# Floating point in python is represented as a binary 

print(0.125 == 1/10 + 2/100 + 5/1000) # comparison "==" operator returns true.
print(format(10/3, '.20f')) # Formatting the float to 20 digits after the coma
print(round(10/3, 20)) # Rounding the number to 20 digits and returns float


a = 0.1 * 3
b = 0.3

print (a == b) # Comaprison character returns False bcuz 0.1 * 3 in python is in fact an infinite binary representation. See below:
print(a) # Returns 0.30000000000000004 instead of 0.3, so in fact, "a != b"

from math import isclose # Importing isclose function from math module. isclose is basically comparing 2 floats or digits neglecting their float difference.
x = 0.000001
y = 0.000002
# for small numbers we use absloute tolerance (abs_tol)
print('The x and Y are identical:', isclose(x, y, abs_tol=0.0001)) 

a = 99999.01
b = 99999.02
# for big numbers we use relative tolerance (rel_tol)
print(isclose(a, b, rel_tol=0.001))

print(0.3 == 0.1 * 3)
print(0.1 * 3)

import math
a = 0.3
b = 0.1
print(math.isclose(a, b * 3 ))