# Python has a function called input() to capture user's input

name = input('Enter your name:')
print('your name\'s:', name)
print(type(name))

# input function always captures the user input as a string/str, so you can't use it in ariphmetical operations unless you convert it

total_qnty = input('Enter the quantity:')
price = input('Enter a price')
# total_price = price * total_qnty # Will return TypeError: can't multiply sequence by non-int of type 'str'

# Need to convert it using either int or float functions 

total_price = float(total_qnty) * float(price)
print(total_price)