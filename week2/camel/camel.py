# camel.py

def main():
    # Prompt the user for a variable name in camel case
    camel_case_name = input("Enter a variable name in camel case: ")

    # Convert the camel case name to snake case
    snake_case_name = convert_to_snake_case(camel_case_name)

    # Output the corresponding name in snake case
    print("Snake case name:", snake_case_name)

def convert_to_snake_case(camel_case_name):
    snake_case_name = camel_case_name[0].lower()  # Convert the first character to lowercase

    # Iterate through the characters starting from the second character
    for char in camel_case_name[1:]:
        # Append an underscore before adding the lowercase character if it's uppercase
        if char.isupper():
            snake_case_name += '_' + char.lower()
        else:
            snake_case_name += char

    return snake_case_name

if __name__ == "__main__":
    main()
