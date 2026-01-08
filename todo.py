
tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    print("Tasks:")
    for i, t in enumerate(tasks, 1):
        print(i, t)

print("Simple To-Do Application")
