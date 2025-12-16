from app.database import Base, engine, print_db_path
from app.models.funcionario import Funcionario
from app.models.usuario import Usuario
from app.security import gerar_hash_senha
from app.database import SessionLocal


def init_db():
    print_db_path()
    Base.metadata.create_all(bind=engine)
    criar_host_padrao()


def criar_host_padrao():
    db = SessionLocal()
    try:
        user = db.query(Usuario).filter_by(username="JOAOPEDRO").first()

        if not user:
            db.add(Usuario(
                username="JOAOPEDRO",
                senha_hash=gerar_hash_senha("host123"),
                role="host"
            ))
            db.commit()
    finally:
        db.close()



if __name__ == "__main__":
    init_db()
