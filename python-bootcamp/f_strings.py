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
