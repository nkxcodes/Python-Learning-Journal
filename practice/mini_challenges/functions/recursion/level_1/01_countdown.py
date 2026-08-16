# Print number from n down to 1 using recursion

def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number -  1)

countdown(10)