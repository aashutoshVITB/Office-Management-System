from datastore import tasks

def add_task():
    title = input("Task name: ")
    assigned_to = input("Assign to (employee name): ")
    task = {
        "title": title,
        "assigned_to": assigned_to
    }
    tasks.append(task)
    print("Task added.")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("-- Tasks --")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} (Assigned to: {task['assigned_to']})")
