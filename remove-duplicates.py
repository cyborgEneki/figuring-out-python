numbers = [3, 3, 5, 6, 2, 2]
uniques = []

for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)