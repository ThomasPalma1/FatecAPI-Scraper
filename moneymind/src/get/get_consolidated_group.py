import requests
import json


def get_consolidated_group():
    url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaValoresDeServicoBancario/versao/v1/odata" \
          f"/GruposConsolidados"
    response = requests.get(url)
    data = json.loads(response.text)
    true_results = data['value']
    return true_results
