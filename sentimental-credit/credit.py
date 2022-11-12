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
            multilplied += 





def sumDigits(n):
    return ( n % 10) + ( n // 10)

main()