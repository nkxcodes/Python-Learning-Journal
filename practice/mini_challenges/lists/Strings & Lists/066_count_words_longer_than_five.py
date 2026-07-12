# Question:
# Ask the user to enter a sentence, split it into words, and print only the words that contain more than five characters.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

count = 0

for word in words_list:
    if len(word) > 5:
        count += 1

print(f'Words longer than five: {count}')