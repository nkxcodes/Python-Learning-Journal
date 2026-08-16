
def countdown(n):
    if n == 0:
        print('Lift Off!')
        return
    
    print(n)
    countdown(n - 1)

countdown(10)

def sum_of_n(n):
    total_sum = 0 
    if n == 0:
        print('End of the Program')
        return
    total_sum += 1
    print(total_sum)
    sum_of_n(n - 1)

sum_of_n(10)
    