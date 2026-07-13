# Question:
# Given a list containing some empty strings, remove all empty strings from the list.

string_list = ['String', 'Student', '', 'Atman', '', 'Brahman', '', '', '', 'Atman', '', 'is', 'Brahman']

for index in range(len(string_list) - 1, -1, -1):
    if string_list[index] == '':
        string_list.remove(string_list[index])

print(f'List: {string_list}')