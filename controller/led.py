import time
import MySQLdb

con = MySQLdb.connect(host="192.168.0.8", user="root", passwd="mysql", db="pi")
con.select_db('banco de dados')
con = MySQLdb.connect(user='root', db='pi')
cursor = con.cursor()
cursor.execute("INSERT INTO app2teste VALUES (%s)"%('OFF'))
con.commit()
rs = cursor.fetchall() # busca todas as linhas ou;
