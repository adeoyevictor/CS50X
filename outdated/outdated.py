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
        dt = input("Date: ").strip()
        try:
            month, day, year = dt.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            pass
        else:
            if check(day, month):
                continue
            break
        try:
            month_day, year = dt.split(', ')
            month, day = month_day.split(' ')
            month = month.capitalize()
            for i in range(len(months)):
                if month == months[i]:
                    month = i + 1
            month = int(month)
            day = int(day)
            year = int(year)
        except:
            pass
        else:
            if check(day, month):
                continue
            break
    frmt(year, month, day)



def frmt(year, month, day):
    if month < 10:
        month = f"{month:02}"
    if day < 10:
        day = f"{day:02}"
    print(year, month, day, sep="-")

def check(day, month):
    return day > 31 or day < 1 or month > 12 or month < 1


main()