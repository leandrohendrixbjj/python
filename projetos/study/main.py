from app.helper.clear import clear
from fastapi import FastAPI
from app.infra.lifespan import lifespan
from app.routers.students import router as students_router

clear()

app = FastAPI(lifespan=lifespan)

app.include_router(students_router)

print('Welcome')