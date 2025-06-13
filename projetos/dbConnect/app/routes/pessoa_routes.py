from fastapi import APIRouter, Request, HTTPException
import random
from schemas import PessoaCreate
from crud import criar_pessoa

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@router.post("/pessoas", response_model=dict)
async def criar_pessoa_endpoint(pessoa: PessoaCreate):
    try:
        nova_pessoa = await criar_pessoa(pessoa)
        return nova_pessoa
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/redis")
async def set_key(request: Request):
    nomes = ['Maria', 'Ana', 'Julia', 'Laura', 'Beatriz', 'Camila', 'Isabela',
             'Fernanda', 'Patrícia', 'Amanda', 'Carolina', 'Clara', 'Mariana', 'Sofia']
    key = f"user:{random.randint(0, 12)}"
    value = random.choice(nomes)

    try:
        redis = request.app.state.redis
        result = await redis.set(key, value)
        if result:
            return {"message": f"Chave '{key}' salva com valor '{value}'"}
        else:
            return {"error": "Erro ao salvar valor"}
    except Exception as e:
        return {"error": str(e)}
