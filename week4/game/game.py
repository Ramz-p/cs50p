import random

def get_level():
    """
    Prompt the user for the level until a positive integer is provided.
    """
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def play_game(level):
    """
    Play the guessing game.
    """
    answer = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                print("Too small!")
            elif guess > level:
                print("Too large!")
            elif guess == answer:
                print("Just right!")
                break
            elif guess < answer:
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            pass

def main():
    level = get_level()
    play_game(level)

if __name__ == "__main__":
    main()
