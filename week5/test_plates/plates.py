# plates.py

def main():
    plate = input("Enter a license plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6 or not s.isalnum():
        return False

    if s.isalpha():
        return True
    else:
        if s[:2].isalpha() and s[-1].isdigit():
            for char in s:
                if char.isdigit():
                    if char.startswith("0") or s[s.index(char):].isalpha():
                        return False
                    else:
                        return True
            return False  # Added to handle cases where there is no digit in the string
        else:
            return False

if __name__ == "__main__":
    main()
