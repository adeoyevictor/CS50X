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

def main():
    dt = input("Date: ")

    if '/' in dt:
        month, day, year = dt.split('/')
        frmt(year, month, day)
    elif ',' in dt:
        month, day, year = dt.split(' ')
        day = day[:-1]
        for i in range(len(months)):
            if months[i] == month.capitalize():
                month = i + 1
        frmt(year, month, day)

def frmt(year, month, day):
    print(year, month, day, sep="-")


main()