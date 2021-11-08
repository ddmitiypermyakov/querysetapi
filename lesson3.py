import psycopg2

conn = psycopg2.connect(dbname='less_db', user='djdima',
                        password='djdima', host='localhost')
cursor = conn.cursor()
#
# sql = """CREATE TABLE less1
# (
#             Id SERIAL PRIMARY KEY,
#             FirstName CHARACTER VARYING(30),
#             LastName CHARACTER VARYING(30),
# 	        Email CHARACTER VARYING(30),
# 	        Age INTEGER);"""
# sql = """INSERT INTO product (product_name,
#                     company_name,
#                     description,
#                     price
#                             )
#             VALUES (
#                     'Grant',
#                     'Lada',
#                     'автомобиль',
#                     15000)"""

# sql = """SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name in ('LADA'));
# sql = """SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name = 'AUDI1' OR name = 'LADA1' OR name = 'fdfdg');
sql = """SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name NOT IN  ('AUDI') );
        
"""
# sql1 = '''SELECT * FROM  product  ;'''
cursor.execute(sql)

print(cursor.fetchall())
conn.commit()
conn.close()