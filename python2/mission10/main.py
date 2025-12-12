

from contextlib import asynccontextmanager
from typing import Generator

from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base

 

from domain.question.question_router import router as question_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown 시 별도 작업 없음


app = FastAPI(lifespan=lifespan)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(question_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)