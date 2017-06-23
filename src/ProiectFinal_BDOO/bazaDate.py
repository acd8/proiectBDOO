
#importare libraria MySQL pentru python
import MySQLdb;

#initializare date de conectare
host="localhost"
user="root"
password=""
bazaDate="aeroport"

#creare conexiune cu baza de date
db=MySQLdb.connect(host,user,password,bazaDate)

#crearea cursorului pentru alocarea zonei de memorie pentru interogari
cursor=db.cursor()

#realizarea interogatiei
cursor.execute("select * from pasager")

#afisare rezultate executie cursor
#nrDate=int(cursor.rowcount)
#for x in range(0, nrDate):
 #   row=cursor.fetchone()
  #  print row[0],"--->", row[1]

#alta varianta
#result = db.cursor.fetchall()
#for record in result:
# print record[0] , "=", record[1]


