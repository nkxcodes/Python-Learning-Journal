
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

# We can add new items in list, using list.append()

even_numbers.append(34)
even_numbers.append(6 * 6)
print(even_numbers)

odd_numbers = even_numbers
print(id(odd_numbers) == id(even_numbers)) # They reference the same object
odd_numbers.append(37)

print(even_numbers)
print(odd_numbers)

# All slice operations return a new list containing the requested elements.
# This means that the following slice returns a shallow copy of the list.

correct_odd = even_numbers[:]
correct_odd[:] = [3, 5, 7, 9, 11, 13, 15, 17, 19]
print(correct_odd) 