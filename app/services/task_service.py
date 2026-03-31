from fastapi import HTTPException
from datetime import datetime, timezone
from sqlmodel import Session, select
from app.database import engine
from app.models.task_model import Task


class TaskService:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, name):
        task = Task(name=name, status="pending")

        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_tasks(self):
        return self.session.exec(select(Task)).all()


    def delete_task(self, task_id):
        task = self.session.get(Task, task_id)
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
    
        self.session.delete(task)
        self.session.commit()

        return {"id": task_id}

    def update_task(self, task_id, name, progress):
        task = self.session.get(Task, task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        task.name = name
        task.progress = progress
        task.updated_at = datetime.now(timezone.utc)
        self.session.add(task)
        self.session.commit()

        self.session.refresh(task)

        return task
        
    def get_task(self, task_id):
        task = self.session.exec(
            select(Task).where(Task.id == task_id)
        ).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        return task
        
    def complete_task(self, task_id):
        task = self.session.get(Task, task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        task.status = "completed"
        task.progress = 100
        task.updated_at = datetime.now(timezone.utc)
        self.session.add(task)
        self.session.commit()

        self.session.refresh(task)

        return task