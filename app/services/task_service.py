from fastapi import HTTPException
from datetime import datetime, timezone
from sqlmodel import Session, select
from app.database import engine
from app.models.task_model import Task


class TaskService:
    # def __init__(self):
    #     self = self

    def create_task(self, name):
        with Session(engine) as session:
            task = Task(name=name, status="pending")

            session.add(task)
            session.commit()

            session.refresh(task)
            return task

    def get_tasks(self):
        with Session(engine) as session:
            return session.exec(select(Task)).all()


    def delete_task(self, task_id):
        with Session(engine) as session:
            task = session.get(Task, task_id)
        
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
    
            session.delete(task)
            session.commit()
            return {"id": task_id}

    def update_task(self, task_id, name, progress):
        with Session(engine) as session:
            task = session.get(Task, task_id)

            if not task:
                raise HTTPException(status_code=404, detail="Task not found")

            task.name = name
            task.progress = progress
            task.updated_at = datetime.now(timezone.utc)
            session.add(task)
            session.commit()

            session.refresh(task)

            return task
        
    def get_task(self, task_id):
        with Session(engine) as session:
            task = session.exec(
                select(Task).where(Task.id == task_id)
            ).first()

            if not task:
                raise HTTPException(status_code=404, detail="Task not found")

            return task
        
    def complete_task(self, task_id):
        with Session(engine) as session:
            task = session.get(Task, task_id)

            if not task:
                raise HTTPException(status_code=404, detail="Task not found")

            task.status = "completed"
            task.progress = 100
            task.updated_at = datetime.now(timezone.utc)
            session.add(task)
            session.commit()

            session.refresh(task)

            return task