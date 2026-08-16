# Print "Hello" exactly n times.

def print_hello(n):
    if n == 0:
        return

    print('Hello')
    print_hello(n - 1)

print_hello(5)