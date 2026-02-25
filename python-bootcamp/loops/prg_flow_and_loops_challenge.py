"""
Challenge #1
Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.
"""

usr_num = int(input('Enter a num: '))
divisor = usr_num -1
while divisor != 0:
    if usr_num % divisor != 0:
        divisor -= 1
        continue
    else: 
        print(f'The divisor of {usr_num} is {divisor}')
        divisor -= 1

# Solution #2
x = int(input("Enter a number: "))
all_divisors = list()
for i in range(2, x//2+1):
    if x % i == 0:
        all_divisors.append(i)

print(all_divisors)


"""
Challenge #2
Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.

Input: 16, 2

Output: 2 ** 4 = 16
"""

big_num = int(input('Enter a big number: '))
small_num = int(input('Enter a small number: '))
n = 0
while small_num ** n <= big_num:
    if big_num != small_num ** n:        
        n +=1
        continue
    else:
        print(f' {small_num} in power of {n} is {big_num}')
        break
else:
    print(f'no matchin power fo {small_num} is found to make it {big_num}')

# Solution # 2

big_num = int(input('Enter a big number: '))
small_num = int(input('Enter a small number: '))

for i in range(2, big_num // 2):
    if small_num ** i == big_num:
        print(f'The exponent for {small_num} is {i} and equals {big_num}')
    else:
        pass

"""
Challenge #3
Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
"""
vovels = 'eyuioa'
count = 0
usr_input = input('Enter a string: ')
for v in usr_input:
    if v in vovels.lower():
        count += 1
print(count)

# Solution 2
vovels = 'eyuioa'
count = 0
usr_input = input('Enter a string: ')
for v in vovels:
    if v in usr_input.lower():
        count += usr_input.count(v)

print(f'Total number of vowels: {count}')

"""
Challenge #4

Write a Python script that checks if a triangle is equilateral, isosceles or scalene.

The user will be prompted for the triangle sides.

Note:

An equilateral triangle is a triangle in which all three sides have the same length.

An isosceles triangle is a triangle that has two equal sides.

A scalene triangle is a triangle that has three unequal sides.



Input: Enter the lengths of the triangle sides:

x: 6

y: 8

z: 12

Expected Output: Scalene triangle.
"""
x = int(input("X: ")) # Or like this: a, b, c = input('Enter the lengths of the triangle sides [Example: 10 20 30]:').split()
y = int(input("Y: "))
z = int(input('Z: '))

while bool(x) and bool(y) and bool(x):
    if x == y == z:
        print('equilateral')
    elif x == y or x == z or y == z:
        print('isosceles')
    else:
        print('scalene')
    break

    