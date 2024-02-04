def shorten(word):
    vowels = "AEIOUaeiou"
    result = ''.join(char for char in word if char not in vowels)
    return result

def main():
    # Prompt the user for input
    user_input = input()

    # Remove vowels from the input and print the result
    result = shorten(user_input)
    print(result)

if __name__ == "__main__":
    main()
