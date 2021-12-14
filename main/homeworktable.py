import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#
# conn = psycopg2.connect(dbname='book1_db', user='testbook',\
#                         password='booktest', host='localhost')
con = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432")

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor =con.cursor()
db_ver=input('Enter name database ') #любое имя базы данных
sql_create_database = f'create database {db_ver}'
cursor.execute(sql_create_database)
person,passwords=input('Enter Role '),input('Enter password ')

sql_create_person = f"create user {person} with password '{passwords}' superuser"
cursor.execute(sql_create_person)

sql_create_privileges_for_db_person = f"GRANT ALL PRIVILEGES ON DATABASE {db_ver} to {person}"
cursor.execute(sql_create_privileges_for_db_person)


cursor.close()
con.close()
print("Соединение с PostgreSQL закрыто", )

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=person,
                                  # пароль, который указали при установке PostgreSQL
                                  password=passwords,
                                  host="127.0.0.1",
                                  port="5432",
                                  database=db_ver)

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")