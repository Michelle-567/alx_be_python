# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case to determine base message
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Add time-bound message
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["low", "medium"]:
        message += ". Consider completing it when you have free time."


# Output the reminder
print(message)