import MySQLdb
stare=""
def CreeazaConexiune(host,user,parola,bazadate):

 try:
    db = MySQLdb.connect(host, user, parola,bazadate)
    print "Status baza de date: Conectat!"
    print "Denumire baza de date: "+bazadate
    stare="conectate"
    return db
 except Exception, e:
     print "Status baza de date: Deconectat!"
     stare="deconectat"
     print "Eroare la conexiunea cu baza de date! - ", e


