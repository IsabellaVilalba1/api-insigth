from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/leadtime-mult")
def get_leadtime_mult():
    session = requests.Session()

    url = "https://transplex.insightcargo.com.br/api/producao/expedicao/leadtime"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://transplex.insightcargo.com.br",
        "Referer": "https://transplex.insightcargo.com.br/reports/production/expeditions/leadtime",
        "Authorization": "3f6bace7243116c16c1e008f62b49da3"
    }

    filiais = [18, 21, 22, 24, 31]
    meses = [1, 2, 3, 4, 5, 6]
    ano = 2025

    resultados = []

    for filial in filiais:
        for mes in meses:
            data = {
                "filial": str(filial),
                "mes": str(mes),
                "ano": str(ano)
            }

            response = session.post(url, headers=headers, data=data)
            try:
                json_data = response.json()
                resultados.append({
                    "filial": filial,
                    "mes": mes,
                    "ano": ano,
                    "dados": json_data
                })
            except:
                resultados.append({
                    "filial": filial,
                    "mes": mes,
                    "ano": ano,
                    "erro": "Falha ao interpretar resposta",
                    "resposta_texto": response.text
                })

    return resultados
