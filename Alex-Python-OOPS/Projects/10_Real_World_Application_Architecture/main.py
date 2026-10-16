from repositories.task_repository import InMemoryTaskRepository
from services.task_service import TaskService

def main():
    service = TaskService(InMemoryTaskRepository())
    task = service.create('Learn Python OOPS architecture')
    print('Created:', task)
    print('Completed:', service.complete(task.task_id))

if __name__ == '__main__': main()
