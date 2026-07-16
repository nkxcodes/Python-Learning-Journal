# Question:
# Ask the user to enter a sentence, split it into words, then replace every occurrence of one user-specified word with another.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

print(f'List: {words_list}')

want_to_replace = input('Which word do you want to replace?: ')

replace_with = input('Replace it with?: ')

for index in range(0, len(words_list)):
    if words_list[index] == want_to_replace:
        words_list[index] = replace_with

print(f'Updated List: {words_list}')