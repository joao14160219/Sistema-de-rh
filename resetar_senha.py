from app.database import SessionLocal
from app.models.usuario import Usuario
from app.security import gerar_hash_senha

db = SessionLocal()

user = db.query(Usuario).filter_by(username="joaopedro").first()

if not user:
    print("Usuário não encontrado.")
else:
    user.senha_hash = gerar_hash_senha("host123")
    db.commit()
    print("Senha redefinida com sucesso!")
