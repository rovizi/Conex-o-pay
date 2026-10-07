from fastapi import FastAPI
from pydantic import BaseModel
from services import criar_pagamento_pix
from config import settings

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

class PagamentoRequest(BaseModel):
    valor: float
    descricao: str
    email_comprador: str

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Conexão Pay - Produção Rodando 🚀"}

@app.post("/api/pagar/pix")
async def gerar_pix(dados: PagamentoRequest):
    resultado = await criar_pagamento_pix(
        valor=dados.valor,
        descricao=dados.descricao,
        email_comprador=dados.email_comprador
    )
    return resultado