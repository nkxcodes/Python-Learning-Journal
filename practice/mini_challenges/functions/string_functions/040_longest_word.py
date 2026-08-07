# Return longest word.

def find_longest_word(u_string):
    splited_string = u_string.split()
    longest_word_length = 0
    longest_word = ''
    
    for word in splited_string:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
            longest_word = word

    return longest_word

result = find_longest_word('Programming is awesome')

print(result)
