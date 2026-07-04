# Swap the first and last elements
 
numbers = [18, 42, 7, 91, 35, 12, 64, 29]

first_element = numbers.pop(0)

numbers.insert(0, numbers[-1])
numbers.pop(-1)
numbers.append(first_element)

print(numbers)