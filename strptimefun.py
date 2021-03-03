# Sometimes you recive the date as a string and need to convert it to
# a datetim object

from datetime import datetime, timedelta

birthday = input('When is your birthday(dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day befor birthday: ' + str(birthday_eve))
