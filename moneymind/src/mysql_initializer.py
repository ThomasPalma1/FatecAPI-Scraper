import mysql.connector
import os
from dotenv import load_dotenv
import socket

dotenv_path = os.path.join(os.path.dirname(__file__), 'standard_database_information.env')
load_dotenv(dotenv_path)


def establishing_mysql_connection():
    host = os.getenv('MYSQL_HOST')
    host_docker = os.getenv('MYSQL_HOST_DOCKER')

    selected_host = host or host_docker
    # print(selected_host)
    # print(host, host_docker)

    if selected_host:
        try:
            connection = mysql.connector.connect(
                host=selected_host,
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD'),
                database=os.getenv('MYSQL_DATABASE'),
                port='3306'
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
            print("Failed to connect to MySQL database:", error)
            return None
    else:
        print("No MySQL host specified.")
        return None


connection = establishing_mysql_connection()
if connection:
    print("Connected to MySQL database!")
