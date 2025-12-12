from typing import Generator, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Question
from schemas import QuestionSchema

router = APIRouter(
    prefix='/api/question',
)


def get_db_dependency() -> Generator[Session, None, None]:
    with get_db() as db:
        yield db


@router.get('/', response_model=List[QuestionSchema])
def question_list(db: Session = Depends(get_db_dependency)) -> List[QuestionSchema]:
    questions = db.query(Question).all()
    return [QuestionSchema.model_validate(item) for item in questions]
