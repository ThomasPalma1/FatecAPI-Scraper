import requests
import json
from mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


# Gets the service from the first API link.

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


# Get all services
def get_code_services():
    url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifaPorValores/versao/v1/odata/ServicosBancarios"
    response = requests.get(url)
    data = json.loads(response.text)

    true_results = data['value']

    return true_results


# Save all services
def insert_all_data_code_services():
    services = get_code_services()
    for service in services:
        dados_serv = (service['Codigo'], service['Nome'])
        sql_service = "INSERT INTO lista_servicos (codigo, nome) VALUES (%s, %s)"
        value_service = dados_serv
        cursor.execute(sql_service, value_service)

        connection.commit()
        print(cursor.rowcount, "Code service")
    return cursor


# Get all consolidated groups

def get_consolidated_group():
    url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaValoresDeServicoBancario/versao/v1/odata" \
          f"/GruposConsolidados"
    response = requests.get(url)
    data = json.loads(response.text)
    true_results = data['value']
    return true_results


def insert_consolidated_group_data():
    consolidated_group = get_consolidated_group()
    for groups in consolidated_group:
        data_groups = (groups['Codigo'], groups['Nome'])
        sql_groups = "INSERT INTO grupos_consolidados (codigo, nome) VALUES (%s, %s)"
        value_groups = data_groups
        cursor.execute(sql_groups, value_groups)

        connection.commit()
        print(cursor.rowcount, "Consolidated group.")
    return cursor


# Get all rates and values list API

def get_and_insert_all_tariffs_and_value():
    consolidated_group = get_consolidated_group()
    services = get_code_services()

    for service in services:
        for group in consolidated_group:
            url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifaPorValores/versao/v1/odata/ListaTarifasPorValores(CodigoGrupoConsolidado=@CodigoGrupoConsolidado,CodigoServico=@CodigoServico)?@CodigoGrupoConsolidado='{group['Codigo']}'&@CodigoServico='{service['Codigo']}'&$top=10000&$format=json"
            response = requests.get(url)
            data = json.loads(response.text)
            true_results = data['value']

            if true_results:

                for tr in true_results:
                    # Checks if API data is null
                    if tr["Cnpj"]:
                        # Save the data in the database
                        data_tariffs_values = (
                            tr["Cnpj"],
                            tr["RazaoSocial"],
                            tr["ValorMaximo"],
                            tr["Periodicidade"],
                            service["Codigo"],
                            group["Codigo"],
                        )
                        sql_tariffs_values = (
                            "INSERT INTO lista_tarifas_valores (cnpj, razao_social, valor_maximo, periodicidade, servico, grupo) VALUES (%s, %s, %s, %s, %s, %s)")
                        value_tariffs_values = data_tariffs_values
                        cursor.execute(sql_tariffs_values, value_tariffs_values)
                        connection.commit()
                        print(cursor.rowcount, "Tariffs and value.")
            else:
                print("Empty Tariffs and value.")
    return cursor


insert_all_data_code_services()
insert_consolidated_group_data()
get_and_insert_all_tariffs_and_value()

cursor.close()
connection.close()
