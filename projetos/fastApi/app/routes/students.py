from itertools import islice
from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query
from app.models.students_data import students

router = APIRouter()

@router.get('/')
def index():
    return {'message': 'Welcome to FastApi'}

@router.get('/students/', tags=['List All'])
def get_students(limit: Optional[int] = Query(None, description="Quantidade de Registro que Deseja Retornar")) -> dict:
    if limit is None:
        return students
    return dict(islice(students.items(), limit))

@router.get('/students/{student_id}', tags=['Seek one student'])
def get_student_by_id(student_id: int = Path(..., description="Informe o ID do Estudante", gt=0)) -> dict:
    student = students.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student

@router.post('/students/', tags=['Create a new student'])
def create_student(student: dict) -> dict:
    student_id = max(students.keys()) + 1
    students[student_id] = student
    return {'id': student_id, **student}

@router.put('/students/{student_id}', tags=['Edit a student'])
def update_student(student: dict, student_id: int = Path(..., description="Informe o ID do Estudante", gt=0)) -> dict:
    if student_id not in students:
        raise HTTPException(status_code=404, detail='Student not found')
    students[student_id] = student
    return {'id': student_id, **student}

@router.delete('/students/{student_id}', tags=['Delete a student'])
def delete_student(student_id: int = Path(..., description="Informe o ID do Estudante", gt=0)) -> dict:
    if student_id not in students:
        raise HTTPException(status_code=404, detail='Student not found')
    del students[student_id]
    return {'message': 'Student deleted successfully'}


