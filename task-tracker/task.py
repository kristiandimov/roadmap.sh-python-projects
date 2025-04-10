from datetime import *
class Task: 
    def __init__(self,id: str,task_name: str,description: str,status: str,created_at: datetime = None, updated_at: datetime = None) -> None:
        self.id = id
        self.task_name = task_name
        self.description = description
        self.status = status
        self.created_at = created_at if created_at is not None else datetime.now().isoformat()
        self.updated_at = updated_at if updated_at is not None else datetime.now().isoformat()
 
    def update_task_description(self,new_description: str) -> None:
        #Updates the description
        self.description = new_description
        self.updated_at = datetime.now().isoformat()

    def update_task_status(self, new_status: str) -> None:
        #Updates the status of a task 
        self.status = new_status
        self.updated_at = datetime.now().isoformat()

    def __str__(self) -> str:
        #Formatting the task in a readable format for the console
        return (
            "---------------------------------------------------------\n"
            f"    Task_ID: {self.id}\n"
            f"    Task_Name: {self.task_name}\n"
            f"    Description: {self.description}\n"
            f"    Status: {self.status}\n"
            f"    Created_at: {self.created_at}\n"
            f"    Updated_at: {self.updated_at}\n"
            "---------------------------------------------------------"
        )