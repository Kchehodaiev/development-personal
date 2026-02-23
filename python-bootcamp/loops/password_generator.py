import random
import string
chars = string.ascii_uppercase + string.digits + string.punctuation

# pw_length = 12 

# or via user input

pw_length = int(input('Enter a password length:'))

password = ''

for _ in range(pw_length):
    add_on = random.choice(chars)
    password += add_on

print(f'{password}')