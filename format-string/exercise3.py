# Code to illustrate the format() function's merge feature

medicine = 'Coughussin'
dosage = 5
duration = 4.5

istructions = '{} - Take {} ML by mouth every {} hours.'.format(
    medicine, dosage, duration)
print(istructions)