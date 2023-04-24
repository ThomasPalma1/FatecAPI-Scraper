from sys_path import setup_sys_path
from insert.get_and_insert_all_tariffs_and_value import get_and_insert_all_tariffs_and_value
from insert.get_and_insert_institutions import get_and_insert_institutions
from insert.get_and_insert_institutions_tariffs import get_and_insert_institutions_tariffs
from insert.insert_all_data_code_services import insert_all_data_code_services
from insert.insert_consolidated_group_data import insert_consolidated_group_data
from mysql_initializer import establishing_mysql_connection



setup_sys_path()

connection = establishing_mysql_connection()
cursor = connection.cursor()


def application_startup():
    insert_all_data_code_services()
    insert_consolidated_group_data()
    get_and_insert_all_tariffs_and_value()
    get_and_insert_institutions()
    get_and_insert_institutions_tariffs()


application_startup()
cursor.close()
connection.close()
