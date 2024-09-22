# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " consider addressing it soon!"
        else:
            reminder += " You can handle it when convenient."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " but it's still advisable to take care of it promptly."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

# Print the customized reminder
print("\nReminder:", reminder)

