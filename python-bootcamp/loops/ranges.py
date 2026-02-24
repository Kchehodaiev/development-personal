# Ranges - is basically a sequence
r = range(2, 10) # to declare a sequence
print(r) # outputs nothing
print(type(r)) # class of range
print(list(r)) # outputs a list of integers [2, 3, 4, 5, 6, 7, 8, 9]

r = range(2, 10, 3) # 3 is a step here
print(list(r)) # will output [2, 5, 8]

print(list(range(0, 11, 2))) # print out only even numbers in a list including '10'

print(list(range(7, 40, 7))) # print out divisible numbers by 7 from 0 to 40

# count a sum from all the numbers in the ranger. Note that it's not necessary to get a list from the ranger. sum function knows how to deal with ranges
s = sum(range(1, 1001)) 
print(s)

# Summary 

# 1. We call the ranger func with 1 argument. In this case it's range(stop) 
# 
#and range function generates a sequence of numbers from 0 to the argument specified excluded: range(5) # is [0, 1, 2, 3, 4]

# 2. range(start, stop) --> range(1, 6) is [1, 2, 3, 4, 5]

# 3, range(start, stop, step) --> range(1, 10, 2) ## output [1, 3, 5, 7, 9]
print(list(range(1, 10, 2)))

print(list(range(12, -2, -3))) # go in reverse order with a step of 3
print(list(range(12, -2, 3))) # empty list

## YOUR CODE STARTS HERE

list1 = list(range(-10, 100, 3))
print(list1)

list2 = list(range(99, -4, -2))
print(list2)

