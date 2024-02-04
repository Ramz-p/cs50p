import random

def main():
    # Get the level from the user
    level = get_level()

    # Play the game and get the score
    score = play_game(level)

    # Display the final score
    print(f"{score}")

def get_level():
    while True:
        try:
            # Prompt the user for the level
            level = int(input("Level: "))

            # Check if the level is valid (1, 2, or 3)
            if level in {1, 2, 3}:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        # Generate a random integer between 0 and 9 for level 1
        return random.randint(0, 9)
    elif level == 2:
        # Generate a random integer between 10 and 99 for level 2
        return random.randint(10, 99)
    elif level == 3:
        # Generate a random integer between 100 and 999 for level 3
        return random.randint(100, 999)

def play_game(level):
    score = 0

    # Loop through 10 rounds of the game
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        prompt = f"{x} + {y} = "

        # Display the math problem to the user
        print(prompt, end="")
        tries = 0

        # Allow the user up to 3 attempts to answer the problem
        while tries < 3:
            try:
                user_answer = int(input())

                # Check if the user's answer is correct
                if user_answer == answer:
                    print("Correct!\n")
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                # Handle the case where the user inputs a non-integer
                print("EEE")

        # If the user couldn't answer correctly after 3 attempts, display the correct answer
        if tries == 3:
            print(f"Correct answer: {answer}\n")

    return score

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
