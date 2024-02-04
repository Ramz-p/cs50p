import csv
import sys


def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Check if the input file has a .csv extension
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            # Call the clean function with the provided input and output file names
            clean(sys.argv[1], sys.argv[2])


def clean(input, output):
    try:
        # Open the input file
        with open(input) as input:
            # Create a CSV reader
            reader = csv.DictReader(input)

            # Open the output file for writing
            with open(output, "w") as output:
                # Specify the header for the output CSV file
                header = ["first", "last", "house"]
                # Create a CSV writer with the specified header
                writer = csv.DictWriter(output, fieldnames=header)
                # Write the header to the output file
                writer.writeheader()

                # Iterate through each student in the input CSV file
                for student in reader:
                    # Split the name into first and last
                    last, first = student["name"].split(", ")
                    # Extract the house information
                    house = student["house"]
                    # Write the cleaned data to the output CSV file
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()
