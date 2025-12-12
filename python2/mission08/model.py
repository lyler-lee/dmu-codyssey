from typing import Optional

from pydantic import BaseModel


class TodoItem(BaseModel):
    id: int
    task: str
    done: bool
    description: Optional[str] = None
