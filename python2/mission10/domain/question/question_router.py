from typing import Dict, Generator, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix='/api/question',
)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/', response_model=List[Dict])
def question_list(db: Session = Depends(get_db)) -> List[Dict]:
    questions = db.query(Question).all()
    result: List[Dict] = []
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
