# Return True if number is prime

def is_prime(number):
    prime = True
    for num in range(2, number - 1):
        if number % num == 0:
            prime = False
            break
    return prime

prime_check = is_prime(3)

print(prime_check)