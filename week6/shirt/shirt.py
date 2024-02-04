from PIL import Image, ImageOps
import sys
import os

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Define valid image formats
        format = [".jpg", ".jpeg", ".png"]

        # Split the extensions of input and output files
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])

        # Check if the output format is valid
        if outp[1].lower() not in format:
            sys.exit("Invalid output format")
        # Check if input and output have the same extension
        elif inp[1].lower() != outp[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            # Call the edit_photo function with provided input and output files
            edit_photo(sys.argv[1], sys.argv[2])

def edit_photo(input, output):
    try:
        # Open the shirt image
        shirt = Image.open("shirt.png")

        # Open the input image
        with Image.open(input) as input:
            # Crop and fit the input image to the size of the shirt image
            input_cropped = ImageOps.fit(input, shirt.size)

            # Paste the shirt image onto the input image using the shirt as a mask
            input_cropped.paste(shirt, mask=shirt)

            # Save the edited image
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
