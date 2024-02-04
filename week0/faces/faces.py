# faces.py

def convert(text):
    # Convert :) to 🙂 and :( to 🙁
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    # Prompt the user for input
    user_input = input("Please enter some text: ")

    # Call the convert function to replace emoticons with emojis
    converted_text = convert(user_input)

    # Output the modified text
    print("Your input with emoticons converted: ", converted_text)

if __name__ == "__main__":
    main()
