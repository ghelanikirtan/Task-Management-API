from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


# 5. Unit Tests:
class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(
            title = 'Test Task',
            description = 'This is Test Task',
            due_date = '2024-02-15',
            status = 'Pending'
        )
        
    # 1) List all tasks
    def test_list_all_tasks(self):
        res = self.client.get('/tasks/')
        self.assertEqual(res.status_code, 200)
    
    # 2) List a single task by id
    def test_retrieve_single_task_byId(self):
        res = self.client.get(f'/tasks/{self.task.id}/')
        self.assertEqual(res.status_code, 200)
    
    # 3) Create a new task
    def test_create_task(self):
        new_task_data = {
            "title" : "New testing task",
            "description": "This is newly created testing task! hehe",
            "due_date": "2024-02-15",
            "status": "In Progress"
        }
        res = self.client.post(f'/tasks/', new_task_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    # 4) Update existing task
    def test_update_existing_task(self):
        updated_data = {
            "title" : "Updated testing task",
            "description": "This is updated testing task",
            "due_date": "2024-02-15",
            "status": "Completed"
        }
        
        # I am using PUT/PATCH method for existing task updation
        res = self.client.patch(f'/tasks/{self.task.id}/', updated_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
        # re-checking updation
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, updated_data['title'])
        self.assertEqual(updated_task.description, updated_data['description'])
        self.assertEqual(str(updated_task.due_date), updated_data['due_date'])
        self.assertEqual(updated_task.status, updated_data['status'])
        
    # 5) Delete a Task
    def test_delete_task(self):
        res = self.client.delete(f'/tasks/{self.task.id}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        
        # re-checking deleted task
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task.id)
            
    