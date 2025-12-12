import csv
import os
from typing import Dict, List, Optional

from fastapi import APIRouter, FastAPI, HTTPException
from model import TodoItem

app = FastAPI()
router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, 'todo_list.csv')
FIELDNAMES = ['id', 'task', 'done', 'description']
todo_list: List[Dict] = []


def load_todo_list() -> List[Dict]:
    items: List[Dict] = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.append(row)
    return items


def save_todo_list(items: List[Dict]) -> None:
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for item in items:
            writer.writerow(item)


def get_next_id(items: List[Dict]) -> int:
    if not items:
        return 1
    max_id = max(int(item['id']) for item in items)
    return max_id + 1


def find_todo_index_by_id(items: List[Dict], todo_id: int) -> Optional[int]:
    for index, item in enumerate(items):
        if int(item['id']) == todo_id:
            return index
    return None


todo_list = load_todo_list()


@router.post('/add_todo')
async def add_todo(item: TodoItem) -> Dict:
    items = load_todo_list()
    if item.id == 0:
        item_id = get_next_id(items)
    else:
        item_id = item.id

    new_item = {
        'id': str(item_id),
        'task': item.task,
        'done': 'True' if item.done else 'False',
        'description': item.description or '',
    }

    items.append(new_item)
    save_todo_list(items)
    return {'result': 'created', 'item': new_item}


@router.get('/retrieve_todo')
async def retrieve_todo() -> Dict:
    items = load_todo_list()
    return {'todos': items}


@router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int) -> Dict:
    items = load_todo_list()
    index = find_todo_index_by_id(items, todo_id)
    if index is None:
        raise HTTPException(status_code=404, detail='Todo item not found')
    return {'item': items[index]}


@router.put('/todo/{todo_id}')
async def update_todo(todo_id: int, item: TodoItem) -> Dict:
    items = load_todo_list()
    index = find_todo_index_by_id(items, todo_id)
    if index is None:
        raise HTTPException(status_code=404, detail='Todo item not found')

    updated_item = {
        'id': str(todo_id),
        'task': item.task,
        'done': 'True' if item.done else 'False',
        'description': item.description or '',
    }

    items[index] = updated_item
    save_todo_list(items)
    return {'result': 'updated', 'item': updated_item}


@router.delete('/todo/{todo_id}')
async def delete_single_todo(todo_id: int) -> Dict:
    items = load_todo_list()
    index = find_todo_index_by_id(items, todo_id)
    if index is None:
        raise HTTPException(status_code=404, detail='Todo item not found')

    deleted_item = items.pop(index)
    save_todo_list(items)
    return {'result': 'deleted', 'item': deleted_item}


app.include_router(router)


# todo.py 실행으로 uvicorn 서버 시작
if __name__ == '__main__':
    import uvicorn

    uvicorn.run('todo:app', host='127.0.0.1', port=8000, reload=True)
