from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


@contextmanager
def get_db() -> Generator[Session, None, None]:
    print('DB 세션 생성') 
    db = SessionLocal()
    try:
        yield db
    finally:
        print('DB 세션 종료') 
        db.close()
