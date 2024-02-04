def main():
    # Initialize an empty dictionary to store grocery items and their counts
    grocery = {}

    try:
        while True:
            # Prompt user to input grocery items (press Ctrl-D to end input)
            item = input()

            # Check if the lowercase version of the item is already in the grocery dictionary
            if item.lower() in grocery:
                # If yes, increment the count for that item
                grocery[item.lower()] += 1
            else:
                # If not, add the item to the dictionary with count 1
                grocery[item.lower()] = 1
    except EOFError:
        # When Ctrl-D is pressed, call the function to print the grocery list
        print_grocery(grocery)

def print_grocery(grocery):
    # Iterate over the keys (sorted alphabetically) in the grocery dictionary
    for key in sorted(grocery.keys()):
        # Print the count and the uppercase version of the item
        print(f"{grocery[key]} {key.upper()}")

if __name__ == "__main__":
    main()
