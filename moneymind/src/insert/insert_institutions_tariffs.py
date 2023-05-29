from moneymind.src.mysql_initializer import establishing_mysql_connection
from moneymind.src.get.get_institutions_tariffs import get_institutions_tariffs

connection = establishing_mysql_connection()
cursor = connection.cursor()


def insert_institutions_tariffs():
    true_results = get_institutions_tariffs()
    count = 0

    for value in true_results:
        sql_tariffs_values_institutions = "INSERT INTO lista_tarifas_instituicoes (codigo_servico, servico, unidade, data_vigencia, valor_maximo, tipo_valor, periodicidade, cnpj, pessoa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_tariffs_values_institutions, value)
        connection.commit()
        count += 1
        print(count, "Tariffs Institutions.")

    return cursor
