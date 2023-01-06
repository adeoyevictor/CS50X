import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
lst = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(lst)
    figlet.setFont(font=f)
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid arguments")

txt = input("Input: ")

print(figlet.renderText(txt))