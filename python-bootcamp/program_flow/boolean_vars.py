# Bollean variable is a subclass of int class

print(issubclass(bool, int)) # true. We can check that
"""
Bollean constants:
True # 1 in int
False # 0 in int
"""

print(int(True)) # returns 1
print(int(False)) # returns 0

print(id(True)) # returns the same address as below
print(id(5>3)) # returns the same address as above

print((4>3) == True) # returns True
print((4 > 3) is True) # Returns True


print(True == 1) # returns True bcuz the value is the same
print(True is 1) # returns False bcuz the address of True is not the same as the address of 1
print(id(True), id(1)) # returs different addresses in RAM

print(3 == False) # False
print(0 == False) # True

print('4' == 4)

a, b = 1, 3

print(a>b, b<a)
print(a>b, b == 3)

True > False # Returns True bcuz 1 is greater than 0

# Since booleans are in fact integers you can call all methods that type 'int' has, and also do arihphmetic operations

print(True + True) # Returns 2, bcuz True = 1.

#####################################################################################################################

# Truthiness of objects / Truthy value

var1 = 'string smth'

if var1:
    print(f'truthy value for var1 is {bool(var1)}') # Truthy value is True when the string or int is not empty or not 0 respectively
else:
    print(f'truthy value for var1 is {bool(var1)}') # False value if the string or int is empty or 0 respectively


c = 1

print(f'Truthy value of c is {bool(c)}')

