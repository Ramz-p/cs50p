def emojize(input_str):
    emoji_mapping = {
        ":1st_place_medal:": "🥇",
        ":thumbsup:": "👍",
        ":earth_asia:": "🌏",
        ":candy:": "🍬",
        ":ice_cream:": "🍨",
        # Add more emoji mappings as needed
    }

    for code, emoji in emoji_mapping.items():
        input_str = input_str.replace(code, emoji)

    return input_str

def main():
    user_input = input("Enter a string in English: ")
    emojized_str = emojize(user_input)
    print("Emojized version:", emojized_str)

if __name__ == "__main__":
    main()
