weight_input = input('What is your weight? ')
units = input('(L)bs or (K)gs? ')

if units.upper() == 'L':
    weight_output = float(weight_input) * 0.45
    print(f'You are {weight_output} kilos.')
elif units == 'K' or units == 'k':
    weight_output = float(weight_input) / 0.45
    print(f'You are {weight_output} pounds.')
else:
    print('Invalid weight. Please put a number.')