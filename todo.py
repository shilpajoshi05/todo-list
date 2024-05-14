import json
import datetime

class Task:
    def __init__(self, description, priority, due_date=None, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __repr__(self):
        return f"{self.description} (Priority: {self.priority}, Due: {self.due_date}, Completed: {self.completed})"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        del self.tasks[index]

    def mark_completed(self, index):
        self.tasks[index].completed = True

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.tasks = [Task(**task) for task in data]

def main():
    todo_list = TodoList()
    todo_list.load_from_file("tasks.json")

    while True:
        print("\nTODO LIST")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD) (optional): ")
            if due_date:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            todo_list.add_task(Task(description, priority, due_date))

        elif choice == "2":
            todo_list.list_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)

        elif choice == "3":
            todo_list.list_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)

        elif choice == "4":
            todo_list.list_tasks()

        elif choice == "5":
            todo_list.save_to_file("tasks.json")
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

