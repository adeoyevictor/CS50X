months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

dt = input("Date: ")

if '/' in dt:
    month, day, year = dt.split('/')
    format(year, month, day)
elif ',' in dt:
    month, day, year = dt.split(' ')
    day = day[:-1]
    for i in range(len(months)):
        if months[i] == month.capitalize():
            month = i + 1
    format(year, month, day)

def format(year, month, day):
    print(year, month, day, sep="-")


