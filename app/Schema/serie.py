from pydantic import BaseModel 
from typing import Optional

class SerieSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano_lancamento: int

    class Config: 
        from_attributes = True


class AtualizarSchema(BaseModel):
    titulo: Optional [str] = None
    descriçao: Optional[str] = None
    ano_lançamento: Optional [int] = None

    class Config: 
        from_attributes = True

