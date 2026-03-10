from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.serie import SerieModel
from app.Schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

# Tarefa: Crie as rotas de atualização e deleção da API
@serie.put("/update")
async def atualizar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    dados = db.query(SerieModel).filter(SerieModel.SerieSchema == dados).first()
    if not dados:
        return("Série não encontrada")   
    for key, value in dados.model_dump().items():
        setattr(dados, key, value)  

    db.commit()
    db.refresh(dados)
    return dados

    




@serie.delete("/delete")
async def deletar_serie(id: int, db: Session = Depends(get_db)):
    id = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not id:
     return ("Id não encontrado")
    
    db.delete(id)
    db.commit()
    return ("Deletado")




