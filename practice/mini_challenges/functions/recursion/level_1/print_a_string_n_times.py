# Print a string n times.

def print_string(u_string, n):
    if n == 0:
        return

    print_string(u_string, n - 1)
    print(u_string)

print_string('I love programming', 5)