# Return Greatest Common Divisor 

def find_gcd(num_1, num_2):
    gcd = 0
    for number in range(1, num_1 + 1):
        if num_1 % number == 0 and num_2 % number == 0:
            gcd = number
    return gcd

result = find_gcd(24, 36)

print(result)