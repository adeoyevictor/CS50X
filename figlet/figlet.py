import sys

txt = input("Input: ")

if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    pass
else:
    sys.exit("Invalid arguments")

