import httpx

async def buy_btc(valor_compra, porcentagem):
    par = "BTCBRL"
    url = f"https://www.binance.com/api/v3/ticker/price?symbol={par}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        resposta = response.json()
        cotacao = float(resposta["price"])
        spread = 0
        taxa_pix = 0.00
        fee_pix = taxa_pix
        valor_com_taxa = valor_compra - fee_pix
        fee_service_brl = (valor_com_taxa * porcentagem) / 100
        taxa_total = fee_service_brl + taxa_pix
        total_comprado = valor_com_taxa - fee_service_brl
        price_compra = cotacao + (cotacao * spread / 100)
        quantidade = total_comprado / price_compra
        quantidade_remake = round(quantidade, 8)  # Ajustando para 8 casas decimais

        
        # Retornando os valores calculados como um dicionário
        return { "quantidade": quantidade_remake}
    else:

        return {"error": f"Erro ao acessar API Binance: {response.status_code}"}
    
async def buy_usdt(valor_compra, porcentagem):
    par = "USDTBRL"
    url = f"https://www.binance.com/api/v3/ticker/price?symbol={par}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        resposta = response.json()
        cotacao = float(resposta["price"])
        spread = 0
        taxa_pix = 0.00
        fee_pix = taxa_pix
        valor_com_taxa = valor_compra - fee_pix
        fee_service_brl = (valor_com_taxa * porcentagem) / 100
        taxa_total = fee_service_brl + taxa_pix
        total_comprado = valor_com_taxa - fee_service_brl
        price_compra = cotacao + (cotacao * spread / 100)
        quantidade = total_comprado / price_compra
        quantidade_remake = round(quantidade, 8)  # Ajustando para 8 casas decimais

        
        # Retornando os valores calculados como um dicionário
        return { "quantidade": quantidade_remake}
    else:

        return {"error": f"Erro ao acessar API Binance: {response.status_code}"}    
    
async def var_valor(valor):
    if valor <= 9999.99:
        taxa = 7
    elif 10000 <= valor < 20000:
        taxa = 6
    elif valor >= 20000:
        taxa = 5
    
    # Chama a função responder_BTC e retorna seu resultado
    return await buy_btc(valor, taxa)

async def var_valor_usdt(valor):
    if valor <= 9999.99:
        taxa = 7
    elif 10000 <= valor < 20000:
        taxa = 6
    elif valor >= 20000:
        taxa = 5
    
    # Chama a função responder_BTC e retorna seu resultado
    return await buy_usdt(valor, taxa)    