# redis_client.py
import redis.asyncio as redis

redis_client: redis.Redis | None = None

async def connect_redis() -> redis.Redis:
    global redis_client
    if redis_client is None:
        redis_client = redis.Redis(
            host="redis",
            port=6379,
            decode_responses=True
        )
    return redis_client

async def close_redis_connection(client: redis.Redis):
    client.close()
    await client.wait_closed()
