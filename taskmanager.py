def task_management():
    tasks = []
    print("_____WELCOME TO TASK MANAGEMENT SYSTEM_____")

    try:
        total_task = int(input("Enter how many tasks you want to add: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    while True:
        print("\nChoose an operation:")
        print("1 - Add task")
        print("2 - Update task")
        print("3 - Delete task")
        print("4 - View tasks")
        print("5 - Exit")
        
        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                idx = tasks.index(updated_val)
                tasks[idx] = up
                print(f"Task updated to '{up}'.")
            else:
                print("Task not found.")

        elif operation == 3:
            deleted_val = input("Enter the task name you want to delete: ")
            if deleted_val in tasks:
                tasks.remove(deleted_val)
                print(f"Task '{deleted_val}' has been successfully deleted.")
            else:
                print("Task not found.")

        elif operation == 4:
            if tasks:
                print("\nCurrent Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks available.")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input. Please select a valid option (1-5).")


if __name__ == "__main__":
    task_management()

