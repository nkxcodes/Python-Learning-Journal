
print('Hello World')

print('doesn\'t')

print('"oh", my god.')

s = "First line.\n Second line"

print(s)

print('C:\this\name') # here \t means tab, \n means newline

print(r'C:\this\name') # note the r before the quote

text = """Hello
World"""

print(text)

print("""\
    Usage: thingy [OPTIONS]
""")

s = """
Hello
"""

print(repr(s)) # python stores it like '\nHello\n'

print('Hello' + 'World')

print(3 * 'Hello' + 'World')

print('Py' 'thon')

string = (
    "Hello"
    "World"  # This is useful when we want to write long readable messages
)

print(string)

text = 'py'
text + 'thon' # text 'thon' this does not work!

# Strings can be indexed

word = 'Universe'
print(word[0])
print(word[5])

# Indices may also be negative numbers, which starts counting from right

word = 'Nature'
print(word[-1])
print(word[-5])