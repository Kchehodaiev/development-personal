# Conditional statemenets
# Ex1
balance = 200
price = 155

if balance >= price:
    answer = input('Continue, yes or no?: ')

    if answer.lower() == 'yes':
        print('We\'ll continue')
        print(f'You are good, and will have {balance - price}$ after the charge')
    elif answer.lower() == 'no':
        print('We stop!')
    else:
        print('Invalid answer')
        
else:
    print(f'Insufficient funds. You are lacking {price - balance}$')


print('Other instructions, not part of If/else statement') # if we indent this line to the level of previous command it would fall under else stmt

#Ex2

# answer = input('Continue, yes or no?: ')

# if answer.lower() == 'yes':
#     print('We\'ll continue')
# elif answer.lower() == 'no':
#     print('We stop!')
# else:
#     print('Invalid answer')

age = 20
if age in '20 years':
   print('He is 20 years old')
else:
   print('He is not 20 years old')