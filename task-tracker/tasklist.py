from typing import Any,List,Optional,Iterator
from task import Task

class TaskList():
    def __init__(self):
        self._tasks: List[Task] = []

    def add_task(self, task: Task):
        self._tasks.append(task)

    def delete_task(self,task: Task):
        self._tasks.remove(task)

    def get_object_by_id(self: Task,id: int) -> Optional[Task]: ##-> Optional[Any]: it will return anything or nothing
        #Finds object with matching id
        for obj in self:
            if obj.get_id == id:
                return obj
        return None
    
    def get_objects_by_status(self: Task,status: str) -> List[Task]: #status: str) -> List[Any]: :srt tells us that the status will be string value and List[Any] will return List of typ any type
        #Gets all task with specific status
        return [task for task in self if task.get_status == status]

    def get_next_id(self) -> int: # -> int anotation tells us that return type will be int
        #Returns max_id with +1
        max_id = max((task.get_id for task in self), default=0)
        return max_id + 1

    def __iter__(self) -> Iterator[Task]:
        return iter(self._tasks)

    def __getitem__(self, index: int) -> Task:
        return self._tasks[index]

    def __len__(self) -> int:
        return len(self._tasks)
