#Making a todo list in which we can add remove show
tasks = []
def addtask(task):
    tasks.append(task)
    print(f"Task added: {task}")

def removetask(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task removed: {task}")
    else:
        print("No Task Found")

    
def showtask():
    if tasks:
        print("Tasks:")
        for index,task in enumerate(tasks):
            print(f"{index+1}.{tasks}")
    else:
        print("No tasks to show")



def main():
    while True:
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Show tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            newtask = input("Enter a new task: ")
            addtask(newtask)
        elif choice == "2":
            tasktoremove= input("Enter the task to be removed: ")
            removetask(tasktoremove)
        elif choice == "3":
            showtask()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
            

if __name__ == "__main__":
    main()
