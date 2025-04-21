from itertools import islice
from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query
from app.models.students_data import students

router = APIRouter()

@router.get('/')
def index():
    return {'message': 'Welcome to FastApi'}

@router.get('/students/', tags=['Students'])
def get_students(limit: Optional[int] = Query(None, description="Quantidade de Registro que Deseja Retornar")) -> dict:
    if limit is None:
        return students
    return dict(islice(students.items(), limit))

@router.get('/students/{student_id}', tags=['Students'])
def get_student_by_id(student_id: int = Path(..., description="Informe o ID do Estudante", gt=0)) -> dict:
    student = students.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student


