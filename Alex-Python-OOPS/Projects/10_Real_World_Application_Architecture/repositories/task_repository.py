from abc import ABC, abstractmethod
from models.task import Task
class TaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task): pass
    @abstractmethod
    def get(self, task_id: int): pass
    @abstractmethod
    def all(self): pass
class InMemoryTaskRepository(TaskRepository):
    def __init__(self): self._tasks = {}
    def save(self, task): self._tasks[task.task_id] = task
    def get(self, task_id): return self._tasks.get(task_id)
    def all(self): return list(self._tasks.values())
