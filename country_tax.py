country = input('What country do you live in? ')

if country.lower() == 'canada':
    province = input('What province/state do you live in? ')

    if province in ('Alberta', 'Nunvut', 'Yukon'):

        tax = 0.05
        print(tax)
    elif province == 'Ontario':
        tax = 0.13
        print(tax)
    else:
        tax = 0.15
        print(tax)
else:
    tax = 0.0
    print(tax)
