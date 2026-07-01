# ==========================================================
# Question 1
# Print the index and value of every element using enumerate().
#
# Example Output:
# 0 Apple
# 1 Mango
# 2 Banana
# ==========================================================

fruits = ['Apple', 'Mango', 'Banana']

for index, fruit in enumerate(fruits, start=0):
    print(f'{index} {fruit}')