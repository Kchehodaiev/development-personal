n = 1
while True:
    if n <= 4:
        print('va-mcc' + 'c'  * n)
        n += 1
    else:
        break

x = 0

while x < 10:
    print(f'x is {x}')
    x +=1
else:
    print(f'Loop ended, x is now {x}')
print('after the loop')

### While & continue statements ###
# Output all numbers divisible by 13 but less than 100
x =12
while x < 100:
    x+=1
    if x % 13 !=0:        
        continue
    print(x)


### While & break statements ###

while True:
    usr_num = int(input('Enter a num: '))
    lucky_num = 5
    if usr_num != lucky_num:
        continue
    else:
        print(f'Congrats you guessed the numnber! The lucky number is {lucky_num}')
        break


x = 5
s = 0
while x:
    x -= 1
    s += x
print(s)

n = 0
my_sum = 0
while n < 100:
    n = n + 1
    while n % 2 != 0:
        my_sum = my_sum + n
        break
else:
    print(my_sum)


n = 1
my_sum = 0

while n <= 100:
    my_sum += n
    n += 2

print(my_sum)