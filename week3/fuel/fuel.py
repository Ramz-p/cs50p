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
            fuel = (values[0] / values[1]) * 100

            # Determine fuel level category
            if fuel <= 1:
                level = "E"
            elif 1 < fuel < 99:
                level = f"{round(fuel)}%"
            elif 99 <= fuel <= 100:
                level = "F"
            else:
                continue

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

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
