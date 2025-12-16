from app.database import SessionLocal
from app.models.usuario import Usuario

db = SessionLocal()

apagados = db.query(Usuario).delete()
db.commit()
db.close()

print(f"Usuários apagados: {apagados}")
