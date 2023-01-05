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
    while True:
        dt = input("Date: ")
        if '/' in dt:
            month, day, year = dt.split('/')
            frmt(year, month, day)
        elif ',' in dt:
            month, day, year = dt.split(' ')
            month = month.capitalize()
            day = day[:-1]
            for i in range(len(months)):
                if month == months[i]:
                    month = i + 1
            frmt(year, month, day)
        else:
            pass

def frmt(year, month, day):
    print(year, month, day, sep="-")


main()