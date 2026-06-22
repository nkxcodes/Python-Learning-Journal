
# A list is like container in which we can store many values together

even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(even_numbers)

print(even_numbers[0])
print(even_numbers[5])
print(even_numbers[0:6])
print(even_numbers[5:0:-1])

even_numbers += [22, 24, 26, 28, 30, 33] # last number is not even

# Solution 

even_numbers[-1] = 32 # Unlike strings, which are immutable, lists are mutable type

print(even_numbers)