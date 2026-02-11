# Formatting strings with f-strings used to compose a new brand string from other strings and other data types. Formatted string literals
first_name = 'John'
last_name = 'Doe'
age = 30

print('Hello,' +  ' ' + first_name + ' ' + last_name + '.' + ' ' + 'You are' + ' ' + str(age) + ' years old.')

# Using f-strings, we can achieve the same result in a more concise and readable way.
print(f'Hello, {first_name} {last_name}. You are {age} years old.') # prints 'Hello, John Doe. You are 30 years old.' but more easily and more readable than the previous example with concatenation.

s = f'{2 * 3.6563:.2f}' # f-strings can also include expressions, which are evaluated at runtime and their results are included in the string. 2f here is used to format the result to 2 decimal places.
print(s) # prints '7.31' because the expression 2 * 3.6563 is evaluated and its result is included in the string.

# Fahrheit to Celsius conversion using f-strings. F = C * 1.8 + 32
celsius = 25.7
print(f'Temp in Farenheit is: {celsius * 1.8 +32:.3f}') # prints 'Temp in Farenheit is: 78.260' because the expression celsius * 1.8 + 32 is evaluated and its result is included in the string, formatted to 3 decimal places.

# F-strings with = for debugging. This will show the expression and its value.

name, age = 'John', 35
print(f'{name=} {age=}') # The output would be "name='John' age=35"

radius = 13.5
P = 3.141592
print(f'The Circle are with {radius=} is: {P * radius ** 2=:.2f}') # will return formated value up to 2 decimals after the floating point "The Circle are with radius 13.5 is: 572.56"

x = 2
y = 3
print(f'{x} - {y} = {x - y}') # will output "2 - 3 = -1" bcuz everythin's outside of expression {} is a string literal.

x = 23
y = 'hello'
answer = f'x, my name is {y}' # define a var which holds a formatted string.
print(answer) # print it out later

distance = 1100
print('The distance from London to Berlin is {distance/1.609} miles.')

name = 'Maria'
age = 40
city = 'Bucharest'
print(f'My name is {name}, ' + 'I am {age} old ' + 'and I live in {city}.' ) # prints out "My name is Maria, I am {age} old and I live in {city}." bcuz python evaluates only 'My name is {name}, ' as an f-string bcuz the closing single-quote, the rest is just a regular str bcuz it does not have an "f" in front of them

name = 'Maria'
age = 40
city = 'Bucharest'
print(f'My name is {name}, ' + f'I am {age} old ' + f'and I live in {city}.' ) # "Will print out My name is Maria, I am 40 old and I live in Bucharest." bcuz everything here is evaqluated as an F-string