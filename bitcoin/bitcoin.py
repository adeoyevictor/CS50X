import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Invalid CL Arguments")

try:
    n = float(sys.argv[1])
except:
    sys.exit("Invalid Amount")

