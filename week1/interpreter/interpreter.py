# interpreter.py

def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    # Split the expression into three parts: x, operator, z
    x, operator, z = expression.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Calculate the result based on the operator
    result = calculate(x, operator, z)

    # Output the result as a floating-point value formatted to one decimal place
    print("{:.1f}".format(result))

def calculate(x, operator, z):
    # Perform the calculation based on the operator
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        # Assume that z will not be 0
        return x / z

if __name__ == "__main__":
    main()
