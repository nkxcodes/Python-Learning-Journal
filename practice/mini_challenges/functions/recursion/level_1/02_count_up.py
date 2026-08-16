# Print numbers from 1 to n using recursion.

def count_up(number):
    if number == 0:
        return
    
    count_up(number - 1)
    print(number)

count_up(10)