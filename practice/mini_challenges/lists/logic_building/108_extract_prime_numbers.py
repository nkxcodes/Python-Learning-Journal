
# Question:
# Create a new list containing only the prime numbers from the original list

list1 = [2, 4, 5, 6, 7, 9, 11, 12, 13, 15]

prime_numbers = []

for element in list1:
    prime = True
    for number in range(2, 6):
        if element % number == 0:
            prime = False
    
    if prime == True:
        prime_numbers.append(element)

print(prime_numbers)