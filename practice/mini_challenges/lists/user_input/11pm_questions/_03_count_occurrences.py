# ==========================================================
# Question 6: Count Occurrences
#
# Create a list containing some repeated values.
# Ask the user to enter a number.
# Count how many times that number appears in the list.
#
# Example:
# numbers = [2, 5, 2, 7, 2, 8]
#
# Input:
# 2
#
# Output:
# 2 appears 3 times.
#
# Try solving it without using list.count().
# ==========================================================

numbers = [2, 5, 2, 7, 2, 8]

num =  int(input('Enter Number to Count: '))

count = 0

for number in numbers:
    if num == number:
        count += 1

print(f'{num} appears {count} times')