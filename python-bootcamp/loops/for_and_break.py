# for, else and break statements

for number in range(10):
        if number == 5:
            break # will break the entire loop only if condition is met
        print(number)
#### exit() # Exit function stops the entire script
print('outside of For loop')


for letter in 'PYTHON'.lower():
    if letter == 'o':
        print(f'breaking out, letter is {letter}')
        break
    print(letter)


# else statements:

