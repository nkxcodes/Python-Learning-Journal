# Write a function that checks whether a person passed or failed based on marks.

def check_passed_or_fail(marks):
    if marks >= 0 and marks < 33:
        return 'Failed'
    elif marks >= 33 and marks <= 100:
        return 'Passed'
    else:
        return 'Invalid Marks'

result = check_passed_or_fail(55)

print(result)