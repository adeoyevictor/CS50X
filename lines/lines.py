import sys

lines = 0

if len(sys.argv) == 2 and sys.argv[1].strip().endswith('.py'):
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") :
                    pass
                elif not line.strip():
                    pass
                else:
                    lines += 1
    except FileNotFoundError:
        sys.exit("An Error Occured")

else:
    sys.exit("Invalid File")

print(lines)