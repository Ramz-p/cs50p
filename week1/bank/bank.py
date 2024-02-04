# bank.py

def main():
    # Prompt the user for a greeting
    user_greeting = input("Enter a greeting: ")

    # Remove leading whitespace and convert the input to lowercase
    user_greeting_cleaned = user_greeting.lstrip().lower()

    # Check the type of greeting and output the corresponding amount
    if user_greeting_cleaned.startswith("hello"):
        print("$0")
    elif user_greeting_cleaned.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
