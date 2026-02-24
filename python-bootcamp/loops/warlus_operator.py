# Warlus operator allow assign a variable and output it's value in 1 line of code

# print(x = 2 + 3) Will get a type error - can not assign variables inside the print function

print(x := 2 +3) # will assign a variable a value resulting in expression AND output 5


# prompt the user for an input until he enters smth:
"""
usr_input = input('Enter smth: ')
while usr_input != '':
    usr_input = input('Enter smth: ')
"""
# Another way (line 10 and line 11 from the previous code are comprised in one line 16 - more cleaner and readable code):

while (usr_input := input('Enter smth:')) != '':      # calling for user input, assigning the value of user input to us_input var using warlus operator, and then comparing the result of the expression with an empty string
    usr_input = input('Enter smth: ')


# Print how many characters in a username
"""
usr_name = input('Enter your name: ')
if len(usr_name) > 0:
    print(len(usr_name))
"""
# Other was to do that with while:

while (usr_name := input('Enter your name: ')): # Prompting a user for an input -> assigning the input to variabe -> checking the truthy value of this variable in one line.
    print(bool(usr_name)) # Checking truthy value of usr_name (not empty) True
    print(len(usr_name))

# another way to do it with if stmt and warlus operator:

data = input('enter name: ')
if (n := len(data)) > 0:
    print(f'your name is {data} and it\'s {n} length')