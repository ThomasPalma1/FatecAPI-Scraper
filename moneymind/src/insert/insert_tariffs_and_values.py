from moneymind.src.get.get_tariffs_and_values import get_all_tariffs_and_value
from mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


def insert_all_tariffs_and_value():
    true_results = get_all_tariffs_and_value()
    count = 0

    for value in true_results:
        sql_tariffs_values = "INSERT INTO lista_tarifas_valores (cnpj, razao_social, valor_maximo, periodicidade, servico, grupo) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql_tariffs_values, value)
        connection.commit()
        count += 1
        print(count, "Tariffs and values.")

    return cursor
