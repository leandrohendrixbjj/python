from app.helper.clear import clear
from fastapi import FastAPI
from app.infra.lifespan import lifespan 
from app.routes.students import router as students_router

clear()

app = FastAPI(lifespan=lifespan)

# Incluindo as rotas de estudantes
app.include_router(students_router)

