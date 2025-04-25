from app.helper.clear import clear
from app.infra.lifespan import lifespan
from fastapi import FastAPI
from app.routers.router import router

clear()

app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == '__main__':
    print('Welcome_2')