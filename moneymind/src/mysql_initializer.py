import mysql.connector
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()


def establishing_mysql_connection():
    try:
        sleep(5)
        connection = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DATABASE'),
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
