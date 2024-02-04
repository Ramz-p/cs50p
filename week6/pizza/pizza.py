import sys
import csv
from tabulate import tabulate


def load_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            return list(csv.reader(csvfile))
    except FileNotFoundError:
        sys.exit("File does not exist")


def print_table(data):
    headers = data[0]
    rows = data[1:]
    table = tabulate(rows, headers=headers, tablefmt="grid")
    print(table)


def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_path = sys.argv[1]

    # Check if the file has a .csv extension
    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    pizza_data = load_csv(file_path)
    print_table(pizza_data)


if __name__ == "__main__":
    main()
