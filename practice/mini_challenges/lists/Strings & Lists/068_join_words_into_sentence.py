# Question:
# Create a list of words and join them together into a single sentence.

words = ['I', 'Love', 'Python', 'Programming']

sentence = ''

for word in words:
    sentence += ' ' + word

print(f'Sentence: {sentence}')