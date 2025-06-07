import sys
from task_manager import add_task, load_tasks, list_tasks, mark_task_status, update_task, delete_task

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py [command] [arguments]")
        return

    command=sys.argv[1]
    
    if command=="add":
        if len(sys.argv)<3:
            print("Usage: python task_cli.py add ['Task Description']")
        else:
            description=" ".join(sys.argv[2:])
            add_task(description)
    
    elif command=="list":
        if len(sys.argv)==2:
            list_tasks()
        elif sys.argv[2] in ["todo", "done", "in-progress"]:
            list_tasks(sys.argv[2])
        else:
            print("Usage: python task_cli.py list [todo | done | in-progress]")
        
    elif command=="mark-done":
        if len(sys.argv)<3 or not sys.argv[2].isdigit():
            print("Usage: python task.cli.py mark-done [task_id]")
        else:
            task_id=int(sys.argv[2])
            mark_task_status(task_id, "done")
    
    elif command=="mark-in-progress":
        if len(sys.argv)<3 or not sys.argv[2].isdigit():
            print("Usage: python task_cli.py mark-in-progress [task_id]")
        else:
            task_id=int(sys.argv[2])
            mark_task_status(task_id, "in-progress")
    
    elif command=="update":
        if len(sys.argv)<4 or not sys.argv[2].isdigit():
            print("Usage: python task_cli.py update [task_id]['New Description']")
        else:
            task_id=int(sys.argv[2])
            new_description=" ".join(sys.argv[3:])
            update_task(task_id, new_description)
    elif command=="delete":
        if len(sys.argv)<3 or not sys.argv[2].isdigit():
            print("Usage: python task_cli.py delete [task_id]")
        else:
            task_id=int(sys.argv[2])
            delete_task(task_id)
        
    else:
        print(f"Unlnown command: {command}")
        
if __name__=="__main__":
    main()