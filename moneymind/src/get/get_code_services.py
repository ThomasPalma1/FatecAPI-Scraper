import requests
import json


def get_code_services():
    url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifaPorValores/versao/v1/odata/ServicosBancarios"
    response = requests.get(url)
    data = json.loads(response.text)

    true_results = data['value']

    return true_results
