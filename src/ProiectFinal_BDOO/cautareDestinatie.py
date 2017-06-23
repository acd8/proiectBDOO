import os
import conexiuneBaza
import MySQLdb

def cautadestinatii(bazaDate):
    cautare_destinatii = raw_input("Cautare destinatii")
    sql="Select oras_aterizare from sejur where oras_plecare='+cautare_destinatii+'"
    try:
        cursor = bazaDate.cursor()
        try:
            cursor.execute(sql)
            nrDate2 = int(cursor.rowcount)
            for x in range(0, nrDate2):
                row = cursor.fetchone()
                print"Destinatie:", row[0]
        except Exception, e:
            print  "Eroare: ", e
        bazaDate.commit()
        cursor.close()
    except Exception, e:
        print "Eroare interogatie la baza de date ->" + e
        print "Eroare la adaugarea in baza de date"