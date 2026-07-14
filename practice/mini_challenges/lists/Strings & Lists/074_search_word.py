# Question:
# Ask the user to enter a sentence, split it into words, then search for a user-specified word and report whether it exists.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()


print(' ')
searched_word = input('Search a Word: ')

exists = False

for word in words_list:
    if word == searched_word:
        exists = True

if exists == True:
    print(f'{searched_word} Exists')
else:
    print(f'{searched_word} Does not Exists')