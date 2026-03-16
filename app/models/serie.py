# Modelo para o banco de dados 
from sqlalchemy import Column, Integer, String
from app.database import Base

class SerieModel(Base):
    __tablename__ = 'serie'

    id = Column(Integer, primary_key= True, autoincrement= True)
    titulo= Column(String(100), nullable= False)
    descriçao = Column(String(255))
    ano_lançamento = Column(Integer)

class update(BaseModel):
    titulo: Optional [str] = None
    descriçao: Optional[str] = None
    ano_lançamento: Optional [int] = None

    class Config: 
        from_attributes = True