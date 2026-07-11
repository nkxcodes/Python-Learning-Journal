# Question:
# Ask the user to enter a sentence, split it into words, and count how many words start with a vowel.

sentence = input('Enter a Sentence: ')

words_list = sentence.split()

count = 0

for word in words_list:
    if (word[0] == 'a' or
        word[0] == 'e' or
        word[0] == 'i' or
        word[0] == 'o' or
        word[0] == 'u'):
        count += 1
    else:
        continue

print(f'Words Starting With Vowel: {count}')