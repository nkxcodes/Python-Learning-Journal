# Print numbers from n down to 1.

def down_to(n):
    if n == 0:
        return
    
    print(n)
    down_to(n - 1)

down_to(10)