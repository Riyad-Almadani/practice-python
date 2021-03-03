price = float(input('How much did you pay: '))

if price >= 1.00:
    tax = 0.07

else:
    tax = 0
print('Tax rate is: ' + str(tax))