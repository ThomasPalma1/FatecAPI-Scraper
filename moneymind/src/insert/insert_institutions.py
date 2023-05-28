from moneymind.src.get.get_institutions import get_institutions
from moneymind.src.mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


def insert_institutions():
    institutions = get_institutions()
    count = 0

    for bank in institutions:
        if bank["Cnpj"]:
            data_institutions_values = (
                bank["Cnpj"],
                bank["Nome"],
            )
            institutions_query = "INSERT INTO instituicoes (cnpj, nome) VALUES (%s, %s)"
            value_institutions_values = data_institutions_values
            cursor.execute(institutions_query, value_institutions_values)
            connection.commit()
            count += 1
            print(count, "insert institutions.")

    return cursor
