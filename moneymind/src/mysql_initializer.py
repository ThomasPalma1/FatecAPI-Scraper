import mysql.connector


def establishing_mysql_connection():
    mysql_user = input("Enter your MySQL username: ")
    mysql_password = input("Enter your MySQL password: ")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=mysql_user,
            password=mysql_password,
            database="money_mind",
        )
        cursor = connection.cursor()
        print("Connected to MySQL database!")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS grupos_consolidados (id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(50) NOT NULL, nome VARCHAR(256) NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS lista_servicos (id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(50) NOT NULL, nome VARCHAR(256) NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS lista_tarifas_valores (id INT AUTO_INCREMENT PRIMARY KEY, cnpj VARCHAR(50) NOT NULL, razao_social VARCHAR(256) NOT NULL, valor_maximo VARCHAR(256) NOT NULL, periodicidade VARCHAR(256) NOT NULL, servico VARCHAR(50), grupo VARCHAR(50))"
        )
        connection.commit()
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
        return None
