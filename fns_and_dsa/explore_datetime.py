# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days: int):
    """
    Calculates a future date based on the number of days entered.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

if __name__ == "__main__":
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Ask user for number of days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("⚠️ Please enter a valid integer for days.")
