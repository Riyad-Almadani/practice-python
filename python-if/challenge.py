prompt = input('Would you like to continue? ')
if prompt == 'no' or prompt == 'n':
    print('Exiting')
elif prompt == 'yes' or prompt == 'y':
    print('Continuing ...')
    print('Complete!')
else:
    print('Plese try again and respond with yes or no.')