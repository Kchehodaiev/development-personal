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
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
mac_str = my_str.removeprefix('wlo1 Link encap:Ethernet HWaddr').strip()

print(mac_str) # prints out 'b4:6d:83:77:85:f3'
# Split the string into a list and return the last list element which is the MAC address
mac = my_str.split()[-1]
print(mac)
# Solution to revert the string backwards and slice the reverted mac out.
print(my_str[::-1])
print(my_str[:-18:-1])
# then we need to convert the resulted string to list and revert it back to string
reverted_mac = my_str[:-18:-1]
mac = reverted_mac[::-1]
print(mac)

# Solution 3
print(my_str)
print(len(my_str)) # 49 indexes
mac = my_str[len(my_str) - 17:]
print(mac)

