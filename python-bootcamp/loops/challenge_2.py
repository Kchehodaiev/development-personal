"""
Challenge #5
Write a Python program that calculates and displays the sum, the product and the average of n float numbers entered by the user, each on a separate line. 

Enter 0 to finish.
"""
numbers = list()
while True:
    usr_input = float(input("Enter a num: "))
    if usr_input == 0:
        break
    else:
        numbers.append(usr_input)
print(numbers)
# Sum
print(sum(numbers))
numbers
# Product/Multiplication using math module
import math
product = math.prod(numbers)
print(product)

# Product Solution #2 using built-in for loop
product = 1
for n in numbers:
    product *= n
print(product)
# Average

print(len(numbers))

print(avg := sum(numbers) / len(numbers))

"""
Challenge #6
Given the string s1, write a program to return the sum and the average of the digits that appear in the string, ignoring all other characters.

Input: Python31py50

Output: Sum: 9, Average: 2.25
"""
import string
clean_num = list() # declaring an empty list that would contain numbers only;
print(numbers := string.digits) # assiging numbers var with a numbers: 0123456789
usr_inp = input('Enter a string: ') # prompting for user input '123dft'
for num in numbers: # iterating over numbers
    if num not in usr_inp: # comparing num var if it's not in usr_inp string
        continue # if it's not - continue to next iteration
    else:
        clean_num.append(num) # if it's part of user string - add this number to the list but the iterables are strings ['1', '2', '3']
print(num_float := list(map(float, clean_num))) # converting to float; prints out [1.0, 2.0, 3.0] as each element here is float
print(sum(num_float)) # print out the sum of clean_num list
print(sum(num_float) / len(clean_num)) # print our the avg

# Solution #2
total, count = 0, 0
for char in input('Enter a string: '):
    if char.isdigit():
        total += float(char)
        count += 1
print(f'total sum is {total}, and avg is {total / count}')


