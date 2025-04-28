from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PessoaCreate(BaseModel):
    nome: str
    data_resposta: Optional[datetime] = None
