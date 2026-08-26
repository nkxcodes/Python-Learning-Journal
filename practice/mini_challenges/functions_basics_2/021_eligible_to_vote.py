# Write a function that takes a person's age and prints whether they are sligible to vote.

def is_eligible(age):
    if age > 18 and age < 90:
        return 'You are eligible to vote'
    else:
        return 'You are not eligible to vote'