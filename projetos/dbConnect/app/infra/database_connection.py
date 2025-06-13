from fastapi import HTTPException
import asyncpg

async def connect_to_db():
    try:
        conn = await asyncpg.connect(
            user='postgres',
            password='secret',
            database='estudo',
            host='db',  # Nome do serviço no Docker
            port=5432
        )
        print("Conectado ao Postgre! 😊")
        return conn
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Falha na conexão com o banco de dados: {e} ❌"
        )
