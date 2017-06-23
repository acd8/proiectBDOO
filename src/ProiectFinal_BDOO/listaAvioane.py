import os
import conexiuneBaza
import MySQLdb
import datetime
def afisareDestinatii(bazaDate):
    sql="Select * from avion"
    cursor=bazaDate.cursor()
    try:
        cursor.execute(sql)
        nrDate=int(cursor.rowcount)
        for x in range(0, nrDate):
           row=cursor.fetchone()
           print "ID Avion:",row[0], " Denumire Avion:", row[1]
    except Exception, e:
        print "Eroare interogatie la baza de date ->", e
        bazaDate.commit()
        cursor.close()
        bazaDate.commit()
