from app.database import SessionLocal
from app.models.usuario import Usuario

db = SessionLocal()

usuarios = db.query(Usuario).all()

print("\n=== USUÁRIOS NO BANCO ===")
for u in usuarios:
    print(f"ID: {u.id} | username: {u.username} | role: {u.role} | hash: {u.senha_hash}")

db.close()
