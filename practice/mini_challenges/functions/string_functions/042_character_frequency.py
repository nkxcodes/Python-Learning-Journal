# Return frequency of each character

def count_character_frequency(u_string):
    processed = []
    count = 0
    for ch in u_string:
        if ch in processed:
            continue
        else:
            for index in range(0, len(u_string)):
                if ch == u_string[index]:
                    count += 1
            processed.append(ch)
        print(f'{ch}: {count}')
        count = 0

result = count_character_frequency('Hello')

print(result)