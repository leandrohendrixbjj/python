import uvicorn
from fastapi import FastAPI
from infra.database_connection import connect_to_db
from app.middleware.redis_service import redis_service
from routes.pessoa_routes import router as pessoa_router

app = FastAPI()
app = FastAPI(lifespan=redis_service)    

# Registra as rotas
app.include_router(pessoa_router)

if __name__ == '__main__':
      connect_to_db            
      uvicorn.run(app, host="0.0.0.0", port=8005)


