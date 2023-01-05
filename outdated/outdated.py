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
elif ',' in dt:
    month, day, year = dt.split(' ')
    day = day[:-1]

