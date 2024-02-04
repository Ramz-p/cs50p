from datetime import date
import inflect
import sys
import operator

# Initialize the inflect engine for converting numbers to words
p = inflect.engine()

def main():
    try:
        # Get the user's date of birth as input
        dob = input("Date of Birth: ")

        # Calculate the difference in days between today and the provided date of birth
        difference = operator.sub(date.today(), date.fromisoformat(dob))

        # Convert the difference in days to a string representation in words
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(time):
    # Convert the time difference in days to minutes
    minutes = time * 24 * 60

    # Convert the number of minutes to words
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()
