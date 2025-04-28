import logging
from datetime import datetime

from fastapi import HTTPException
from infra.database_connection import connect_to_db
from schemas import PessoaCreate

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def criar_pessoa(pessoa: PessoaCreate):
    try:
        db_connection = await connect_to_db()

        # Garante que data_resposta tem timezone
        data_resposta = datetime.now()    
                
        logging.info(f"Registrando pessoa: {pessoa.nome}, Data Resposta: {data_resposta}")
        
        print(f"Registrando pessoa: {pessoa.nome}, Data Resposta: {data_resposta}")

        query = """
        INSERT INTO pessoa (nome, data_resposta)
        VALUES ($1, $2)
        RETURNING id, nome, data_criacao, data_resposta
        """
        values = (pessoa.nome, data_resposta)
        
        nova_pessoa = await db_connection.fetchrow(query, *values)

        return dict(nova_pessoa) if nova_pessoa else None

    except Exception as e:
        logging.error(f"Erro ao criar pessoa: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao criar pessoa.")
    
    finally:
        if 'db_connection' in locals() and db_connection:
            await db_connection.close()
