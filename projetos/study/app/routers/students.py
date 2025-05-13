from itertools import islice
from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query
from app.model.students_data import students as data

router = APIRouter()

@router.get('/')
def index():
    return {'message': 'Welcome to FastAPI'}


@router.get('/students', tags=['Listagem']) 
def get_students(limit: Optional[int] = Query(None, description="Qtd total de registros")) -> dict:
    if limit is None:
        return data
    
    return dict(islice(data.items(),limit))
    


@router.get('/students/{student_id}', tags=['Busca um Registro'])
def get_students_by_id(student_id: int = Path(..., description='Informe o id do estudante', gt=0)) -> Optional[dict]:
    student = data.get(student_id) 
    
    if not student or not student_id:
        raise HTTPException(status_code=404, detail='Student not found')
    return student

@router.post('/students', tags=['Cria um novo Estudante'])
def create_students(body: dict)-> dict:    
    data_id = max(data.keys()) + 1
    data[data_id] = body
    return {'id':data_id, **body}

@router.put('/students/{student_id}', tags=['Editar um Estudante'])
def edit_students(body: dict, student_id: int = Path(..., description='Informe um ID para o estudante')) -> dict:
    if not student_id in data:
        raise HTTPException(status_code=400, detail='Não achou um id')
    data[student_id] = body
    return {'id': student_id, **body}

@router.delete('/students/{student_id}', tags=['Remover um Estudante'])
def delete_students(student_id: int):
    del data[student_id]
    return {'message': 'Students was deleted'}