# TODO
from cs50 import get_int

def main():
    num = get_int("Number: ")
    noOfDigits, multiplied, notMultiplied, firstNumber, secondNumber, i = 0,0,0,0,0,0
    print(noOfDigits, multiplied, notMultiplied, firstNumber, secondNumber, i)


def sumDigits(n):
    return ( n % 10) + ( n / 10)

main()