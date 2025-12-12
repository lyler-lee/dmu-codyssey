from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import Base, engine
from domain.question.question_router import router as question_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(question_router)


# main.py 실행으로 uvicorn 서버 구동 가능
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)