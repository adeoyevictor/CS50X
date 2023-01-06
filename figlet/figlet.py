import sys

txt = input("Input: ")

if len(sys.argv) == 1:

elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):

else:
    sys.exit("Invalid arguments")

