from get.get_institutions import get_institutions
import json
import requests
from mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


def get_and_insert_institutions_tariffs():
    institutions = get_institutions()
    type_person = ['F', 'J']
    count = 0

    for person in type_person:
        for bank in institutions:
            url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifasPorInstituicaoFinanceira/versao/v1/odata/ListaTarifasPorInstituicaoFinanceira(PessoaFisicaOuJuridica=@PessoaFisicaOuJuridica,CNPJ=@CNPJ)?@PessoaFisicaOuJuridica='{person}'&@CNPJ='{bank['Cnpj']}'&$top=10000&$format=json"
            response = requests.get(url)
            data = json.loads(response.text)
            true_results = data['value']

            if true_results:
                for tr in true_results:
                    if bank["Cnpj"]:
                        data_tariffs_values_institutions = (
                            tr["CodigoServico"],
                            tr["Servico"],
                            tr["Unidade"],
                            tr["DataVigencia"],
                            tr["ValorMaximo"],
                            tr["TipoValor"],
                            tr["Periodicidade"],
                            bank["Cnpj"],
                            person,
                        )
                        sql_tariffs_values_institutions = "INSERT INTO lista_tarifas_instituicoes (codigo_servico, servico, unidade, data_vigencia, valor_maximo, tipo_valor, periodicidade, cnpj, pessoa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        value_tariffs_values_institutions = data_tariffs_values_institutions
                        cursor.execute(sql_tariffs_values_institutions, value_tariffs_values_institutions)
                        connection.commit()
                        count += 1
                        print(count, "Tariffs Institutions.")
            else:
                print("Empty Tariffs Institutions.")
    return cursor
