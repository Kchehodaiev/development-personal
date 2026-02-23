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

for n in range(1, 10):
     if n % 13 == 0:
          print(f'the number {n} is divisible by 13, breaking out...')
          break
else:                               # Here 'else' stmnt pertains to for loop, not to 'if', and it will execute if the loop isn't broken and when the loop gets gets exhausted of the iterables.
     print(f'Loop exhaused iterables and ended')


for l in 'abc':
     print(l)
     for n in range(3):
        if n == 1:
            break
        print(n)


for letter in 'pythoooon!!!':
    if letter == 'o':
        break
    print(letter, end='')
else:
    print('Go!')


###### CHALLENGE #######
"""
Using a for loop and the range() function, calculate the sum and the product of the numbers between 1 and 25  (both included).
Store the calculated values in two variables called my_sum and my_product.
Print the values of my_sum and my_product variables.
"""
## starting variables

my_sum = 0
my_product = 1 

for i in range(1, 26):
    my_sum += i # add each no. in the range to my_sum
    my_product *= i # multiply each no. in the range by my_product


