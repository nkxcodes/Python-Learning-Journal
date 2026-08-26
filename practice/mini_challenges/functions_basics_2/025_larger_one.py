# Write a function that takes two numbers and prints the larger one.

def larger_one(n_1, n_2):
    if n_1 > n_2:
        return n_1
    else:
        return n_2

result = larger_one(98, 988)

print(result)