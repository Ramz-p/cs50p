import sys


def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            non_empty_lines = [line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")]
            return len(non_empty_lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_path = sys.argv[1]

    # Check if the file has a .py extension
    if not file_path.endswith(".py"):
        sys.exit("Not a Python file")

    lines_count = count_lines(file_path)
    print(lines_count)


if __name__ == "__main__":
    main()
