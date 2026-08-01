# Call functions using keywords arguments

def greet(name='Guest', country='N/A'):
    print(f'Hello {name} from {country}')

greet()
greet(country='India', name='Nitesh')
greet('Rahul') # Output: Hello Rahul from N/A
greet(country='Japan') # Output: Hello Guest from Japan
greet(name='Alice') # Output: Hello Alice from N/A
greet('Bob', 'Canada') # Output: Hello Bob from Canada
greet('Bob', country='Canada') # Output: Hello Bob from Canada

greet('Bob', country='Canada') # This is valid
# greet(name='Bob', 'India') # This gives an error becomes positional arguments cannot come after keyword arguments