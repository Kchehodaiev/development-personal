# For, continue and pass Statements
# here it will output everything except 'o' characters, as when letter = o it basically says stop iterating the below code and go to the beginning of the loop to the next iteration
for letter in 'let\'s go, Python, goooo':
    if letter == 'o':
        continue
    print(letter, end='') # output in the same line 'let's g, Pythn, g'


# print out odd and even numbers:

for n in range(10):
    if n % 2 == 0:
        print(f'the number {n} is even')
        continue
    print(f'the number {n} is odd')

# pass statement is basically a placeholder to "execute nothing". 

for k in range (10):
    pass # when no logic should be executed but the statement is required you just paste 'pass' stmnt.