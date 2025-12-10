from fastapi import FastAPI, APIRouter, Request
from typing import Dict, List
import csv
import os

app = FastAPI()
router = APIRouter()

todo_list = []

CSV_FILE = 'todo_list.csv'


def load_todo_list() -> List[Dict]:
    items = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.append(row)
    return items


def save_todo_list(items: List[Dict]) -> None:
    if items:
        keys = items[0].keys()
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            for item in items:
                writer.writerow(item)

# 초기 로드
todo_list = load_todo_list()


@router.post('/add_todo')
async def add_todo(request: Request) -> Dict:
    data = await request.json()
    todo_list.append(data)
    save_todo_list(todo_list)
    return {'result': 'ok', 'item': data}


@router.get('/retrieve_todo')
async def retrieve_todo() -> Dict:
    items = load_todo_list()
    return {'todos': items}


app.include_router(router)  

