import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Invalid CL Arguments")

try:
    n = float(sys.argv[1])
except:
    sys.exit("Invalid Amount")


try:
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(f"{res.json()['bpi']['USD']['rate_float']:,.4f}")
except requests.RequestException:
    sys.exit("Request Error")
