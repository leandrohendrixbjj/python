from idlelib.query import Query
from itertools import islice
from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query
from app.model.data import students
router = APIRouter()

@router.get('/', tags=["root"])
def index():
    return {'message': 'Hello World!'}

@router.get('/students/', tags=['students'])
def get_students(limit: Optional[int] = Query(None, description="Quantidade de Registro que Deseja Retornar")) -> dict:
    if not limit:
        return students
    return dict(islice(students.items(), limit))

@router.get('/students/{student_id}', tags=['students'])
def get_student_by_id(student_id: int = Path(..., description="Student ID", gt=0)) -> dict:
    data = students.get(student_id)
    if data is None:
         raise HTTPException(status_code=404, detail='Student not found')
    return {'data': students}