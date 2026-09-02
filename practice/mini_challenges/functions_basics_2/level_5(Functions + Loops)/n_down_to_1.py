# Write a function that counts from n down to 1.

def down_to(n):
    for num in range(n, 0, -1):
        print(num)

down_to(10)