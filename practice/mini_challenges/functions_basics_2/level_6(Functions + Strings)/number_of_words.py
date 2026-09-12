# Write a function that counts the number of word in a sentence.

def count_words(u_sentence):
    word_list = u_sentence.split()
    count = 0
    for word in word_list:
        count += 1
    return count

result = count_words('I love programming')

print(result)