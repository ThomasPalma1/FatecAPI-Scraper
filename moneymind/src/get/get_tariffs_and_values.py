import requests
import json
from requests.exceptions import ConnectionError
from moneymind.src.get.get_consolidated_group import get_consolidated_group
from moneymind.src.get.get_code_services import get_code_services
from urllib3.util.retry import Retry

session = requests.Session()
retry_strategy = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 504])
adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)


def get_all_tariffs_and_value():
    consolidated_group = get_consolidated_group()
    services = get_code_services()

    true_results = []

    for service in services:
        for group in consolidated_group:
            url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifaPorValores/versao/v1/odata/ListaTarifasPorValores(CodigoGrupoConsolidado=@CodigoGrupoConsolidado,CodigoServico=@CodigoServico)?@CodigoGrupoConsolidado='{group['Codigo']}'&@CodigoServico='{service['Codigo']}'&$top=10000&$format=json"
            try:
                response = session.get(url)
                response.raise_for_status()
                data = json.loads(response.text)
                results = data['value']

                if results:
                    for result in results:
                        if result["Cnpj"]:
                            data_tariffs_values = (
                                result["Cnpj"],
                                result["RazaoSocial"],
                                result["ValorMaximo"],
                                result["Periodicidade"],
                                service["Codigo"],
                                group["Codigo"],
                            )
                            true_results.append(data_tariffs_values)
                            print(data_tariffs_values)
                        else:
                            print("Empty Tariffs and value.")
            except (ConnectionError, requests.exceptions.HTTPError) as e:
                print(f"Connection error occurred: {e}.")
            except Exception as e:
                print(f"An error occurred: {e}.")
    return true_results
