# bank.py

def main():
    # Prompt the user for a greeting
    user_greeting = input("Enter a greeting: ")

    # Remove leading whitespace and convert the input to lowercase
    user_greeting_cleaned = user_greeting.lstrip().lower()

    # Check the type of greeting and output the corresponding amount
    amount = value(user_greeting_cleaned)
    print(f"${amount}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
