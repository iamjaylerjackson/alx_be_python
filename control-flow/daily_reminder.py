task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(
                f"Reminder: {task} is a high priority task, try and complete when you can.")

    case "medium":
        if time_bound == "yes":
            print(
                f"Reminder: {task} is a meduim priority task that require iimediate atention today!")
        else:
            print(
                f"Reminder: {task} is a medium priority task, try and complete it when you can.")

    case "low":
        if time_bound == "yes":
            print(
                "Reminder: {task} is a low priority task that requires immediate attention today!")

        else:
            print(
                f"Note: {task} is a low priority task, consider completing it when you have free time.")
