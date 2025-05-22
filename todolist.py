def menu():
    print("""
    TO DO LIST
    --------------------
    1. Add a task
    2. View all tasks
    3. Mark a task as complete
    4. Delete a task
    5. Exit
    """)


def add_a_task(task: str) -> str:
    return "Task added" if task.strip() else "Invalid"


def view_all_tasks(all_tasks: list):
    if not all_tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(all_tasks, start=1):
            print(f"{index}. [] {task}") 


def mark_task_complete(task_list: list):
    view_all_tasks(task_list)
    
    if task_list:
        try:
            task_number = int(input("\nEnter the task number to mark complete: "))
            if 0 <= task_number < len(task_list):
                print(f"Task '{task_list[task_number]}' marked as complete!")
                task_list[task_number] = f"[x] {task_list[task_number]}"
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def delete_task(task_list: list):
    view_all_tasks(task_list)

    if task_list:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 0 <= task_number < len(task_list):
                removed_task = task_list.pop(task_number)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    tasks = []

    while True:
        menu()
        
        try:
            user_choice = int(input("Enter your choice (1-5): "))
            if user_choice == 1:
                task = input("\nEnter your task: ")
                if add_a_task(task) == "Task added":
                    tasks.append(task)
                    print("Task added successfully!")
                else:
                    print("Invalid input. Task cannot be empty.")

            elif user_choice == 2:
                view_all_tasks(tasks)

            elif user_choice == 3:
                mark_task_complete(tasks)

            elif user_choice == 4:
                delete_task(tasks)

            elif user_choice == 5:
                print("\nExisting application... Goodbye!")
                break

            else:
                print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")




if __name__ == "__main__":
    main()
