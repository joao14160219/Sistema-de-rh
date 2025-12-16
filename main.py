from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from app.init_db import init_db

# Rotas
from app.routes.login import router as login_router
from app.routes.usuarios import router as usuarios_router
from app.routes.funcionarios import router as funcionarios_router
from app.routes.dashboard import router as dashboard_router


# ============================================================
#                CONFIGURAÇÃO DO FASTAPI
# ============================================================
app = FastAPI(
    title="HRManager API",
    version="2.0.0",
    description="Backend Corporativo do HRManager",
    contact={
        "name": "João Pedro",
        "email": "seu-email@empresa.com"
    }
)

# Inicializar DB e usuário host
init_db()


# ============================================================
#                   CONFIGURAÇÃO DE CORS
# ============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Em produção: restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
#                EVENTOS DE STARTUP & SHUTDOWN
# ============================================================
@app.on_event("startup")
async def startup_event():
    print("🚀 HRManager API iniciada com sucesso.")


@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 HRManager API desligada.")


# ============================================================
#                 MIDDLEWARE DE LOG DE REQUISIÇÕES
# ============================================================
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"➡ Nova requisição: {request.method} {request.url}")
    response = await call_next(request)
    print(f"⬅ Resposta: {response.status_code}")
    return response


# ============================================================
#                TRATAMENTO GLOBAL DE ERROS
# ============================================================

# Erros de validação (pydantic)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Erro de validação",
            "errors": exc.errors()
        }
    )


# Erros gerais
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    print("⚠ ERRO NO SERVIDOR:", exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno no servidor"}
    )


# ============================================================
#                   REGISTRO DAS ROTAS
# ============================================================
app.include_router(login_router)
app.include_router(usuarios_router)
app.include_router(funcionarios_router)
app.include_router(dashboard_router)


# ============================================================
#                      ROTA PRINCIPAL
# ============================================================
@app.get("/")
def root():
    return {
        "status": "online",
        "sistema": "HRManager API",
        "versao": "2.0.0",
        "autor": "João Pedro"
    }
