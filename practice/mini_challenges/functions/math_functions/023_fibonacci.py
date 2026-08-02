# Return first N fibonacci numbers

def fibonacci_of(number): # Fibonacci function that takes a number and generate fibonacci series of that number
    num_1 = 0 # num_1 intialisation
    num_2 = 1 # num_2 initialisation
    result = 0 # result initialisation
    if num_1 == 0 and num_2 == 1: # if num_1 == 0 and num_2 == 1 then print both num_1 and num_2
        print(num_1)
        print(num_2)
    for num in range(number + 1): # run a loop till user given number + 1
        result = num_1 + num_2 # result will be num_1 + num_2
        print(result) # print the result
        num_1, num_2 = num_2, result # then num_1 value will be num_2 value and num_2 value will be result's value

fibonacci_of(10) # Functions invocation
