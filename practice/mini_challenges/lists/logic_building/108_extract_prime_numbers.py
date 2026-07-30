
# Question:
# Create a new list containing only the prime numbers from the original list

list1 = [2, 4, 5, 6, 7, 9, 11, 12, 13, 15]

prime_numbers = []


for index in range(0, len(list1)):
    prime = True
    for number in range(2, list1[index] - 1):
        if list1[index] % number == 0:
            prime = False
            break
    if prime:
        prime_numbers.append(list1[index])

print(prime_numbers)