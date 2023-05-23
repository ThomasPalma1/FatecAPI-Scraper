from get.get_tariffs_and_value import get_all_tariffs_and_value
from get.get_consolidated_group import get_consolidated_group
from get.get_code_services import get_code_services
from mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


def insert_all_tariffs_and_value():
    print('entrando aqui 1')
    true_results = get_all_tariffs_and_value()
    print('entrando aqui 2')
    consolidated_groups = get_consolidated_group()
    print('entrando aqui 3')
    services = get_code_services()
    print('entrando aqui 4')
    count = 0
    if true_results:
        for tr in true_results:
            if tr:
                for brackets in tr:
                    if brackets["Cnpj"]:
                        data_tariffs_values = (
                            brackets["Cnpj"],
                            brackets["RazaoSocial"],
                            brackets["ValorMaximo"],
                            brackets["Periodicidade"],
                            services["Codigo"],
                            consolidated_groups["Codigo"],
                        )

                        sql_tariffs_values = "INSERT INTO lista_tarifas_valores (cnpj, razao_social, valor_maximo, periodicidade, servico, grupo) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql_tariffs_values, data_tariffs_values)
                        connection.commit()
                        count += 1
                        print(count, "Tariffs and value.")
    else:
        print("Empty Tariffs and value.")

    return cursor
