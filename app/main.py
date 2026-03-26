from fastapi import FastAPI

from app.database import create_db
from contextlib import asynccontextmanager
from app.routers.task_router import router as task_router




@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 START APP---------------------")

    create_db()
    print("✅ Database created")

    yield

    print("🛑 SHUTDOWN")


app = FastAPI(lifespan=lifespan)

app.include_router(task_router)


