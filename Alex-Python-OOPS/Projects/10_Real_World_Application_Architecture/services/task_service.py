from models.task import Task
class TaskService:
    def __init__(self, repository):
        self.repository = repository  # Dependency injection
        self._next_id = 1
    def create(self, title):
        if not title.strip(): raise ValueError('Title required')
        task = Task(self._next_id, title)
        self.repository.save(task)
        self._next_id += 1
        return task
    def complete(self, task_id):
        task = self.repository.get(task_id)
        if task is None: raise LookupError('Task not found')
        if task.completed: raise ValueError('Already completed')
        task.completed = True
        self.repository.save(task)
        return task
    def list_tasks(self): return self.repository.all()
