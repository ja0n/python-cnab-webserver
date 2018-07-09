import json
from decimal import *

from cnab240.bancos import banco_brasil
from cnab240.tipos import Arquivo


def gera_remessa():
    json_str = open('./data.json', 'r').read()
    data = json.loads(json_str)
    remessa = processa_pagamentos(data)
    return remessa

def processa_pagamentos(data):
    arquivo = Arquivo(banco_brasil, **data)
    pagamentos = data.get('pagamentos')
    valor_total = Decimal(0.0)
    # "arquivo_data_de_geracao": "01041990",
    # "arquivo_hora_de_geracao": "235959",

    for pagamento in pagamentos:
        arquivo.incluir_pagamentos_diversos(**data, **pagamento)
        valor_total += Decimal(pagamento.get('valor', 0.0))

    arquivo.lotes[0].trailer.somatorio_valor = valor_total
    return str(arquivo)
