import json
import requests
from get_consolidated_group import get_consolidated_group


def get_institutions():
    consolidated_group = get_consolidated_group()
    for group in consolidated_group:
        url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifasPorInstituicaoFinanceira/versao/v1/odata/ListaInstituicoesDeGrupoConsolidado(CodigoGrupoConsolidado=@CodigoGrupoConsolidado)?@CodigoGrupoConsolidado='{group['Codigo']}'&$top=10000&$format=json"
        response = requests.get(url)
        data = json.loads(response.text)
        true_results = data['value']
        return true_results
