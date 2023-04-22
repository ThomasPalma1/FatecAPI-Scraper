from get_institutions import get_institutions
from mysql_initializer import establishing_mysql_connection

connection = establishing_mysql_connection()
cursor = connection.cursor()


def get_and_insert_institutions():
    institutions = get_institutions()
    for bank in institutions:
        if bank["Cnpj"]:
            # Save the data in the database
            data_institutions_values = (
                bank["Cnpj"],
                bank["Nome"],
            )
            institutions = (
                "INSERT INTO instituicoes (cnpj, nome) VALUES (%s, %s)")
            value_institutions_values = data_institutions_values
            cursor.execute(institutions, value_institutions_values)
            connection.commit()
            print(cursor.rowcount, "insert institutions.")

    return cursor
