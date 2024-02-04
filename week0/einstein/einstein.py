# einstein.py

def calculate_energy(mass):
    # Speed of light in meters per second
    speed_of_light = 300000000

    # Calculate energy using E=mc^2
    energy = mass * (speed_of_light ** 2)
    return energy

def main():
    # Prompt the user for mass as an integer
    mass = int(input("Please enter mass (in kilograms) as an integer: "))

    # Calculate energy using the provided function
    energy = calculate_energy(mass)

    # Output the equivalent energy in Joules
    print("Equivalent energy in Joules: ", energy)

if __name__ == "__main__":
    main()
