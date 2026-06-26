
# Arithmetic Operators
    # Used for mathematical calculations

print(5 + 3) # Addition

print(5 - 3) # Subtraction

print(5 * 3) # Multiplication

print(5 / 2) # Division

print(5 // 2) # Floor Division

print(5 % 2) # Modulus(Remainder)

print(5 ** 2) # Exponentiation

# Comparison (Relational) Operators
    # Used to Compare Values

print(5 == 5) # Equal to

print(5 != 3) # Not Equal to

print(5 > 3) # Greater than

print(5 < 3) # Less than

print(5 >= 5) # Greater than or equal to

print(5 <= 3) # Less than or equal to

# Assignment Operators
    # Used to Assign Values to Variables
        # Other Assignment Operators: //=, %=, **=


x = 5
x += 5 
x -= 5
x *= 5
x /= 5
x //= 5
x %= 5
x **= 5

# Logical Operators
    # Used to Combine Conditions

if 5 > 3 and 5 == 5: # True and False -> False
    print('Hello')

if 5 > 3 or 5 == 5: # True or False -> True
    print('Hello')

if not 5 == 5: # not True
    print('Hello')

# Bitwise Operators 
    # Operate on binary numbers.

a = 5
b = 3

print(a & b) # Bitwise AND (&)

print(a | b) # Bitwise OR (|)

print(a ^ b) # Bitwise XOR (^)

print(~a) # Bitwise NOT (~)

print(5 << 1) # Left Shift (<<)

print(20 >> 2) # Right Shift (>>)

# Membership Operators
 # Check if a value exists in a sequence

print('a' in 'apple') # in

print('z' not in 'apple') # not in

# Identity Operators
    # Check whether two variables refer to the same object

a = [1, 2]
b = a
print(a is b) # is
print(a is not b) # not is