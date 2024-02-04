# deep.py

def main():
    # Prompt the user for the answer to the Great Question
    user_input = input("What is the Answer to the Great Question? ")

    # Remove leading and trailing spaces and convert the input to lowercase
    user_input_cleaned = user_input.strip().lower()

    # Check if the cleaned user input matches the expected answers
    if user_input_cleaned == "42" or user_input_cleaned == "forty-two" or user_input_cleaned == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
