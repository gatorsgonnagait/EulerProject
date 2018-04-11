
# jan 31
# feb 28
# mar 31
# apr 30
# may 31
# jun 30
# jul 31
# aug 31
# sep 30
# oct 31
# nov 30
# dec 31

# leap year: any year divisible by 4, not on a century unless divisible by 400
# how many sundays were on first day of month from 1901 to dec 31 2000
days31keys = dict.fromkeys(range(1,32))
days30keys = dict.fromkeys(range(1,31))
febkeys = dict.fromkeys(range(1,29))
leapfebkeys = dict.fromkeys(range(1,30))


def generate_year():
    return {
        1: days31keys,
        2: febkeys,
        3: days31keys,
        4: days30keys,
        5: days31keys,
        6: days30keys,
        7: days31keys,
        8: days31keys,
        9: days30keys,
        10: days31keys,
        11: days30keys,
        12: days31keys
    }

def generate_leap_year():
    return {
        1: days31keys,
        2: leapfebkeys,
        3: days31keys,
        4: days30keys,
        5: days31keys,
        6: days30keys,
        7: days31keys,
        8: days31keys,
        9: days30keys,
        10: days31keys,
        11: days30keys,
        12: days31keys
    }

def is_leap_year(year_num):
    if year_num%4 == 0 :
        if year_num%400==0:
            return True
        elif year_num%100==0:
            return False
        return True
    return False


def dayConverter(string_day):
    switch = {
        'Sunday':1,
        'Monday':2,
        'Tuesday':3,
        'Wednesday':4,
        'Thursday':5,
        'Friday':6,
        'Saturday':7
    }
    return switch.get(string_day)


def sunday_counter(start_year, end_year, weekday):

    day_of_week = dayConverter(weekday)
    sunday_the_first_count = 0

    for  year_num in range(start_year, end_year+1):


        if is_leap_year(year_num):

            years = generate_leap_year()
        else:
            years = generate_year()


        for month in years:

            for day in years[month]:

                if day_of_week == 8:
                    day_of_week = 1

                if day == 1 and day_of_week == 1: # first day of month is sunday

                    sunday_the_first_count += 1

                day_of_week += 1

    return sunday_the_first_count





print(sunday_counter(1901, 2000, 'Monday'))


