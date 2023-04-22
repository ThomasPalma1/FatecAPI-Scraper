import requests
import json


def get_services(person, group_code):
    # API endpoint URL with filters and pagination
    url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaValoresDeServicoBancario/versao/v1/odata" \
          f"/ListaValoresServicoBancario(PessoaFisicaOuJuridica=@PessoaFisicaOuJuridica," \
          f"CodigoGrupoConsolidado=@CodigoGrupoConsolidado)?@PessoaFisicaOuJuridica='" \
          f"{person}'&@CodigoGrupoConsolidado='{group_code}'&$top=100&$format=json"

    # Send a GET request to the API and get the JSON response
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract the list of services and fees from the JSON data
    true_results = data['value']

    return true_results


# Example usage: get the list of banking services and fees for companies (pessoa='J') in the service category '01''
results = get_services('J', '01')

pretty_json = json.dumps(results, indent=4, ensure_ascii=False)
