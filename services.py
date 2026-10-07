import httpx
from fastapi import HTTPException
from config import settings

async def criar_pagamento_pix(valor: float, descricao: str, email_comprador: str):
    url = "https://api.mercadopago.com/v1/payments"
    
    headers = {
        "Authorization": f"Bearer {settings.MP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "transaction_amount": float(valor),
        "description": descricao,
        "payment_method_id": "pix",
        "payer": {
            "email": email_comprador
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        
        if response.status_code not in [200, 201]:
            raise HTTPException(
                status_code=response.status_code, 
                detail=f"Erro ao gerar pagamento no Mercado Pago: {response.text}"
            )
            
        data = response.json()
        
        ponto_de_inclusao = data.get("point_of_interaction", {})
        qr_code_data = ponto_de_inclusao.get("transaction_data", {})
        
        return {
            "payment_id": data.get("id"),
            "status": data.get("status"),
            "qr_code": qr_code_data.get("qr_code"),
            "qr_code_base64": qr_code_data.get("qr_code_base64"),
            "ticket_url": qr_code_data.get("ticket_url")
        }