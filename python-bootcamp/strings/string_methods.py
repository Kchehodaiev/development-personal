# String methods
# String methods are essentially a functions attached to each object data type (str, int, float, set, dictionary, etc).
# Meaning there specific methods for each datatype.

# print(), len(), type(), sum(), max(), main(), round() etc these are regular functions, not methods

# 'dfdfsf'.  First method to call all available string methods - just type a literal string, then dot and then there will be a dropdown.

# print(dir(str)) # second method to output all avail method for a data type of string
# help(str.capitalize)  # to call a help function of the specifed method for the specified datatype. 

s = 'Python'
print(s)
s = 'Java'
s_upper = s.upper() # calling an upper method to output the string value in upper case. !!! VARIABLE VALUE ITSELF DOESNT CHANGE, IT"S STILL 'Python', bcuz strings are immutable. It just returns this output.
print(s, s_upper)
s = s.upper()

print('proGRAming'.lower()) # will return 'programing'

# Most useful string methods

my_str = 'Let\'s go FAZe'
# 1. str.upper() Makes all capitalized

print(my_str.upper())
# 2. str.lower() Makes all lower case
print(my_str.lower())

# 3. str.strip() By default removes whitespaces at the beginning and the end of the string
ip = '   192.168.01  '
ip = ip.strip()
print(ip)

# You can also give this method an argument what it has to replace/strip

value = '$$$455$3453$$$$'

print(value.strip('$')) # Will return 455$3453 as it only removes specifed stuff from the beginning and end of the string.

# 4. str.replace() Takes 2 arguments and replaces a substring that contains 1st argument with a second one

new_value = value.replace('$', '#')
print(new_value) # ###455#3453####

# 5 str.count() Returns the number of occurence of the specific substring in a string

txt = 'I love PytHon, pYthon is great!'
n = txt.lower().count('python') # 2
print(n)

# 6. str.split() Splits a string into a list where by default each word of a string is a list item

my_list = txt.split()
print(my_list) # ['I', 'love', 'PytHon,', 'pYthon', 'is', 'great!'] By default it uses spaces, tabs and new lines as a delimiter
# But you can pass it a customer delimiter:
print('1.2.3.4'.split('.')) # ['1', '2', '3', '4']

# 7. str.join() makes the opposite of split - it joins the lists to the string.

ip = '1.2.3.4'
ip_list = ip.split('.') # ['1', '2', '3', '4']
print(ip_list)

ip_joined = 'xxxxx'.join(ip_list) # 1xxxxx2xxxxx3xxxxx4
print(ip_joined)
# 8. str.find Find the index of the substring beginning

my_str = 'I love PytHon, pYthon is great!'

print(my_str.find('love')) # returns '2' as index of the beginning of this substring is 2


# 9. 'in' a bolean operator that returns True if certain substring exists in string or not

print('love' in my_str) # True

# 10. 'not in' same the the prior one just reversed

#  11. str.removeprefix() & str.removesuffix()

url = 'https://example.com'
cleaned_url = url.removeprefix('https://')
first_lvl_domain = url.removeprefix('https://').removesuffix('.com')

print(cleaned_url, first_lvl_domain) # example.com example

s = 'pYThoN'
print(s.capitalize())

print('py' in 'Python'.lower())
print(':'.join('abc'))

f = 'foo'
b = 'bar'
print('barf' in 3 * (f + b))