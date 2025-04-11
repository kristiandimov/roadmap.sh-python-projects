import shlex
from task import *
from tasklist import *

task_database = TaskList()

def cli_menu():
    print("""Choose one of following actions:
    task-cli add "[TASK_NAME]"                  --> Creates a task  
    task-cli update [TASK_ID] "[DESCIPTION]"    --> Update task by id
    task-cli delete [TASK_ID]                   --> Delete task by id
    task-cli mark-in-progress [TASK_ID]         --> Marks task in progress status
    task-cli mark-done [TASK_ID]                --> Marks task as done
    task-cli list                               --> Lists all tasks
    task-cli list done                          --> Lists all done tasks
    task-cli list todo                          --> Lists all todo tasks
    task-cli list in-progress                   --> Lists all in-progress tasks
    (Type 'quit', 'exit', or 'q' to exit.)
    (Type help, -help, --help, h, -h, --h to exit.)""")

def print_tasks(tasks : TaskList) -> None:
    for task in tasks:
        print(str(task))

def check_id(id:str):
    try:
        id = int(id[0])
        return id
    except ValueError:
        print("Error: TASK_ID needs to be integer")
        return

def add_task(args: list):
    if not args:
        print("Error: Task name is required.")
        return
    
    task_name = args[0]
    id = task_database.get_max_id()

    task = Task(id,task_name) 

    task_database.append(task)
    print(f"Successfuly added new task --> ID: {id} task_name: {task_name}")

def update_task(args: list):
    if len(args) < 2:
        print("Usage: update [TASK_ID] \"[DESCRIPTION]\"")
        return
    
    id = check_id(args[0])

    task_description = args[1]

    task = task_database.get_object_by_id(id)

    if task is None:
        print(f"Error: None tasks were found with id = {id}")
        return

    task.update_task_description(task_description)
    print(f"Successfully updated task '{task.get_task_name()}'.")

def delete_task(args: List):
    
    if not args:
        print("Usage: update [TASK_ID]")
        return

    id = check_id(args[0])

    task = task_database.get_object_by_id(id)
    task_database.remove(task)

    print(f"Successfuly delete task {task.get_task_name()}")

def list_tasks(args: List):
    if args:
        status = args[0]
        tasks = task_database.get_objects_by_status(status)

        if not tasks:
            print(f"No tasks found with status: {status}")
        else:
            print_tasks(tasks)
    else:
        print_tasks(task_database)
def mark_status(args: List,new_status):
    if not args:
        print("Usage: update [TASK_ID]")
        return

    id = check_id(args[0])

    task = task_database.get_object_by_id(id)

    if task is None:
        print(f"Error: No task found with ID {id}.")
        return
    
    task.update_task_status(new_status)

    print(f"Successfully updated task status to '{new_status}':\n{task}")


def process_commands(command_line: str):
    ##Parses and process command line commands
    if command_line.startswith("task-cli"):
        command_line = command_line[len("task-cli "):].strip()

    try:
        #Returns commands splitted for bash commands
        tokens = shlex.split(command_line)
    except Exception as e:
        print(f"Error parsing command {str(e)}")
        return

    if tokens is None:
        return
    
    cmd = tokens[0].lower()
    params = tokens[1:]

    if cmd == "add":
        ##Passing task_name
        add_task(params)
    elif cmd == "update":
        update_task(params)
    elif cmd == "delete":
        delete_task(params)
    elif cmd == "list":
        list_tasks(params)
    elif cmd == "mark-in-progress":
        mark_status(params,"in-progress")
    elif cmd == "mark-done":
        mark_status(params,"done")
    else:
        print("Unsuported command ")
    
def main():
    cli_menu()

    while True:
        command_line = input(">>> ").strip()

        if command_line.lower() in ("quit","exit","q"):
            print("Exiting...")
            break
        elif command_line.lower() in ("help","-help","--help",'h',"-h","--h"):
            cli_menu()
            continue

        process_commands(command_line)


if __name__ == "__main__":
    main()

