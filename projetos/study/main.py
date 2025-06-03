from app.helper import clear
from fastapi import FastAPI
from app.infra.lifespan import lifespan
from app.routes.students import router as students_router

clear.screen()

app = FastAPI(lifespan=lifespan)

app.include_router(students_router)

