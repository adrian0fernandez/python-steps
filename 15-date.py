import datetime

def utc():
    my_time = datetime.datetime.now()
    print(my_time)


def my_day():

    my_day = datetime.date.today()
    print(my_day)

def my_time():

    my_time =datetime.date.today()
    print(f'Year: {my_time.year}')
    print(f'Month: {my_time.month}')
    print(f'Day: {my_time.day}')


utc()
my_day()
my_time()