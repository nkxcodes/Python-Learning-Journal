# Return duplicate characters.

def find_duplicate_characters(u_string):
    processed = []
    non_dup_string = ''

    for ch in u_string:
        if ch in processed:
            continue
        else:
            non_dup_string += ch
            processed.append(ch)

    return non_dup_string

result = find_duplicate_characters('Programming')

print(result)
