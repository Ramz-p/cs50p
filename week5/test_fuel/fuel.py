# fuel.py

def main():
    # Call fuel_lvl() and print the result in the main function
    print(fuel_lvl())

def fuel_lvl():
    level = ""
    while True:
        # Get values from user input using check_values()
        values = check_values()
        try:
            # Calculate fuel level percentage
            fuel = convert(values[0], values[1])

            # Determine fuel level category
            level = gauge(fuel)

            # Break the loop if calculation is successful
            break

        except ZeroDivisionError:
            continue

    # Return the calculated fuel level
    return level

def check_values():
    while True:
        # Get user input as a list and try to convert to integers
        user_input = input("Enter a fuel fraction (X/Y): ").split("/")
        try:
            user_input[0], user_input[1] = int(user_input[0]), int(user_input[1])

            # Break the loop if conversion is successful
            break

        except ValueError:
            continue

    # Return the user input as integers
    return user_input

def convert(x, y):
    # Calculate and return the percentage
    if not isinstance(x, int) or not isinstance(y, int) or x > y:
        raise ValueError("Invalid input")
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return round((x / y) * 100)

def gauge(percentage):
    # Determine and return the fuel level category
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
