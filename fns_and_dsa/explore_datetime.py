#Part 1: Display the Current Date and Time
#Import datetime and timedelta
from datetime import datetime, timedelta
#datetime.now() → gives current date and time.
#timedelta(days=5) → lets you add or subtract days from a date.

#Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print("Current date and time:", formatted_date)

#strftime() is used to format how the date looks.
#Example: "%Y-%m-%d" means "year-month-day".

#Calculate a Future Date
#Create a function calculate_future_date() that:
#Asks the user how many days to add.
#Adds those days to today’s date using timedelta.
#Prints the future date in "YYYY-MM-DD" format.
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)

#Run It All in a main() Function
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
