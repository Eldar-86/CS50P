import sys
import requests


api_request = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=d63f9f832523e154bd98139692f694c5dd35e081f43515ce3ba067787019f678").json()


try:
    if len(sys.argv) < 2:
        print("Missing command-line argument")
        sys.exit(1)
    elif sys.argv[1].isalpha():
        print("Command-line argument is not a number")
        sys.exit(1)
    else:
        if api_request["data"]["priceUsd"]:
            result = float(api_request["data"]["priceUsd"]) * float(sys.argv[1])
            print(f"${result:,.4f}")
except (ValueError, requests.RequestException):
    sys.exit(1)
