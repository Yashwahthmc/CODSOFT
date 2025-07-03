tasks = []
def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i,task in enumerate(tasks,1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}. [{status}] {task['title']}")
def add_task():
    title=input("Enter task:")
    tasks.append({"title":title,"done":False})
    print("Task added.")
def mark_done():
    show_tasks()
    try:
        idx=int(input("Enter task number to mark as done: "))-1
        if 0<=idx<len(tasks):
            tasks[idx]["done"]=True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")
def delete_task():
    show_tasks()
    try:
        idx=int(input("Enter task number to delete: ")) - 1
        if 0<=idx<len(tasks):
            tasks.pop(idx)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")
print("📋 Welcome to Yashwanth's To-Do List App 📋")
while True:
    print("\nMenu:\n1.Add Task\n2.View Tasks\n3.Mark Task as Done\n4.Delete Task\n5.Exit")
    choice=input("Enter choice:")
    if choice=='1':
        add_task()
    elif choice=='2':
        show_tasks()
    elif choice=='3':
        mark_done()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        print("Exiting... ✅")
        break
    else:
        print("Invalid choice. Try again.")
