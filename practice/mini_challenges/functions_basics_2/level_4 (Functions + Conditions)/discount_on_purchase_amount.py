# Write a function that calculates a discount based on purchase amount.

def calculate_discount(purchase_amount):
    discount = 0
    if purchase_amount >= 0 and purchase_amount <= 999:
        discount = 0
    elif purchase_amount >= 1000 and purchase_amount <= 4999:
        discount = (5 / 100) * purchase_amount
    elif purchase_amount >= 5000 and purchase_amount <= 9999:
        discount = (10 / 100) * purchase_amount
    elif purchase_amount >= 10000 and purchase_amount <= 19999:
        discount = (15 / 100) * purchase_amount
    elif purchase_amount >= 20000:
        discount = (20 / 100) * purchase_amount
    else:
        return 'Invalid Amount!'

    return purchase_amount - discount

result = calculate_discount(200000)

print(result)