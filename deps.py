from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.sessao import Sessao
from app.models.usuario import Usuario


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usuario_atual(
    x_token: str = Header(..., alias="X-Token"),
    db: Session = Depends(get_db)
) -> Usuario:
    sessao = db.query(Sessao).filter(
        Sessao.token == x_token,
        Sessao.ativo == True
    ).first()

    if not sessao:
        raise HTTPException(status_code=401, detail="Sessão inválida ou expirada")

    return sessao.usuario
