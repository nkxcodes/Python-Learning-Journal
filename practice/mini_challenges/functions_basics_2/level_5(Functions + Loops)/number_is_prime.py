# Write a function that checks whether a number is prime.

def is_prime(number):
    prime = True

    if number < 2:
        return False

    for num in range(2, (number // 2) + 1):
        if number % num == 0:
            prime = False
            break
        else:
            prime = True
        
    return prime

result = is_prime(5)

print(result)