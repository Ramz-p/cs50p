def main():
    # Define a dictionary with fruit names as keys and their respective calories as values
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "kiwifruit": 90,
        "pear": 100,
        "sweet cherries": 100,
        # Add more fruits and their calories as needed
    }

    # Prompt the user to input a fruit (case-insensitive)
    fruit_input = input("Enter a fruit: ").lower()

    # Check if the input is a valid fruit in the dictionary
    if fruit_input in fruit_calories:
        calories = fruit_calories[fruit_input]
        print(calories)  # Output only the calories without additional text
    else:
        # Output an empty string for invalid input
        print("")

if __name__ == "__main__":
    main()
