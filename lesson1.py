import sqlite3

conn = sqlite3.connect('db.sqlite3') #создает соединение с БД
# print(dir(conn))
cursor = conn.cursor() #поставь курсор в SQL
SQL = '''INSERT INTO main_auto ('name','price', 'brand_id')
         VALUES ('XRS', 45, 1)
 '''
# print(dir(cursor),'object cursor')
c=cursor.execute(SQL) #Выполнить запрос
# print(dir(c))
conn.commit()
print(cursor.fetchall())
conn.close()


