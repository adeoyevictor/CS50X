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
        try:
            month, day, year = dt.split('/')
        except:
            pass
        else:
            break
        try:
            month, day, year = dt.split(' ')
            month = month.capitalize()
            day = day[:-1]
            for i in range(len(months)):
                if month == months[i]:
                    month = i + 1
        except:
            pass
        else:
            break
    frmt(year, month, day)



def frmt(year, month, day):
    if int(month) < 10:
        month = f"0{month}"
    if int(day) < 10:
        day = f"0{day}"
    print(year, month, day, sep="-")

main()