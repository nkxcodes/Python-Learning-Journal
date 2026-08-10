# Return first non-repeating character.

def find_first_non_repeating_character(u_string):
    count = 0
    for ch in u_string:
        for index in range(0, len(u_string)):
            if ch == u_string[index]:
                count += 1
        if count == 1:
            return ch
    count = 0

result = find_first_non_repeating_character('Programming')

print(result)