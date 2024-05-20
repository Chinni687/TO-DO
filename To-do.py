import os 
from tabulate import tabulate

#function to complete a task
def loaded_task():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt","r") as file:
            tasks = [line.strip().split(",") for line in file.readlines()]
        return tasks
    else:
        return[]
    
#function to save tasks 
def saved_task(tasks):
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(",".join(task) + "\n")

    
#function to display tasks 
def displayed_tasks(tasks):
    if tasks:
        print(tabulate(tasks,headers=["Task","Status"]))
    else:
        print("No Tasks found")

#function to add tasks
def added_task(tasks,task):
    tasks.append([task,"Incomplete"])
    
#function to remove tasks
def removed_task(tasks,task_index):
    if 0 <=task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index!")

def completed_task(tasks,task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index][1] = "Complete"

#Main function
def main():
    tasks= loaded_task()

    while True:
        print("\nTO-DO LIST:")
        displayed_tasks(tasks)

        print("\n_ _ _ Menu_ _ _")
        print("1. ADDED TASK ")
        print("2. DELETED TASK ")
        print("3. MARKED TASK AS COMPLETED")
        print("4. SAVEED TASK AND QUIT ")

        choice = input("Enter your Choice:")

        if choice == "1":
        
            task=input("Enter task:")
            added_task(tasks,task)
        elif choice == "2":
            task_index=int(input("Enter task index to delete:"))
            removed_task(tasks,task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to mark as Complete: "))
            completed_task(tasks,task_index)
        elif choice=="4":
            saved_task(tasks)
            print("Tasks saved. Quitting.....")
            break 
        else:
            print("Invalid Choice.Try again...")


if __name__ =="__main__":
    main()

