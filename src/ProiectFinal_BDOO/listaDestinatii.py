import os
import conexiuneBaza
import MySQLdb
import datetime
def afisareDestinatii(bazaDate):
    sql="Select * from sejur WHERE data_plecare >= CURDATE() AND ora_plecare >= CURTIME()"
    cursor=bazaDate.cursor()
    try:
        cursor.execute(sql)
        a=datetime.datetime.now().strftime("%Y-%m-%d")
        datetime.datetime.now().strftime("%H:%M:%S")
        nrDate=int(cursor.rowcount)
        for x in range(0, nrDate):
           row=cursor.fetchone()
           print "ID-plecare:",row[0], " Numar Avion:", row[1]," Oras plecare:",row[2],"Oras destinatie:",row[3],"Data plecare:",row[4],"Ora plecare:",row[5],"Data Aterizare:",row[6],"Ora Aterizare:",row[7]
    except Exception, e:
        print "Eroare interogatie la baza de date ->", e
        bazaDate.commit()
        cursor.close()
        bazaDate.commit()
