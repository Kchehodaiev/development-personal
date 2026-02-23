# A loop means execute smth repetitevely

# FOR LOOPS
for letter in 'Python and Java':
    print(letter)

for list in [1, 2, 3]:
    print(list)

for tuple in (5, 6, 7):
    print(tuple)

for set in {'f', 8, 'abc'}:
    print(set)

# Create a script that outputs only vowels from a given string

my_str = input('Enter a string: ').lower() # Prompt a user for a string and make it lowecase
vowels = 'auioye' # Define vowel letters
for vow in my_str: # Create a loop that iterates over each element of the string and checks if this element is a part of 'vowels' string
    if vow in vowels:
        print(vow, end = ' ')

for n in [1, 2, 3]:
    print('#')
print(n)


c = 0
for i in 'abc xyz':
    c = c+1
print(c)

# sum all numbers in a range of 100 
s = 0
for n in range(11):
    s +=n
    print(n)
print(f'the summed is {s}')


# Picking up a random winner
import random

names = [
    'anna',
    'josh',
    'Wiener',
    'dick',
    'prick'
]

# in python we can use '_' as an iteration variable as we will not use it anywhere else outside the loop.
# basically we use '_' iteration var to say how many times the loop should execute.
for _ in range(3): 
     
    print(f'Choosed a winner in round {int(_ + 1)}...')
    winner = random.choice(names)
    print(winner)
    names.remove(winner)