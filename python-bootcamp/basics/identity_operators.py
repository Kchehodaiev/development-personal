# Identity operators "is" & "is not" | returns True or False

a, b = 3, 4
print(a is b)

# immutable types: int, float, str, tuple, frozenset
# Mutable types: list, dict, set

print(id(a))

a += 3

print(id(a))

numbers = [1, 2, 5]

print(id(numbers))

numbers.append(7)
print(numbers)
print(id(numbers))

nums = numbers.copy() # Creating a new list by copying the existing one calling a copy method.s
print(nums == numbers) # Comparison operator returns True bcuz these variables have the same values.
print(nums is numbers) #  Identity operator returned False bcuz these are 2 different identities and saved in different memory address