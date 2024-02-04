import sys
import requests

def get_bitcoin_price(bitcoin_amount):
    try:
        # Fetch Bitcoin price from CoinDesk API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an exception for bad response status

        # Parse JSON response
        data = response.json()
        rate_float = data["bpi"]["USD"]["rate_float"]

        # Calculate the cost of specified Bitcoins in USD
        cost_in_usd = bitcoin_amount * rate_float

        # Print the result with four decimal places and thousands separator
        print(f"The cost of {bitcoin_amount:.8f} Bitcoins is ${cost_in_usd:,.4f} USD")
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

def main():
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    # Get the number of Bitcoins from the command-line argument
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        print("Error: Invalid number of Bitcoins")
        sys.exit(1)

    # Get the current Bitcoin price and calculate the cost
    get_bitcoin_price(bitcoin_amount)

if __name__ == "__main__":
    main()
