def main():
    plate = input("Enter a license plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length is between 2 and 6 characters, and if all characters are alphanumeric
    if 2 <= len(s) <= 6 and s.isalnum():
        # Return true if all characters are letters
        if s.isalpha():
            return True
        else:
            # Check for a number in the middle, only if the first 2 characters are letters and the last character is a number
            if s[:2].isalpha() and s[-2].isdigit():
                # Iterate through the characters in the string
                for char in s:
                    # Check if the character is a digit
                    if char.isdigit():
                        # Return false if the number starts with 0 or the following character is a letter
                        if char.startswith("0") or s[s.index(char):].isalpha():
                            return False
                        else:
                            return True
                return False  # Added to handle cases where there is no digit in the string
            else:
                return False
    else:
        return False

if __name__ == "__main__":
    main()
