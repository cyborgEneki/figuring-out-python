numbers = [5, 2, 5, 2, 2]
length_of_outer_loop = len(numbers)
string = ''

for i in range(len(numbers)):
    for j in range(numbers[i]):
        string += 'x'
    print(string)
    string = ''
