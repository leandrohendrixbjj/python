from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI): 
    print('🚀 Aplicação iniciada!')
    print('🔗 Acesse: http://127.0.0.1:8001')
    print('📘 Documentação: http://127.0.0.1:8001/docs')
    yield
    print('👋 Aplicação finalizada.')

    