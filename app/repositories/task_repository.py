from fastapi import HTTPException
from datetime import datetime, timezone

from sqlmodel import Session
from sqlmodel import select
from app.models.task_model import Task

class TaskRepository: 
    def __init__(self, session: Session):
        self.session = session = session

    def get_all(self):
        return self.session.exec(
            select(Task)
            ).all()
    
    def get_by_id(self, task_id):
        return self.session.exect(
            select(Task)
            .where(Task.id == task_id)
        ).first()
    
    def create(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)

        return task

    def update(self, task_id, name, progress):
        task = self.session.get(Task, task_id)

        task.name = name
        task.progress = progress
        task.updated_at = datetime.now(timezone.utc)
        self.session.add(task)
        self.session.commit()

        self.session.refresh(task)

        return task

    def delete(self, id):
        task = self.session.exec(
            select(Task)
            .where(Task.id == id)
        ).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        self.session.delete(task)
        self.session.commit()

        return task
