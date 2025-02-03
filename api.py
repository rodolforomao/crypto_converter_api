from fastapi import FastAPI, Query
from main import trade_crypto

app = FastAPI()

@app.get("/V1/API/trade", 
         tags=["Trading"],
         summary="Calcula quantidade de cripto",
         description="Retorna a quantidade de cripto comprada ou vendida com base no valor fiat.")
async def trade(
    amount: float = Query(..., description="Valor em BRL para conversão"),
    pair: str = Query(..., description="Par de moedas (exemplo: BTCBRL, USDTBRL)"),
    operation: str = Query(..., description="Operação desejada: 'buy' ou 'sell'"),
    tax_rate: float = Query(..., description="Taxa que será cobrada")
    
):
    if operation not in ["buy", "sell"]:
        return {"error": "Operação inválida. Use 'buy' ou 'sell'."}

    resultado = await trade_crypto(amount, pair, operation, tax_rate)

    if "error" in resultado:
        return {"error": resultado["error"]}

    return resultado
