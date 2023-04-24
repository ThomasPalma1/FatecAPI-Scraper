import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def establishing_mysql_connection():
    try:
        connection = mysql.connector.connect(
            # host=os.environ.get('MYSQL_HOST'), # if you want to run the code locally, just comment out this line
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DATABASE'),
        )
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS grupos_consolidados (id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(50) NOT NULL, nome VARCHAR(256) NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS lista_servicos (id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(50) NOT NULL, nome VARCHAR(256) NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS lista_tarifas_valores (id INT AUTO_INCREMENT PRIMARY KEY, cnpj VARCHAR(50) NOT NULL, razao_social VARCHAR(256) NOT NULL, valor_maximo VARCHAR(256) NOT NULL, periodicidade VARCHAR(256) NOT NULL, servico VARCHAR(50), grupo VARCHAR(50))"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS instituicoes (id INT AUTO_INCREMENT PRIMARY KEY, cnpj VARCHAR(50) NOT NULL, nome VARCHAR(256) NOT NULL)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS lista_tarifas_instituicoes (id INT AUTO_INCREMENT PRIMARY KEY, codigo_servico VARCHAR(50) NOT NULL, servico VARCHAR(256) NOT NULL, unidade VARCHAR(256) NOT NULL, data_vigencia VARCHAR(256) NOT NULL, valor_maximo FLOAT NOT NULL, tipo_valor VARCHAR(50),periodicidade VARCHAR(50),cnpj VARCHAR(50),pessoa VARCHAR(50))"
        )
        connection.commit()
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
        return None


connection = establishing_mysql_connection()
if connection:
    print("Connected to MySQL database!")
