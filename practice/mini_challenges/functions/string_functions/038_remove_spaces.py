# Remove all spaces

def remove_spaces(u_string):
    result = ''
    for ch in u_string:
        if ch == ' ':
            continue
        else:
            result += ch
    return result

result = remove_spaces('P R O G R A M M I N G')

print(result)