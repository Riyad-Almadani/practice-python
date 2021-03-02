today = input('Today\'s date? ')
print(today)

breakfast = input('Breakfast clories? ')
print(breakfast)

lunch = input('Lunch calories? ')
print(lunch)

dinner = input('Dinner calories? ')
print(dinner)

snack = input('Snack calories? ')
print(snack)

calorie = int(breakfast) + int(lunch) + int(dinner) + int(snack)
print(f'Colorie content for {today}: {calorie}')