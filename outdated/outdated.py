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

#         if '/' in dt:
#
#             frmt(year, month, day)
#         elif ',' in dt:
#
#             month = month.capitalize()
#             day = day[:-1]
#             for i in range(len(months)):
#                 if month == months[i]:
#                     month = i + 1
#                     frmt(year, month, day)

#         else:
#             pass



def main():
    while True:
        try:
            dt = input("Date: ")
            month, day, year = dt.split('/')
        except:
            pass
        
        try:
            month, day, year = dt.split(' ')
        except:



# def frmt(year, month, day):
#     print(year, month, day, sep="-")

main()