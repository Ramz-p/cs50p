import re

def main():
    # Get user input for hours
    print(convert(input("Hours: ")))

def convert(s):
    # Define regular expression for matching time ranges in the format HH:MM AM/PM
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"

    # Use regex to match the entire input string
    match = re.search(r"^" + regex + " to " + regex + "$", s)

    if match:
        # Extract components of the matched time range
        from_time = standardize(match.group(1), match.group(2), match.group(3))
        time = standardize(match.group(4), match.group(5), match.group(6))

        # Return the standardized time range
        return f"{from_time} to {time}"
    else:
        # Raise a ValueError if the input does not match the expected format
        raise ValueError

def standardize(hr, min, x):
    # Standardize the hour, minute, and AM/PM components
    if hr == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+12}"

    # Set minute to "00" if it is not provided
    if min is None:
        minute = "00"
    else:
        minute = f"{int(min):02}"

    # Return the standardized time in HH:MM format
    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()
