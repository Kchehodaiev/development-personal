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
weight = float(input('Enter your fat-ass kg:'))
height = float(input('Enter your hieght in meters:'))
bmi = weight / (height ** 2)
print('Your BMI is:', round(bmi, 2)) 
# Or like this:
print('Your BMI is: ', format(bmi, '.2f'))
