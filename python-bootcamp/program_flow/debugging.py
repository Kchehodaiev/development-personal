a = 10
x =5
print(a, x)
for n in [1, 2, 3, 4, 5, 6]:
    print(type(n))
    nn = n * 2
    print(type(nn))
    if nn % 2 == 0:
        print(f'the value {nn} is even')
    else:
        print(f'the value of {nn} is odd')


print(a)