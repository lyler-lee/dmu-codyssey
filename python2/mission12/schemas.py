from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class QuestionSchema(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime

    model_config = ConfigDict(from_attributes=True)


class QuestionCreate(BaseModel):
    subject: str = Field(min_length=1)
    content: str = Field(min_length=1)


class QuestionListSchema(BaseModel):
    questions: List[QuestionSchema]
