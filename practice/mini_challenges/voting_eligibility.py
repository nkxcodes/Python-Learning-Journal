# Voting Eligibility Checker
#
# Description:
# Determine whether a person is eligible to vote based on their age.
#
# Example:
# Enter your age: 20
#
# Output:
# You are eligible to vote.

age = int(input('Enter your age: '))

if age > 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')