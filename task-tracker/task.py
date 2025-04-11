from datetime import *
class Task: 
    def __init__(self,id: str,task_name: str,description: str = "",status: str = "todo" ,created_at: datetime = None, updated_at: datetime = None) -> None:
        self.__id = id
        self.__task_name = task_name
        self.__description = description
        self.__status = status
        self.__created_at = created_at if created_at is not None else datetime.now().isoformat()
        self.__updated_at = updated_at if updated_at is not None else datetime.now().isoformat()

    def get_id(self) -> int:
        return self.__id
    
    def get_status(self) -> int:
        return self.__status
    
    def get_task_name(self) -> str:
        return self.__task_name
 
    def update_task_description(self,new_description: str) -> None:
        #Updates the description
        self.__description = new_description
        self.__updated_at = datetime.now().isoformat()

    def update_task_status(self, new_status: str) -> None:
        #Updates the status of a task 
        self.__status = new_status
        self.__updated_at = datetime.now().isoformat()

    def __str__(self) -> str:
        #Formatting the task in a readable format for the console
        return (
            "---------------------------------------------------------\n"
            f"    Task_ID: {self.__id}\n"
            f"    Task_Name: {self.__task_name}\n"
            f"    Description: {self.__description}\n"
            f"    Status: {self.__status}\n"
            f"    Created_at: {self.__created_at}\n"
            f"    Updated_at: {self.__updated_at}\n"
            "---------------------------------------------------------"
        )