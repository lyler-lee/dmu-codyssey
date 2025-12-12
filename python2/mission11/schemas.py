from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


class QuestionSchema(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime

    model_config = ConfigDict(from_attributes=True)


class QuestionListSchema(BaseModel):
    questions: List[QuestionSchema]
