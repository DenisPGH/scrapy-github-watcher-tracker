from datetime import date

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="roboweb_db",
    user="denis_postgre",
    password="D_12-K9")

cursor=conn.cursor()
#cursor.execute("CREATE TABLE github (date date,time time, names varchar )")
cursor.execute("INSERT INTO github(date,time,names ) VALUES ('2022-02-02','14:00:00','Deni')")
conn.commit()


conn.close()
cursor.close()

print(conn.info)