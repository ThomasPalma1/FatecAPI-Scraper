from moneymind.src.mysql_initializer import establishing_mysql_connection
from moneymind.src.get.get_code_services import get_code_services

connection = establishing_mysql_connection()
cursor = connection.cursor()


def insert_all_data_code_services():
    services = get_code_services()
    count = 0
    for service in services:
        dados_serv = (service['Codigo'], service['Nome'])
        sql_service = "INSERT INTO lista_servicos (codigo, nome) VALUES (%s, %s)"
        value_service = dados_serv
        cursor.execute(sql_service, value_service)
        connection.commit()
        count += 1
        print(count, "code service")
    return cursor
