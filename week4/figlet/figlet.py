import sys
import random
from pyfiglet import Figlet

# Create a Figlet object
figlet = Figlet()

# Possible command-line arguments for font selection
argv1 = ["-f", "--font"]

def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        # If no arguments provided, choose a random font
        font = random.choice(figlet.getFonts())
        figletize("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts():
        # If valid font is specified in command-line arguments
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        # If invalid usage, print error message and exit
        sys.exit("Invalid usage")

def figletize(prompt, f):
    # Prompt the user for input
    txt = input(prompt)

    # Set the font for the Figlet object
    figlet.setFont(font=f)

    # Display the formatted text using the specified font
    print("Output:")
    print(figlet.renderText(txt))

# Run the main function
main()
