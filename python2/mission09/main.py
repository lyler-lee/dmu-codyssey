from contextlib import asynccontextmanager
from typing import Generator, List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Question


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    pass


app = FastAPI(lifespan=lifespan)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/questions', response_model=List[dict])
def get_questions(db: Session = Depends(get_db)) -> List[dict]:
    questions = db.query(Question).all()
    result: List[dict] = []
    for item in questions:
        result.append(
            {
                'id': item.id,
                'subject': item.subject,
                'content': item.content,
                'create_date': item.create_date.isoformat(),
            },
        )
    return result