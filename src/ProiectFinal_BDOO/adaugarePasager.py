import os
import conexiuneBaza
import MySQLdb

def crearecont(bazaDate):
    numeadd = raw_input("Nume utilizator")
    prenumeadd=raw_input("Prenume utilizator")
    usernameadd = raw_input("Numele userului:")
    parolaadd = raw_input("Parola:")
    sql = 'INSERT INTO pasager(nume,prenume,username,parola) values ("%s", "%s", "%s", "%s")' %(numeadd, prenumeadd, usernameadd, parolaadd)

    try:
        cursor=bazaDate.cursor()
        try:
            cursor.execute(sql)
        except Exception, e:
            print  "Eroare: ", e
        bazaDate.commit()
        cursor.close()

    except Exception, e:
        print "Eroare interogatie la baza de date ->" + e
        print "Eroare la adaugarea in baza de date"
raw_input("Apasati 'Enter' pentru a continua.")

