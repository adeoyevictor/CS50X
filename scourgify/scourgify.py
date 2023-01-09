import sys
import csv

students = []

if len(sys.argv) == 3 and sys.argv[1].strip().endswith('.csv') and sys.argv[2].strip().endswith('.csv'):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {}
                student["first"] = row["name"].split(", ")[0]
                student["last"] = row["name"].split(", ")[1]
                student["house"] = row["house"]
                students.append(student)
    except FileNotFoundError:
        sys.exit("An Error Occured")

else:
    sys.exit("Invalid Files")





with open(sys.argv[2], "a") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    for s in students:
        writer.writerow(s)