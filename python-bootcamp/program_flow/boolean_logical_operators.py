# and or not
# AND operator
age = 6
print(age > 0 and age < 18) # returns True can be also written like '0 < a < 18' but that's not readable
age = 20

print(age > 0 and age < 18) # returns False if at least one of the statements is False

name = 'Daniel'.lower()
print(age > 0 and age < 28 and name == 'daniel') # returs True
print(age > 0 and age < 28 and 'Danny' in name) # returns False bcuz Danny substr is not in name string value

# OR operator
age, name = 6, 'Daniel'
print(age < 5 or name == 'Daniel') # Returns true as long as at least 1 of expressions is True. 

# NOT operator
# the not operator will simply negate the expressions truthy value. Truthy value reverted.
2 == 2 # retuns True
not 2 == 2 # returns False.
age = 6
name = 'Daniel'
print(not age > 20) # True
print(age < 18 and not name == 'Josh') # returns True

print(not age == 6 or name.lower() == 'daniel') # True
print(not (age == 6 or name.lower() == 'daniel')) # If you want to negate the entirte expression use ()