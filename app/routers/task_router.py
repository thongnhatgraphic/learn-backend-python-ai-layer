from fastapi import APIRouter
from pydantic import BaseModel

from app.models.task_model import Task
from app.services.task_service import TaskService

router = APIRouter()

task_service = TaskService()

class TaskRequest(BaseModel):
    name: str
    progress: int

@router.get("/tasks")
async def get_tasks():
    return {
        "data": task_service.get_tasks(),
        "message": "List of tasks"
    }

@router.get("/tasks/{task_id}")
async def get_tasks(task_id: int):
    return {
        "data": task_service.get_tasks(task_id),
        "message": "List of tasks"
    }

@router.post("/tasks")
async def create_task(task : TaskRequest):
    return {
        "data": task_service.create_task(task.name),
        "message": "Task added"
    }

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task : TaskRequest):
    return {
        "data": task_service.update_task(task_id, task.name, task.progress),
        "message": "Task updated"
    }

@router.delete("/tasks/{task_id}")
async def delete_task(task_id : int):
    return {
        "data": task_service.delete_task(task_id),
        "message": "Task was deleted"
    }

@router.put('/tasks/{task_id}/complete')
async def complete_task(task_id: int):
    return {
        "data": task_service.complete_task(task_id),
        "message": "Task completed"
    }