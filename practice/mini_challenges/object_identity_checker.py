# Object Identity Checker
#
# Description:
# Check whether two variables refer to the same object in memory.
#
# Example:
# Variable A: [1, 2]
# Variable B: Variable A
#
# Output:
# Both variables refer to the same object.

a = [1, 2]
b = a

if a is b:
    print('Both variables refer to the same object')
else:
    print('Both variables not refer to the same object')
