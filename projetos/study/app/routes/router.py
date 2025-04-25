from itertools import islice

from fastapi import APIRouter, HTTPException, Query, Depends
from app.model.students import students

router = APIRouter()

@router.get('/')
async def index():
    return {'message': 'Hello World!'}

@router.get('/students/')
async def get_student(limit : int = Query(default=None,description='Id Estudante')):
    if not students:
        return HTTPException(status_code=404, detail="No students found")

    if int:
        return dict(islice(students.items(), limit))

    return {'data': students}

@router.get('/students/{id}')
async def get_student(id: int):
    if not id or not students:
        return HTTPException(status_code=404, detail="No students found")
    else:
        return {'data': students[id]}

@router.post('/students/')
async def create_student(data: dict):
    if not data:
        return HTTPException(status_code=404, detail="No students found")
    students.update(data)
    return {'data': students}

