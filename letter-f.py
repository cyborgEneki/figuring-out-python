numbers = [5, 2, 5, 2, 2]
length_of_outer_loop = len(numbers)
string = ''

for i in numbers:
    string = ''
    for j in range(i):
        string += 'x'
    print(string)
