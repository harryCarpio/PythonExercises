# Create a Python function that accepts any number of numbers as positional arguments and prints the sum of those numbers.
def sum(*numbers):
    sum = 0

    for number in numbers:
        sum = sum + number

    return sum


print("Sum:", sum(3, 5, 6, 1, 2, 3))
