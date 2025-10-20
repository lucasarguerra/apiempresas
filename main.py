from fastapi import FastAPI, HTTPException, status, Depends, Query
from schemas.user import EmpresaDadosGerais
from config.db import Session
from model.user import User
from typing import Optional

app = FastAPI()

# Dependência de sessão
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


# ========== CREATE ==========
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: EmpresaDadosGerais, db: Session = Depends(get_db)):
    """
    Cadastra uma nova empresa, verificando duplicidade de CNPJ e e-mail.
    """
    # Verifica duplicidade de CNPJ
    if db.query(User).filter(User.cnpj == user.cnpj).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma empresa cadastrada com esse CNPJ."
        )

    # Verifica duplicidade de e-mail
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma empresa cadastrada com esse e-mail."
        )

    new_user = User(
        name=user.name,
        cnpj=user.cnpj,
        cidade=user.cidade,
        ramo_atuacao=user.ramo_atuacao,
        telefone=user.telefone,
        email=user.email,
        data_de_cadastro=user.data_de_cadastro
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ========== READ - LISTAGEM ==========
@app.get("/users")
def get_users(
    cidade: Optional[str] = Query(None),
    ramo_atuacao: Optional[str] = Query(None),
    name: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Lista todas as empresas, com filtros opcionais:
    - cidade
    - ramo_atuacao
    - busca por nome (texto parcial)
    """
    query = db.query(User)

    if cidade:
        query = query.filter(User.cidade.ilike(f"%{cidade}%"))
    if ramo_atuacao:
        query = query.filter(User.ramo_atuacao.ilike(f"%{ramo_atuacao}%"))
    if name:
        query = query.filter(User.name.ilike(f"%{name}%"))

    results = query.all()

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma empresa encontrada com os parâmetros informados."
        )

    return results


# ========== READ - DETALHE POR ID ==========
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    Retorna os dados de uma única empresa pelo ID.
    """
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Empresa com ID {user_id} não encontrada."
        )

    return user


# ========== UPDATE ==========
@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: EmpresaDadosGerais, db: Session = Depends(get_db)):
    """
    Atualiza os dados de uma empresa existente.
    Não permite alterar: id, cnpj e data_de_cadastro.
    """
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Empresa com ID {user_id} não encontrada."
        )

    # Atualiza apenas os campos permitidos
    user.name = user_update.name
    user.cidade = user_update.cidade
    user.ramo_atuacao = user_update.ramo_atuacao
    user.telefone = user_update.telefone
    user.email = user_update.email

    db.commit()
    db.refresh(user)

    return user


# ========== DELETE ==========
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Exclui uma empresa existente pelo ID.
    """
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Empresa com ID {user_id} não encontrada."
        )

    db.delete(user)
    db.commit()

    return {"message": f"Empresa com ID {user_id} foi excluída com sucesso."}
