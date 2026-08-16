# Factorial using recursion

def factorial_of(number):
    if number == 0:
        return
    
    print(number)
    factorial_of(number - 1)

factorial_of(10)