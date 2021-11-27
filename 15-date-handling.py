from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Format LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Format USA: {my_str}')

my_str = my_datetime.strftime('We are in the year %Y')
print(f'Format Random: {my_str}')