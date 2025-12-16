# app/security.py

import uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# ==============================
# HASH DE SENHA
# ==============================
def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)

# ==============================
# TOKEN
# ==============================
def gerar_token() -> str:
    return str(uuid.uuid4())
