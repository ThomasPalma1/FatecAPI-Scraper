from src.get.get_consolidated_group import get_consolidated_group
from src.get.get_code_services import get_code_services
import json
import requests

from src.mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


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
