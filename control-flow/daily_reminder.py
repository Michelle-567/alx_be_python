# daily_reminder.py

# Get user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize message
message = ""

# Match case to handle priority levels
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Invalid priority level for task: '{task}'"

# Add time-bound message only if the priority was valid
if "priority" in message:
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        if priority in ["low", "medium"]:
            message += ". Consider completing it when you have free time."

# Print the final reminder
print(message)
