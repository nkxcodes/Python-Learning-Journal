# Return Total Consonants

def total_consonants(u_string):
    vowels = ['a', 'e', 'i', 'o', 'u'
              'A', 'E', 'I', 'O', 'U']
    consonants = 0
    for ch in u_string:
        if ch not in vowels:
            consonants += 1
    return consonants

result = total_consonants('PROGRAMMING')

print(result)