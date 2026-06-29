# Last Digit Finder # 
# # Description: 
# # Find and display the last digit of a number using an operator. # # Example: # Enter a number: 9876 # # Output: # Last digit: 6

number = int(input('Enter a Number: '))

last_digit = number % 10

print(f'Last Digit: { last_digit}')