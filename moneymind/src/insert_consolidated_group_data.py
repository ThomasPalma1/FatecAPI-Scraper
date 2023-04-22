from get_consolidated_group import get_consolidated_group
from mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


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
