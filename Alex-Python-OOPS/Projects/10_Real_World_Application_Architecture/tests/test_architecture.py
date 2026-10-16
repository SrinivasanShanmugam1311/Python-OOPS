import unittest
from repositories.task_repository import InMemoryTaskRepository
from services.task_service import TaskService
class ArchitectureTests(unittest.TestCase):
    def setUp(self): self.service = TaskService(InMemoryTaskRepository())
    def test_create(self): self.assertEqual(self.service.create('Learn').title,'Learn')
    def test_invalid_title(self):
        with self.assertRaises(ValueError): self.service.create(' ')
    def test_complete(self):
        task=self.service.create('Learn')
        self.assertTrue(self.service.complete(task.task_id).completed)
    def test_missing_task(self):
        with self.assertRaises(LookupError): self.service.complete(999)
    def test_double_completion(self):
        task=self.service.create('Learn'); self.service.complete(task.task_id)
        with self.assertRaises(ValueError): self.service.complete(task.task_id)
    def test_list(self):
        self.service.create('A'); self.service.create('B')
        self.assertEqual(len(self.service.list_tasks()),2)
    def test_repository_isolation(self):
        other=TaskService(InMemoryTaskRepository())
        self.service.create('A')
        self.assertEqual(len(other.list_tasks()),0)
    def test_ids(self):
        a=self.service.create('A');b=self.service.create('B')
        self.assertNotEqual(a.task_id,b.task_id)
if __name__ == '__main__': unittest.main()
