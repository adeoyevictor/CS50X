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
    print(json.dumps(res.json()['bpi']['USD'], indent=2))
except requests.RequestException:
    pass
