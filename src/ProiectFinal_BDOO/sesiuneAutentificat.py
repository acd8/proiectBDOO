import os

def meniuAutentificat(utilizator):
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    os.system('cls')
    print "                                               Bun venit " + utilizator
    print "_______________________________________________________________________"
    print "|   1.Biletele mele                                                    | "
    print "|   2.Cumparare bilet                                                  | "
    print "|   3.Cumparare bilet                                                  | "
    print "|   4.Pentru a va deconecta, scrieti \"deconectare\"                   | "
    print "|______________________________________________________________________|"
    optiune = raw_input("====: ")
    return optiune

def incepeSesiune(utilizator):
    optiune=""
    while(optiune!="deconectat"):
        optiune=meniuAutentificat(utilizator)
        if(optiune=="1"):
            print("Biletele mele sunt")
        if(optiune=="deconectare"):
            intrebare=raw_input("Doriti sa va deconectati?(y \ n):")
            if(intrebare=="y"):
                optiune="deconectat";



