# coke.py

def main():
    # Initialize variables to track the amount inserted and the cost of a Coke
    amount_inserted = 0
    coke_cost = 50

    # Continue prompting the user to insert coins until enough is inserted
    while amount_inserted < coke_cost:
        # Prompt the user to insert a coin
        coin = input("Insert a coin (25, 10, or 5 cents): ")

        # Check if the input is a valid coin denomination
        if coin in ["25", "10", "5"]:
            # Convert the input to an integer and add it to the amount inserted
            amount_inserted += int(coin)
            # Output the amount due only if the cost is not reached
            if amount_inserted < coke_cost:
                print("Amount Due:", coke_cost - amount_inserted)
        else:
            # Ignore invalid input and inform the user
            print("Amount Due:", coke_cost - amount_inserted)

    # Calculate and output the change owed
    change = amount_inserted - coke_cost
    print("Change Owed:", change)

if __name__ == "__main__":
    main()
