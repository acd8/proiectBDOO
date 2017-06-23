import os
import conexiuneBaza
import MySQLdb

def verificareAutentificare(bazaDate):
    username=raw_input("Numele de uilizator:")
    parola=raw_input("Parola:")
    verificat="neverificat"
    sql="Select username,parola from pasager where username=\""+username+"\""
    cursor=bazaDate.cursor()
    try:
        cursor.execute(sql)
        nrDate=int(cursor.rowcount)
        if(nrDate != None):
            for x in range(0, nrDate):
                row=cursor.fetchone()
                usernameTemp=row[0]
                parolaTemp=row[1]
            if(usernameTemp==username and parolaTemp==parola):
                verificat="verificat"
            else:
                verificat="neverificat"
        else:
            print("Numele de utilizator sau parola sunt gresite!");
            returnare=raw_input("Apasati 0 pentru a iesi din program. Pentru a incerca din nou apasati tasta 1")

        print verificat
    except Exception, e:
        print "Eroare interogatie la baza de date ->", e
    bazaDate.commit()
    cursor.close()