def bid_adieu(names):
    # Determine the number of names
    length = len(names)

    # Construct farewell message based on the number of names
    if length == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif length == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"
        return farewell


def main():
    # Initialize an empty list to store names
    names = []

    try:
        # Gather names until control-d is pressed
        while True:
            name = input("Enter a name: ")
            names.append(name)
    except EOFError:
        # Control-d pressed, construct and print farewell message
        farewell_message = bid_adieu(names)
        print(farewell_message)


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
