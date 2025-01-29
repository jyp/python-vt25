# how old am i (in number of days)
# what is the number of days between two arbitrary dates (in the Gregorian calendar)

number_of_days_per_year = 365.2422
number_of_days_per_month = 30.5
def date_diff_approx(y1,m1,d1, y2,m2,d2 ):
    return (y2-y1)* number_of_days_per_year + (m2-m1) * number_of_days_per_month + (d2-d1)

# input("date?")

def is_divisible_by(k,n):
    return n % k == 0

def is_leap_year(y):
    if is_divisible_by(400,y):
        return True
    elif is_divisible_by(100,y):
        return False
    elif is_divisible_by(4,y):
        return True
    else:
        return False

assert(not is_leap_year(1700))
assert(not is_leap_year(1800) )
assert(not is_leap_year(1900))
assert(is_leap_year(1600))
assert(is_leap_year(2000))

def number_of_days_in_month(m,y):
    if m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    if m in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

def number_of_days_in_year(y):
    if is_leap_year(y):
        return 366
    else:
        return 365

def days_from_epoch(y,m,d):
    days = 0
    for year in range(1,y):
        days = days + number_of_days_in_year(year)
    for month in range(1,m):
        days = days + number_of_days_in_month(month,year)
    days = days + d
    return days

def date_diff(y1,m1,d1, y2,m2,d2):
    return days_from_epoch(y2,m2,d2) - days_from_epoch(y1,m1,d1)

# print("test one year:", date_diff(2024,1,27 ,2025,1,27))
# print("test one month:", date_diff(2025,1,27 ,2025,2,27))
# print("test one month: ", date_diff(2024,12,27 ,2025,1,27))

# print(date_diff(1978,12,15 ,2025,1,27))
