# meal.py

def main():
    # Prompt the user for a time in 24-hour format
    time_input = input("Enter the time in 24-hour format (e.g., 07:30): ")

    # Convert the time to hours as a float
    time_in_hours = convert(time_input)

    # Determine the mealtime and output the result
    determine_mealtime(time_in_hours)

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(':'))

    # Convert the time to hours as a float
    return hours + minutes / 60

def determine_mealtime(time):
    # Define the time ranges for each meal
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    # Determine the mealtime and output the result
    if breakfast_start <= time <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= time <= lunch_end:
        print("lunch time")
    elif dinner_start <= time <= dinner_end:
        print("dinner time")

if __name__ == "__main__":
    main()
