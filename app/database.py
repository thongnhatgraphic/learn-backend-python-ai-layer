from sqlmodel import SQLModel, create_engine

sqlite_url = "sqlite:///./tasks.db"

engine = create_engine(sqlite_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)
    