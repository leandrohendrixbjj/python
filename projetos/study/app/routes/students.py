from typing import Optional
from fastapi import APIRouter, Query, Path, HTTPException
from app.model.students import students

router = APIRouter()

@router.get("/")
async def index():
    return {"message": "Welcome to Students"}

@router.get("/students")
async def get_all(limit: Optional[int] = Query(None, description="Limitar a quantdade de registros"), tags=["Lista Todos"])-> dict:
    if limit is None:
        return dict(students)
    return dict(list(students.items())[:limit])

@router.get("/students/{student_id}", tags=["Buscar um estudante"]) 
async def get_by_id(student_id: int = Path(..., description="Informe ID do estudante", gt=0))-> dict:  
    if student_id is None:
        return {"message": "Student ID is required"}

    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
     
    return students.get(student_id)
    