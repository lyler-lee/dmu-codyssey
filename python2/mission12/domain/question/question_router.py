from datetime import datetime, timezone
from typing import Generator, List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from models import Question
from schemas import QuestionCreate, QuestionSchema

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


@router.post(
    '/',
    response_model=QuestionSchema,
    status_code=status.HTTP_201_CREATED,
)
def question_create(
    question: QuestionCreate,
    db: Session = Depends(get_db_dependency),
) -> QuestionSchema:
    db_question = Question(
        subject=question.subject,
        content=question.content,
        create_date=datetime.now(timezone.utc),
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return QuestionSchema.model_validate(db_question)
