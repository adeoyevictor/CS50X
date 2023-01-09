import sys

if len(sys.argv) == 2 and sys.argv[1].strip().endswith('.py'):
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#")
    except FileNotFoundError:
        sys.exit("An Error Occured")

else:
    sys.exit("Invalid File")
