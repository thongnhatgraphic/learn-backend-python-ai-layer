from sqlmodel import Session
from sqlmodel import select, text
from app.models.task_model import Task
from uuid import UUID


class TaskRepository: 
    def __init__(self, session: Session):
        self.session = session = session

    def get_tasks_raw(self, user_id: UUID):
        statement = text("""
            SELECT * FROM task
            WHERE user_id = :user_id
            ORDER BY created_at DESC
        """).bindparams(user_id=user_id)
        return self.session.exec(statement)

    def get_all(self, user_id: UUID):
        return self.session.exec(
            select(Task)
            .where(Task.user_id == user_id)
            ).all()
    
    def get_by_id_and_user_id(self, task_id, user_id: UUID):
        return self.session.exec(
            select(Task)
            .where(Task.id == task_id, Task.user_id == user_id)
        ).first()
    
    def create(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def update(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)

        return task

    def delete(self, task: Task):
        self.session.delete(task)
        self.session.commit()
