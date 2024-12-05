weekday = 0
day = 0
month = 0
year = 1900
sum = 0

def daysThisMonth(month, year):
    if month in [0, 2, 4,6,7,9,11]:
        return 31
    if month in [3,5,8,10]:
        return 30
    if month == 1:
        if (year % 4 == 0 and (year % 400 == 0 or (not year % 100 == 0))):
            return 29
        else: return 28
    raise Exception("Month not found")

while (year < 2001):
    if weekday == 6 and day == 0 and year >= 1901 and year <= 2000:
        sum += 1
    #advance to the next day
    weekday = (weekday + 1) % 7
    day = (day + 1) % daysThisMonth(month, year)
    if day == 0:
        month = (month + 1) % 12
        if month == 0:
            year += 1
print(sum)
