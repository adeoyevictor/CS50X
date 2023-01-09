import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2 and sys.argv[1].strip().endswith('.csv'):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)


    except FileNotFoundError:
        sys.exit("An Error Occured")

else:
    sys.exit("Invalid File")

