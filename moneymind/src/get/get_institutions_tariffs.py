from moneymind.src.get.get_institutions import get_institutions
from urllib3.util.retry import Retry
from requests.exceptions import ConnectionError
import json
import requests

session = requests.Session()
retry_strategy = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 504])
adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)


def get_institutions_tariffs():
    institutions = get_institutions()
    type_person = ['F', 'J']
    true_results = []

    for person in type_person:
        for bank in institutions:
            url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifasPorInstituicaoFinanceira/versao/v1/odata/ListaTarifasPorInstituicaoFinanceira(PessoaFisicaOuJuridica=@PessoaFisicaOuJuridica,CNPJ=@CNPJ)?@PessoaFisicaOuJuridica='{person}'&@CNPJ='{bank['Cnpj']}'&$top=10000&$format=json"
            try:
                response = session.get(url)
                response.raise_for_status()
                response = requests.get(url)
                data = json.loads(response.text)
                results = data['value']

                if results:
                    for result in results:
                        if bank["Cnpj"]:
                            data_tariffs_values_institutions = (
                                result["CodigoServico"],
                                result["Servico"],
                                result["Unidade"],
                                result["DataVigencia"],
                                result["ValorMaximo"],
                                result["TipoValor"],
                                result["Periodicidade"],
                                bank["Cnpj"],
                                person,
                            )
                            true_results.append(data_tariffs_values_institutions)
                            print(data_tariffs_values_institutions)
                        else:
                            print("Empty Tariffs and value.")
            except (ConnectionError, requests.exceptions.HTTPError) as e:
                print(f"Connection error occurred: {e}.")
            except Exception as e:
                print(f"An error occurred: {e}.")
    return true_results
