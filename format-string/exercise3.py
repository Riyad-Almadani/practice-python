# Code to illustrate the format() function's merge feature

medicine = 'Coughussin'
dosage = 5
duration = 4.5

istructions = '{} - Take {} ML by mouth every {} hours.'.format(
    medicine, dosage, duration)
print(istructions)

istructions = '{2} - Take {1} ML by mouth every {0} hours'.format(
    medicine, dosage, duration)
print(istructions)
