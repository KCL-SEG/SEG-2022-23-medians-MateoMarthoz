"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1: # Odd number of elements
        return sorted_numbers[length // 2]
    else: # Even number of elements
        middle1 = sorted_numbers[length // 2 - 1]
        middle2 = sorted_numbers[length // 2]
        return (middle1 + middle2) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

median = find_median(numbers)
print(f"The median is: {median}")
