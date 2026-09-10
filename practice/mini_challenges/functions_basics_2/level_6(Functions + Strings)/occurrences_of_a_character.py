# Write a function that counts occurrences of a character.

def count_occurrence(u_string, character):
    count = 0
    for ch in u_string:
        if character == ch:
            count += 1
    return count

result = count_occurrence('Programming', 'm')

print(result)