# A loop means execute smth repetitevely

# FOR LOOPS
for letter in 'Python':
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