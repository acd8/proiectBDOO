import os
import stergereBilet
def meniuAutentificat(utilizator):
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    os.system('cls')
    print "                                               Bun venit " + utilizator
    print "_______________________________________________________________________"
    print "|   1.Biletele mele                                                    | "
    print "|   2.Cumparare bilet                                                  | "
    print "|   3.Cumparare bilet                                                  | "
    print "|   4.Stergere bilet                                                   | "
    print "|   5.Pentru a va deconecta, scrieti \"deconectare\"                   | "
    print "|______________________________________________________________________|"
    optiune = raw_input("====: ")
    return optiune

def incepeSesiune(utilizator):
    optiune=""
    while(optiune!="deconectat"):
        optiune=meniuAutentificat(utilizator)
        if(optiune=="1"):
            print("Biletele mele sunt")
        if (optiune == "4"):
            idBilet = raw_input("Intoduceti id-ul biletului:")
            stergereBilet.stergereInterogatie(db, idBilet, utilizator)
        if(optiune=="deconectare"):
            intrebare=raw_input("Doriti sa va deconectati?(y \ n):")
            if(intrebare=="y"):
                optiune="deconectat";



