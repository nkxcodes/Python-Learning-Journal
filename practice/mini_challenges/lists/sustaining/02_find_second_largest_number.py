# Question:
# Find second largest number

numbers = [4, 7, 2, 9, 7, 9, 5]

second_largest = numbers[0]

for element in numbers:
    if element < second_largest:
        second_largest = element

print(f'Second Largest: {second_largest}')

students = [
    {
        "name": "Nitesh",
        "age": "17"
    },
    {
        "name": "Mridul",
        "age": "17"
    }
]

print()
print(f"Name: {students[0]["name"]}")
print(f"Age: {students[0]["age"]}")

print()
print(f"Name: {students[1]["name"]}")
print(f"Age: {students[1]["age"]}")