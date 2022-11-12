import sys
import re
from cs50 import get_int
def main():

    num = input("Number: ")
    noOfDigits = len(num)
    firstNumber = int(num[0:1])
    secondNumber = int(num[1:2])
    firstTwoDigits = int(num[0:2])
    num = int(num)

    multiplied, notMultiplied, i = 0, 0, 0
    while True:
        if num < 10:
            if i % 2 == 1:
                num = num * 2
                if num > 9:
                    num = sumDigits(num)
                multiplied += num
            elif i % 2 == 0:
                notMultiplied += num
            break
        digit = num % 10
        num = num // 10
        if i % 2 == 1:
            digit = digit *2
            if digit > 9:
                digit = sumDigits(digit)
            multiplied += digit
        elif i % 2 == 0:
            notMultiplied += digit
        i += 1
    sum = multiplied + notMultiplied
    if sum % 10 == 0:
        if firstNumber == 4:
            if noOfDigits == 13 or noOfDigits == 16:
                print('VISA')
            else:
                print('INVALID')
        elif firstTwoDigits == 34 or firstTwoDigits == 37:
            if noOfDigits == 15:
                print('AMEX')
            else:
                print('INVALID')
        elif firstTwoDigits == 51 or firstTwoDigits == 52 or firstTwoDigits == 53 or firstTwoDigits == 54 or firstTwoDigits == 55:
            if noOfDigits == 16:
                print('MASTERCARD')
            else:
                print('INVALID')
        else:
            print('INVALID')
    else:
        print('INVALID')
def sumDigits(n):
    return ( n % 10) + ( n // 10)
main()