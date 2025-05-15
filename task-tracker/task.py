from datetime import *
class Task(): 
    def __init__(self,id: str,task_name: str,description: str = "",status: str = "todo" ,created_at: datetime = None, updated_at: datetime = None) -> None:
        self._id = id
        self._task_name = task_name
        self._description = description
        self._status = status
        self._created_at = created_at if created_at is not None else datetime.now().isoformat()
        self._updated_at = updated_at if updated_at is not None else datetime.now().isoformat()

    @property
    def get_id(self) -> int:
        return self._id
    
    @property
    def get_status(self) -> str:
        return self._status
    
    @property
    def get_task_name(self) -> str:
        return self._task_name
 
    def update_task_description(self,new_description: str) -> None:
        #Updates the description
        self._description = new_description
        self._updated_at = datetime.now().isoformat()

    def update_task_status(self, new_status: str) -> None:
        #Updates the status of a task 
        self._status = new_status
        self._updated_at = datetime.now().isoformat()

    def __str__(self) -> str:
        #Formatting the task in a readable format for the console
        return (
            "---------------------------------------------------------\n"
            f"    Task_ID: {self._id}\n"
            f"    Task_Name: {self._task_name}\n"
            f"    Description: {self._description}\n"
            f"    Status: {self._status}\n"
            f"    Created_at: {self._created_at}\n"
            f"    Updated_at: {self._updated_at}\n"
            "---------------------------------------------------------"
        )