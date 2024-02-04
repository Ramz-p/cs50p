# Menu of Felipe's Taqueria with prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_cost = 0.0  # Initialize total cost

    try:
        while True:
            # Prompt user for an item
            item = input("Enter an item (or press Ctrl-D to finish): ").title()

            # Check if item is in the menu
            if item in menu:
                total_cost += menu[item]  # Add item cost to total
                print(f"Total cost: ${total_cost:.2f}")
            else:
                print("Invalid item. Please choose from the menu.")

    except EOFError:
        print("\nOrder complete. Thank you!")

if __name__ == "__main__":
    main()
