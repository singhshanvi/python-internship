# ---------------------------------------------
# PROJECT :  Personal Task Manager 🧾
# AUTHOR  :  Shanvi Singh
# INTERNSHIP :  CodSoft – Python Programming
# DESCRIPTION :
#   This program lets users manage daily tasks easily.
#   Users can add, view, edit, delete, and mark tasks done.
# ---------------------------------------------

task_list = []   # Stores all tasks

# -----------------------------------------------------
# Function : display_menu()
# -----------------------------------------------------
def display_menu():
    print("\n📋 ----- MY TASK MANAGER -----")
    print("1️⃣  Add New Task")
    print("2️⃣  Show All Tasks")
    print("3️⃣  Edit a Task")
    print("4️⃣  Delete a Task")
    print("5️⃣  Mark Task as Completed ✅")
    print("6️⃣  Exit")
    print("---------------------------------")


# -----------------------------------------------------
# Function : add_new_task()
# -----------------------------------------------------
def add_new_task():
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"✔️  '{task}' has been added successfully!")


# -----------------------------------------------------
# Function : show_tasks()
# -----------------------------------------------------
def show_tasks():
    if len(task_list) == 0:
        print("⚠️  No tasks found! Please add one first.")
    else:
        print("\n🗂️  Your Current Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")


# -----------------------------------------------------
# Function : edit_task()
# -----------------------------------------------------
def edit_task():
    show_tasks()
    if len(task_list) > 0:
        try:
            num = int(input("Enter task number to edit: "))
            if 1 <= num <= len(task_list):
                new_task = input("Enter the new description: ")
                task_list[num - 1] = new_task
                print("✏️  Task updated successfully!")
            else:
                print("❌  Invalid task number!")
        except ValueError:
            print("❌  Please enter a valid number!")


# -----------------------------------------------------
# Function : delete_task()
# -----------------------------------------------------
def delete_task():
    show_tasks()
    if len(task_list) > 0:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(task_list):
                removed = task_list.pop(num - 1)
                print(f"🗑️  '{removed}' deleted successfully!")
            else:
                print("❌  Invalid task number!")
        except ValueError:
            print("❌  Please enter a valid number!")


# -----------------------------------------------------
# Function : mark_completed()
# -----------------------------------------------------
def mark_completed():
    show_tasks()
    if len(task_list) > 0:
        try:
            num = int(input("Enter task number to mark completed: "))
            if 1 <= num <= len(task_list):
                if "✅" not in task_list[num - 1]:
                    task_list[num - 1] += " ✅"
                    print("🎉  Task marked as completed!")
                else:
                    print("⚠️  Task is already completed!")
            else:
                print("❌  Invalid task number!")
        except ValueError:
            print("❌  Please enter a valid number!")


# -----------------------------------------------------
# Main Program Loop
# -----------------------------------------------------
while True:
    display_menu()
    choice = input("👉  Enter your choice (1-6): ")

    if choice == '1':
        add_new_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        edit_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_completed()
    elif choice == '6':
        print("\n👋  Thanks for using My Task Manager! Have a productive day!")
        break
    else:
        print("❌  Invalid option! Please choose from 1 to 6.")
