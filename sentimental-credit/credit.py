# TODO
from cs50 import get_int

def main():
    num = get_int("Number: ")
    noOfDigits, multiplied, notMultiplied, firstNumber, secondNumber, i = 0, 0, 0, 0, 0, 0
    while True:
        noOfDigits += 1
        if num < 10:
            firstNumber = num
            if i % 2 == 1:
                num = num * 2
                if num > 9:
                    num = sumDigits(num)
                multiplied += num
            elif i % 2 == 0:
                notMultiplied += num
            break
        if num < 100:
            secondNumber = num % 10
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
    firstTwoDigits = (firstNumber * 10) + secondNumber

    if sum % 10 == 0:
        if firstNumer == 4:
            if noOfDigits == 13 or noOfDigits == 16:
                print('VISA')
            else:
                print('INVALID')

def sumDigits(n):
    return ( n % 10) + ( n // 10)

main()