from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base
from config.db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True)
    name = Column(String(50))
    cnpj = Column(String(14))
    cidade = Column(String(50))
    ramo_atuacao= Column(String(50))
    telefone = Column(String(11))
    email = Column(String(50))
    data_de_cadastro = Column(Date)


Base.metadata.create_all(engine)