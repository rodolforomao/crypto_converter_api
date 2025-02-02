import httpx

DEPIX_TAX = 0.99  # Taxa fixa do Pix

async def get_binance_price(pair: str) -> float:
    """Obtém a cotação atual do par de moedas na Binance."""
    url = f"https://www.binance.com/api/v3/ticker/price?symbol={pair}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return float(response.json().get("price", 0))
    
    raise Exception(f"Erro ao acessar API Binance: {response.status_code}")

async def trade_crypto(amount: float, pair: str, operation: str) -> dict:
    """Realiza compra ou venda de criptomoeda com base na cotação da Binance."""
    if operation not in ["buy", "sell"]:
        return {"error": "Operação inválida. Use 'buy' ou 'sell'."}

    try:
        price = await get_binance_price(pair)
        tax_rate = get_trade_tax(amount)
        fee_service_brl = (amount * tax_rate) / 100

        total = amount - fee_service_brl - DEPIX_TAX if operation == "buy" else amount + fee_service_brl + DEPIX_TAX
        quantity = total / price

        return {"quantidade": round(quantity, 8)}

    except Exception as e:
        return {"error": str(e)}

def get_trade_tax(amount: float) -> int:
    """Determina a taxa de negociação com base no valor."""
    return 7 if amount <= 9999.99 else 6 if amount < 20000 else 5

# Exemplo de uso:
# import asyncio
# asyncio.run(trade_crypto(5000, 'BTCBRL', 'buy'))
