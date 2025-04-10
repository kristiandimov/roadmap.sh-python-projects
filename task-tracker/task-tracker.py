from task import *
from tasklist import *

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
""")

task_database = TaskList()

def print_tasks(tasks : TaskList) -> None:
    for task in tasks:
        print(str(task))

def main():
    while True:
        id = task_database.get_max_id()
        cmd = input("> ").strip()

        if cmd.lower() in ("quit","exit","q"):
            print("Exitting...")
            break

        if cmd is None:
            continue
        
        cmd = cmd.replace("task-cli","").strip()

        if cmd.startswith("add "):
            task_name = cmd[len("add "):].strip()
            if len(task_name) >= 2 and task_name.startswith('"') and task_name.endswith('"'):
                task_name = task_name[1:-1]

            task_database.append(Task(id,
                        cmd.replace("add",""),
                        "",
                        "todo"))
            print(f"Successfuly added new task --> ID: {id} task_name: {task_name}")

        elif cmd.startswith("update "):
            cmd = cmd[len("update "):].strip()
            task_id = int((cmd.split() or [None])[0])
            task_description = cmd[len(str(task_id)):].strip()

            task = task_database.get_object_by_id(task_id)
        
            task.description = task_description

            print(f"Succesfuly updated task {task.task_name}")
        elif cmd.startswith("delete "):
            cmd = cmd[len("delete "):].strip()
            task_id = int(cmd)

            task = task_database.get_object_by_id(task_id)
            task_database.remove(task)

        elif cmd.startswith("list"):
            cmd = cmd[len("list "):].strip()

            if cmd == "todo":
                print_tasks(task_database.get_objects_by_status("todo"))
            elif cmd == "in-progress":
                print_tasks(task_database.get_objects_by_status("in-progress"))
            elif cmd == "done":
                print_tasks(task_database.get_objects_by_status("done"))
            else:
                print_tasks(task_database)
        elif cmd.startswith("mark-"):
            cmd = cmd[len("mark-"):].strip()

            if cmd.startswith("in-progress"):
                cmd = cmd[len("in-progress "):].strip()
                task = task_database.get_object_by_id(int(cmd))
                task.status = "in-progress"
                print(f"""Successfluly updated task status
                                {str(task)}
                """)
            elif cmd.startswith("done"):
                cmd = cmd[len("done "):].strip()
                task = task_database.get_object_by_id(int(cmd))
                task.status = "done"
                print(f"""Successfluly updated task status
                                {str(task)}
                """)
        else:
            print(f"Unsuported command {cmd}")
        
main()

