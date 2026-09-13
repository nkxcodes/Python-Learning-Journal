# Write a function that finds the longest word in a sentence.

def longest_word(u_string):
    words_list = u_string.split()
    longest_word = ''
    length = len(words_list[0])

    for word in words_list:
        if len(word) >= length:
            longest_word = word
            length = len(word)

    return longest_word

result = longest_word('I love python programming')

print(result)