# Question:
# Ask the user to enter a sentence, split it into words, and count how many times each word appears.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

processed = []

for word_n in words_list:
    if word_n in processed:
        continue
    count = 0
    for word in words_list:
        if word_n == word:
            count += 1
    print(f'{word_n}: {count}')
    count = 0
    processed.append(word_n) 