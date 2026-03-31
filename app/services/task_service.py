from fastapi import HTTPException
from app.models.task_model import Task
from datetime import datetime, timezone
from app.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, name):
        task = Task(name=name, status="pending")

        self.repository.create(task)
        return task

    def get_tasks(self):
        return self.repository.get_all()

    def delete_task(self, task_id):
        task = self.repository.get_by_id(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        self.repository.delete(task)
        return {"id": task_id}

    def update_task(self, task_id, name, progress):
        task = self.repository.get_by_id(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        task.name = name
        task.progress = progress
        task.updated_at = datetime.now(timezone.utc)

        return self.repository.update(task)

    def get_task(self, task_id):
        task = self.repository.get_by_id(task_id)

        print(task)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        return task
        
    def complete_task(self, task_id):
        task = self.repository.get_by_id(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        task.status = "completed"
        task.progress = 100
        task.updated_at = datetime.now(timezone.utc)

        return self.repository.update(task)