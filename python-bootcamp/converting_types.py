# Converting Types
# We can convert between types using the built-in functions int(), float(), str(), etc.

# Example: Convert the miles to Km based on the user input
# miles = input('Enter distance in miles:')
# float_miles = float(miles) # Convert the input string to a float
# km = float_miles * 1.60934 # Convert miles to kilometers
# print(round(km, 2)) # Round the result to 2 decimal places and print it

# OR we can do it in one line
# km = round(float(input('Enter distance in miles:')) * 1.60934, 2) # Convert the input string to a float, convert miles to kilometers, round the result to 2 decimal places, and assign it to km
# print(km)

# int => float

a = 10
b = 3.14
c = '8.2'
a_float = float(a) # Convert integer to float
print('The type of a_float is:', type(a_float)) # <class 'float'>

# float => int
b_int = int(b) # Convert float to integer (truncates the decimal part)
print('The type of b_int is:', type(b_int), 'and the value is:', b_int) # <class 'int'>

# float => str

b_str = str(b)
print('The type of b_str is:', type(b_str), 'and the value is:', b_str) # Returns <class 'str'>

# str => float
c_float = float(c)
print('The type of c_float is:', type(c_float), 'and the value is:', c_float) # <class 'float'>

# str => int
c_int = int(float(c)) # Convert string to float first, then to integer
print('The type of c_int is:', type(c_int), 'and the value is:', c_int) # <class 'int'>