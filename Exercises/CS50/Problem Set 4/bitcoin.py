import requests
import sys
import json


try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    elif isinstance(float(sys.argv[1]), float):
        btc_num = float(sys.argv[1])

        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=cb3adb97b9cdac7c22fc7155421a4614ab4caf243651cc8e1794ecceece3d87e"
            )
        btc_response = response.json()

        btc_price = float(btc_response["data"]["priceUsd"])
        btc_purchase_cost = btc_num * btc_price

        print(f"${btc_purchase_cost:,.4f}")

    else:
        sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit()

except ValueError:
    sys.exit("Command-line argument is not a number")
