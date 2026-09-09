# Write a function that checks whether a string is a palindrome.

def is_palindrome(u_string):
    palindrome = False
    if u_string == u_string[::-1]:
        Palindrome = True
    else:
        Palindrome = False
    return Palindrome

result = is_palindrome('MAAM')

print(result)