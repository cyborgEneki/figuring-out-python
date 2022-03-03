import math
numbers = [-3, -4, -6, -2]
largest_number = -math.inf
# largest_number = numbers[0]

for item in numbers:
    if item > largest_number:
        largest_number = item
print(largest_number)