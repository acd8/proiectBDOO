import os
import MySQLdb
host="localhost"
user="root"
password=""
bazaDate="aeroport"
def stergereInterogatie(db,idBilet,utilizator):
    #sql = ('Select oras_aterizare from sejur where oras_plecoare="%s"' % (cautare_destinatii))
    db = MySQLdb.connect(host, user, parola, bazadate)
    sql1=('DELETE FROM bilet where id_bilet="%s" && id_pasager=(select id_pasager from pasager where username="%s");'%(idBilet, utilizator))
    try:
        cursor = db.cursor()
        try:
            cursor.execute(sql1)
        except Exception, e:
            print  "Eroare: ", e


    except Exception, e:
        print "Eroare interogatie la baza de date -> stergere" + e
        print "Eroare la adaugarea in baza de date"
    db.commit()
    cursor.close()



