# twttr.py

def remove_vowels(text):
    vowels = "AEIOUaeiou"
    result = ''.join(char for char in text if char not in vowels)
    return result

def main():
    # Prompt the user for input
    user_input = input("Enter a text: ")

    # Remove vowels from the input and print the result
    result = remove_vowels(user_input)
    print("Text without vowels:", result)

if __name__ == "__main__":
    main()
