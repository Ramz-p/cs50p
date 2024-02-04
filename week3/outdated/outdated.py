from datetime import datetime

def main():
    while True:
        user_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ").strip()
        formatted_date = parse_date(user_input)

        if formatted_date:
            print(formatted_date)
            break
        else:
            print("Invalid date. Please enter a valid date.")

def parse_date(user_input):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    try:
        # Attempt to parse date in MM/DD/YYYY format
        date_obj = datetime.strptime(user_input, "%m/%d/%Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        pass  # Continue to the next parsing method

    try:
        # Attempt to parse date in Month Day, Year format
        date_obj = datetime.strptime(user_input, "%B %d, %Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        return None  # Parsing unsuccessful

if __name__ == "__main__":
    main()
