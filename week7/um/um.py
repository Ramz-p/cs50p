import re
import sys


def main():
    try:
        print(count(input("Text: ")))
    except ValueError:
        sys.exit("Invalid input")


def count(s):
    # Using regular expression to find the occurrences of "um" as a whole word
    um_pattern = r'\bum\b'
    um_matches = re.findall(um_pattern, s, re.IGNORECASE)

    # Returning the count of matches
    return len(um_matches)


if __name__ == "__main__":
    main()
