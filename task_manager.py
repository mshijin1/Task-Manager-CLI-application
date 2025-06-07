import json
import os
from datetime import datetime

TASK_FILE="tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE): # Checks if the file exists or not
        
        # If the file does not exists, the creating a new file as tasks.json
        with open(TASK_FILE,"w") as f:
            json.dump([],f) 
            
    # But, if the file exists, it will load the tasks from the file
    with open(TASK_FILE, "r") as f:
        tasks=json.load(f)
        print(tasks)
        return tasks

# function to assign new 'ID' to the new task
def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks)+1

# function to save the task in tasks.json
def save_tasks(tasks):
    with open(TASK_FILE,"w") as f:
        json.dump(tasks,f,indent=4)

   
# Creating a function to add a task
def add_task(description):
    tasks=load_tasks() # first we fetch all the tasks with load_tasks()
    
    # Adding details about the new task
    new_task={
        "id": get_next_id(tasks), # This function helps to assign 'ID' to the new tasks followed by one another
        "description":description,
        "status":"todo",
        "createdAT": datetime.now().isoformat(),
        "updatedAT":datetime.now().isoformat()
    }
    tasks.append(new_task) 
    save_tasks(tasks) # now saving the tasks into the real json file
    print(f'Task added successfully (ID: {new_task["id"]})')


# A function used to list all the tasks according to there status
def list_tasks(filter_status=None):
    tasks=load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    if filter_status:
        tasks=[task for task in tasks if task["status"]==filter_status] # Filtering tasks based on the status [todo | done | in-progress]
        
    if not tasks:
        print(f"No tasks found in the list")
        
    for task in tasks:
        print(f"[{task['id']}] {task['description']} | status: {task['status']} | Created: {task['createdAT']}")
        
def mark_task_status(task_id, new_status):
    tasks=load_tasks()
    task_found=False
    
    for task in tasks:
        if task['id']==task_id:
            task['status']=new_status
            task['updatedAT']=datetime.now().isoformat()
            task_found=True
            break
    if not task_found:
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks(tasks)
        print(f"Task {task_id} marked as {new_status}")
        
def update_task(task_id, new_description):
    tasks=load_tasks()
    task_found=False
    
    for task in tasks:
        if task["id"]==task_id:
            task["description"]=new_description
            task["updatedAT"]=datetime.now().isoformat()
            task_found=True
            break
    
    if not task_found:
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully.")

def delete_task(task_id):
    tasks=load_tasks()
    new_tasks=[task for task in tasks if task["id"]!=task_id]
    
    if len(new_tasks)==len(tasks):
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted successfully.")
        