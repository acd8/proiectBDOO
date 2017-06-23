import os
import conexiuneBaza
import autentificareUser
import listaDestinatii
import adaugarePasager
import listaAvioane

host="localhost"
user="root"
parola=""
bazaDate="aeroport"
db=conexiuneBaza.CreeazaConexiune(host,user,parola,bazaDate)
def meniu():
    os.system('cls')
    print "_______________________________________________________________________"
    print "|Universitatea 1 Decembrie 1918 din Alba-Iulia      PABD 2017 v.0.0.1  |"
    print "|Baze de date orientate obiect                                         |"
    print "|                             Aplicate aeroport                        |"
    print "|                                             Donea Alexandru-Cristian |"
    print "|                                                          Boldea Raul |"
    print "|  1.Autentificare                                                     |"
    print "|  2.Creare cont                                                       |"
    print "|  3.Cautare destinatii                                                |"
    print "|  4.Lista destinatii                                                  |"
    print "|  5.Afisare Avioane                                                   |"
    print "|  6.Iesire din aplicatie                                              |"
    print "|  7.GITHUB                                                            |"
    print "|______________________________________________________________________|"
    optiune = raw_input("====: ")
    return optiune

optiune=""
while(optiune!="7"):
    opt=meniu()
    if(opt=="1"):
        autentificareUser.verificareAutentificare(db)
    elif(opt=="2"):
        adaugarePasager.crearecont(db)
    elif (opt == "3"):
        text()
    elif(opt=="4"):
        listaDestinatii.afisareDestinatii(db)
    elif(opt=="5"):
        listaAvioane.afisareDestinatii(db)