# playback.py

def main():
    # Prompt the user for input
    user_input = input("Please enter some text: ")

    # Replace each space with three periods
    replaced_text = user_input.replace(' ', '...')

    # Output the modified text
    print("Your input with spaces replaced: ", replaced_text)

if __name__ == "__main__":
    main()

