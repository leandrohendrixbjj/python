from contextlib import asynccontextmanager
from fastapi import FastAPI
from infra.redis_connection import connect_redis, close_redis_connection

@asynccontextmanager
async def redis_service(app: FastAPI):
    try:
        redis = await connect_redis()
        await redis.ping()
        print("✅ Redis conectado!")
        app.state.redis = redis        
    except Exception as e:
        print(f"❌ Falha ao conectar no Redis: {e}")
        raise RuntimeError(f"Falha na conexão com o Redis: {e} ❌")

    yield

    redis = app.state.redis
    await close_redis_connection(redis)
    print("🛑 Redis desconectado!")
