# Question:
# Ask the user to enter a sentence, convert it into a list of words, and count the total number of words.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

count = 0

for word in words_list:
    count += 1

print(f'Count: {count}')