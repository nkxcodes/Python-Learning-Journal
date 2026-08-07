# Return shortest word.

def find_shortest_word(u_string):
    splited_string = u_string.split()
    shortest_word_length = len(splited_string[0])
    shortest_word = splited_string[0]

    for word in splited_string:
        if len(word) < shortest_word_length:
            shortest_word_length = len(word)
            shortest_word = word

    return shortest_word

result = find_shortest_word('Programming Is Awesome')

print(result)