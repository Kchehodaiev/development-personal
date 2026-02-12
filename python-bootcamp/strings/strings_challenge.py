# x = input('Enter x:')
# y = input('Enter y:')
# print(x * y) # will return error TypeError: can't multiply sequence by non-int of type 'str


# x = int(input('Enter x:'))
# print(x*2, type(x)) # will multiply bcuz we converted to int initially

# print(int(input('Enter:'))) # will print out ValueError: invalid literal for int() with base 10: 'a'

# a = '1.5'
# b = '2'
# #Using Type Casting create a new variable called c that stores the result of a multiplied by b. c stores a float and will be 3.0.

# c = float(a) * float(b)
# print(c)



# Calculate the BMI (Body Mass Index) based on the user input for weight in kg and height in meters. The formula for BMI is weight / (height ** 2). Display the result rounded to 2 decimal places.
# weight = float(input('Enter your fat-ass kg:'))
# height = float(input('Enter your hieght in meters:'))
# bmi = weight / (height ** 2)
# print('Your BMI is:', round(bmi, 2)) 
# # Or like this:
# print('Your BMI is: ', format(bmi, '.2f'))


"""
Consider the following string declaration which is part of the output of a Linux command.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

Try to solve the challenge in more than one way.
"""
# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# mac_str = my_str.removeprefix('wlo1 Link encap:Ethernet HWaddr').strip()

#print(mac_str) # prints out 'b4:6d:83:77:85:f3'

# Solution 2: Split the string into a list and return the last list element which is the MAC address
# mac = my_str.split()[-1]
# print('Solution 2. Mac is:',mac)


# Solution 3  to revert the string backwards and slice the reverted mac out.
# print(my_str[::-1])
# print(my_str[:-18:-1])
# reverted_mac = my_str[:-18:-1]
# mac = reverted_mac[::-1]
# print(mac)

# Solution 4
# print(my_str)
# print(len(my_str)) # 49 indexes
# mac = my_str[len(my_str) - 17:]
# print(mac)

# CHALLENGE 2 
"""
Display the following strings literally:

It displayed: "You've got an error!"
\n means a new line.
\ is known as the escape character.
"""

print('It displayed: "You\'ve got an error!"\n\\n means a new line.\n\\ is known as the escape character ')

# CHALLENGE 3

"""
Challenge #3

Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm

The user will be prompted to enter the value in ft.

Display the value in cm with 2 decimals, formatted using an f-string.
"""
# ft = input('Enter a value in ft:')

# print('feet value is:', ft)
# print(f'{ft}ft = {(float(ft) * 30.48):.2f} cm')

# Challenge 4
"""
Write a Python script that tests if a string is a palindrome.
"""
# mystr = input('Enter a string:')
# reverted_str = mystr[::-1]
# print(reverted_str)
# print(reverted_str == mystr)

# Challenge 5

"""
Change the solution of the previous challenge so that both the white spaces and the letter case are ignored when checking if the string is a palindrome.
"""
# mystr = input('Enter a string:')
# mystr = mystr.strip().lower()
# reverted_str = mystr[::-1]
# print(reverted_str)
# print(reverted_str == mystr)

# Challenge 6

"""
Write a Python script to get a string made of the first and the last 2 chars from a given string entered by the user.
"""
my_str = input('Enter a string:')

new_str = my_str[:2] + my_str[-2:]
print(new_str)

# Challenge 7 

"""
Write a Python program to get a string from a given string where all occurrences of its first character have been changed to '$'
except the first character itself.

Sample String: 'mama'

Expected Result: 'ma$a'
"""
