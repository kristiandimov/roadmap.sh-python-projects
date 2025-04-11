from typing import Any,List,Optional
from task import Task

class TaskList(list):
    def get_object_by_id(self,id: int) -> Optional[Task]: ##-> Optional[Any]: it will return anything or nothing
        #Finds object with matching id
        for obj in self:
            if obj.id == id:
                return obj
        return None
    
    def get_objects_by_status(self,status: str) -> List[Any]: #status: str) -> List[Any]: :srt tells us that the status will be string value and List[Any] will return List of typ any type
        #Gets all task with specific status
        return [task for task in self if task.status == status]

    def get_max_id(self) -> int: # -> int anotation tells us that return type will be int
        #Returns max_id with +1
        max_id = max((task.id for task in self), default=0)
        return max_id + 1

        
